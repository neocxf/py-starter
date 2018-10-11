i = 0
while i < 10:
    print(i)
    i = i + 1

print("Done with loop")

for j in range(6):
    print(j)

'''
comment1
comment2
'''


def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation = translation + "G"
            else:
                translation = translation + "g"

        else:
            translation = translation + letter
    return translation


print(translate(input("Enter a phrase: ")))
