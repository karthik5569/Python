#Task1
try:
    file = open("sample.txt", "r")
    print("Reading file content:")
    line_number = 1
    for line in file:
        print("Line", line_number, ":", line.strip())
        line_number += 1
    file.close()
except:
    print("Error: The file 'sample.txt' was not found.")

#Task2
text1 = input("Enter text to write to the file: ")
file = open("output.txt", "w")
file.write(text1 + "\n")
file.close()
print("Data successfully written to output.txt.")

text2 = input("Enter additional text to append: ")
file = open("output.txt", "a")
file.write(text2 + "\n")
file.close()
print("Data successfully appended.")

print("\nFinal content of output.txt:")
file = open("output.txt", "r")
print(file.read())
file.close()
