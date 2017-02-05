from sys import argv
from os.path import exists

# Set arguments
script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

# we could do these two one line, how?
in_file = open(from_file)
indata = in_file.read()

# Printing number of bytes in the file
print "The input file is %d bytes long" % len(indata)

# exists() is used to check if file with that name does exist
print "Does the output file exist? %r" % exists(to_file)
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()

# Specifying w when opening the file because it will be written to
out_file = open(to_file, 'w')
out_file.write(indata)

print "Alright, all done."

# Close both files
out_file.close()
in_file.close()

# Syntax for creating txt file
# echo "This is a text file" test.text
# Syntax for opening txt file
# cat test.txt
