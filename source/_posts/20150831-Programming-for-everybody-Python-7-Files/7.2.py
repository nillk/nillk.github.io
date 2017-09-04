fname = raw_input("Enter file name: ")
fh = open(fname)
count = 0
sum = 0.0
for line in fh:
	if line.startswith("X-DSPAM-Confidence:"):
		count = count + 1
		pos = line.find(":")
		sum = sum + float(line[pos + 1:])
print 'Average spam confidence:',(sum / count)
