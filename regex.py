import re

numberPattern = re.compile(r'.*?([0-9]+)$')

print(numberPattern.match("are23").group(1))
print(numberPattern.match("are23a"))
