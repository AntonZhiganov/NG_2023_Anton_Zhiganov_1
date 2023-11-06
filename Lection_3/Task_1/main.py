userFile = input("Enter full name you file: ")
openFile = open(userFile, 'r')
contentFile = openFile.read()

result = {}
for char in set(contentFile):
    result.update({char : contentFile.count(char)})

print(result)

openFile.cloce()