import zipfile
z = zipfile.ZipFile("a.zip")
for name in z.namelist():
    print
    print "FILE:", name
    print
    print z.read(name)


# zipfile module provides interface to read and write zip files.
