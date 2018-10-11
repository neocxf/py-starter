import random
import re
import docx

file = open("employee.txt", "r")
# print(file.read())

# for line in file:
#     print(line)
lastLine = ''
for line in file.readlines():
    print(line, end='')
    lastLine = line

pattern = re.compile(r'.*?([0-9]+)$')

try:
    idx = int(pattern.match(lastLine).group(1))
except ValueError:
    idx = 0
except IndexError:
    idx = 0
except AttributeError:
    idx = 0

idx += 1

randInt = random.randint(1, 20)

file = open("employee.txt", 'a')

for i in range(idx, randInt + idx, 1):
    file.write("\nneo%d" % i)

file.close()

print(docx.Document.__doc__)
