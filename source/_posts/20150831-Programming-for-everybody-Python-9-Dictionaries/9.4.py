name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

messages = dict()
maxKey = ''
maxValue = 0

for line in handle:
	if line.startswith("From "):
		mail = line.split()[1]
		messages[mail] = messages.get(mail, 0) + 1
		if messages[mail] > maxValue:
			maxKey = mail
			maxValue = messages[mail]

print maxKey, maxValue