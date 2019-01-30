hrs = raw_input("Enter Hours:")
rate = raw_input("Enter Rate:")
h = float(hrs)
if h > 40:
    h = (h - 40) * 1.5 + 40
r = float(rate)
print h * r