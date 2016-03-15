formatter = "%r %r %r"

print formatter % (1, 2, 3)

print formatter % (formatter % (1, 2, 3), formatter % ("one", "two", "three"), formatter % (True, False, True))
