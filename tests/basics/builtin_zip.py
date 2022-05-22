try:
    zip
    set
except NameError:
    print("SKIP")
    raise SystemExit

print(list(zip()))
print(list(zip([1], {2, 3})))
