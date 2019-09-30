oldfile = open("sqlservr.old", "rb").read()
newfile = oldfile.replace("\x00\x94\x35\x77", "\x00\x80\x84\x1e")
open("sqlservr", "wb").write(newfile)
exit()