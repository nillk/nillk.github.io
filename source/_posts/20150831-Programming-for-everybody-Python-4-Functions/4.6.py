def computepay(h,r):
    if h > 40:
        realH = 40 + (h - 40) * 1.5
        return realH * r
    else:
        return h * r

hrs = raw_input("Enter Hours:")
print computepay(float(hrs), 10.50)