fname = input("Enter file name: ")
fh = open(fname)
fread = fh.read()
ly = fread.rstrip()
lz = ly.upper()
print(lz)