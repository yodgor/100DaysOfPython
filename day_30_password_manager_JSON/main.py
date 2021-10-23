#FileNotFound Error

try:
    file = open("a_file.txt")
except FileNotFoundError:
    file = open("a_file.txt", "w")
    file.write("Something")
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print("file was closed")
    raise TypeError("This is an error I made up.")