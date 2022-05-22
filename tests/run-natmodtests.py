#!/usr/bin/env python3

# This file is part of the MicroPython project, http://micropython.org/
# The MIT License (MIT)
# Copyright (c) 2019 Damien P. George

import os
import subprocess
import sys
import argparse

sys.path.append("../tools")
import pyboard

# Paths for host executables
CPYTHON3 = os.getenv("MICROPY_CPYTHON3", "python3")
MICROPYTHON = os.getenv("MICROPY_MICROPYTHON", "../ports/unix/micropython-coverage")

NATMOD_EXAMPLE_DIR = "../examples/natmod/"

# Supported tests and their corresponding mpy module
TEST_MAPPINGS = {
    "btree": "btree/btree_$(ARCH).mpy",
    "framebuf": "framebuf/framebuf_$(ARCH).mpy",
    "uheapq": "uheapq/uheapq_$(ARCH).mpy",
    "urandom": "urandom/urandom_$(ARCH).mpy",
    "ure": "ure/ure_$(ARCH).mpy",
    "uzlib": "uzlib/uzlib_$(ARCH).mpy",
}

# Code to allow a target MicroPython to import an .mpy from RAM
injected_import_hook_code = """\
import usys, uos, uio
class __File(uio.IOBase):
  def __init__(self):
    self.off = 0
  def ioctl(self, request, arg):
    return 0
  def readinto(self, buf):
    buf[:] = memoryview(__buf)[self.off:self.off + len(buf)]
    self.off += len(buf)
    return len(buf)
class __FS:
  def mount(self, readonly, mkfs):
    pass
  def chdir(self, path):
    pass
  def stat(self, path):
    if path == '__injected.mpy':
      return tuple(0 for _ in range(10))
    else:
      raise OSError(-2) # ENOENT
  def open(self, path, mode):
    return __File()
uos.mount(__FS(), '/__remote')
uos.chdir('/__remote')
usys.modules['{}'] = __import__('__injected')
"""


class TargetSubprocess:
    def __init__(self, cmd):
        self.cmd = cmd

    def close(self):
        pass

    def run_script(self, script):
        try:
            p = subprocess.run(
                self.cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, input=script
            )
            return p.stdout, None
        except subprocess.CalledProcessError as er:
            return b"", er


class TargetPyboard:
    def __init__(self, pyb):
        self.pyb = pyb
        self.pyb.enter_raw_repl()

    def close(self):
        self.pyb.exit_raw_repl()
        self.pyb.close()

    def run_script(self, script):
        try:
            self.pyb.enter_raw_repl()
            output = self.pyb.exec_(script)
            output = output.replace(b"\r\n", b"\n")
            return output, None
        except pyboard.PyboardError as er:
            return b"", er


def run_tests(target_truth, target, args, stats):
    for test_file in args.files:
        # Find supported test
        for k, v in TEST_MAPPINGS.items():
            if test_file.find(k) != -1:
                test_module = k
                test_mpy = v.replace("$(ARCH)", args.arch)
                break
        else:
            print(f"----  {test_file} - no matching mpy")
            continue

        # Read test script
        with open(test_file, "rb") as f:
            test_file_data = f.read()

        # Create full test with embedded .mpy
        try:
            with open(NATMOD_EXAMPLE_DIR + test_mpy, "rb") as f:
                test_script = b"__buf=" + bytes(repr(f.read()), "ascii") + b"\n"
        except OSError:
            print(f"----  {test_file} - mpy file not compiled")
            continue
        test_script += bytes(injected_import_hook_code.format(test_module), "ascii")
        test_script += test_file_data

        # Run test under MicroPython
        result_out, error = target.run_script(test_script)

        # Work out result of test
        extra = ""
        if error is None and result_out == b"SKIP\n":
            result = "SKIP"
        elif error is not None:
            result = "FAIL"
            extra = f" - {str(error)}"
        else:
            # Check result against truth
            try:
                with open(f"{test_file}.exp", "rb") as f:
                    result_exp = f.read()
                error = None
            except OSError:
                result_exp, error = target_truth.run_script(test_file_data)
            if error is not None:
                result = "TRUTH FAIL"
            elif result_out != result_exp:
                result = "FAIL"
                print(result_out)
            else:
                result = "pass"

        # Accumulate statistics
        stats["total"] += 1
        if result == "SKIP":
            stats["skip"] += 1
        elif result == "pass":
            stats["pass"] += 1
        else:
            stats["fail"] += 1

        # Print result
        print("{:4}  {}{}".format(result, test_file, extra))


def main():
    cmd_parser = argparse.ArgumentParser(
        description="Run dynamic-native-module tests under MicroPython"
    )
    cmd_parser.add_argument(
        "-p", "--pyboard", action="store_true", help="run tests via pyboard.py"
    )
    cmd_parser.add_argument(
        "-d", "--device", default="/dev/ttyACM0", help="the device for pyboard.py"
    )
    cmd_parser.add_argument(
        "-a", "--arch", default="x64", help="native architecture of the target"
    )
    cmd_parser.add_argument("files", nargs="*", help="input test files")
    args = cmd_parser.parse_args()

    target_truth = TargetSubprocess([CPYTHON3])

    if args.pyboard:
        target = TargetPyboard(pyboard.Pyboard(args.device))
    else:
        target = TargetSubprocess([MICROPYTHON])

    stats = {"total": 0, "pass": 0, "fail": 0, "skip": 0}
    run_tests(target_truth, target, args, stats)

    target.close()
    target_truth.close()

    print(f'{stats["total"]} tests performed')
    print(f'{stats["pass"]} tests passed')
    if stats["fail"]:
        print(f'{stats["fail"]} tests failed')
    if stats["skip"]:
        print(f'{stats["skip"]} tests skipped')

    if stats["fail"]:
        sys.exit(1)


if __name__ == "__main__":
    main()
