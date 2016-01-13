from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

in_file = open(from_file)
indata = in_file.read()

print "The input file is %d bytes long" % len(indata)

print "Does the output file exist? %r" % exists(to_file)
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()

out_file = open(to_file, 'w')
out_file.write(indata)

print "Alright, all done."

out_file.close()
in_file.close()


# Understands following points in exercise 17
# Got the idea of how to copy content from one file to another file.
# Here used os.path madule to use exists. Which is return true if file path refers to an existing path.
# If file not target file is not exists, it will create new file.
# len function is used to gets the length of the string.