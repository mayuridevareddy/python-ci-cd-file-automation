# Writing to a file
with open("sample.txt", "w") as file:
    file.write("Hello DevOps World!\n")
    file.write("This is a CI/CD pipeline demo.\n")

# Reading from the file
with open("sample.txt", "r") as file:
    content = file.read()
    print("File Content:\n", content)

print("Script executed successfully")