name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

count = dict()
for line in handle:
	if line.startswith("From "):
		hour = line.split()[5].split(":")[0]
		count[hour] = count.get(hour, 0) + 1

hourList = list()
for h, c in count.items():
	hourList.append((h, c))

hourList.sort()

for h, c in hourList:
	print h, c