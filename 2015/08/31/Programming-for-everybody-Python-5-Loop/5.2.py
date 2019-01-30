largest = None
smallest = None
while True:
    num = raw_input("Enter a number: ")
    if num == "done" : break
    try:
        n = int(num)
        if smallest is None:
            smallest = n
        if n < smallest:
            smallest = n
        if n > largest:
            largest = n
    except:
        print "Invalid input"

print "Maximum is", largest
print "Minimum is", smallest