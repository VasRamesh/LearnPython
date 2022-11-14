# How to read in files (file name = Readin.txt)

# File name/path , mode (r = reading, w = writing, a = append onto file, r+ = read and write)
ex_text = open("Readin.txt", "r")
print(ex_text.readable())  # Returns boolean value True if file is readable (change with mode)

# Read the file line-by-line
print(ex_text.readline())

# Read the entire file:
print(ex_text.read())

# Read and store the file lines in array format
print(ex_text.readlines())
for names in ex_text:
    print(names)
ex_text.close()  # Should close a file after you are done using it

# Append in files: (w - write will override old file)
write_in_file = open("Readin.txt", "a")
write_in_file.write("\ngoo")
write_in_file.close()


