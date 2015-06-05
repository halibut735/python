import sys, string, os, shutil

def RenameFiles(srcdir):
    srcfiles = os.listdir(srcdir)

    for srcfile in srcfiles:
        destfile = srcdir + "/" + srcfile[3:]
        srcfile = os.path.join(srcdir, srcfile)
        os.rename(srcfile, destfile)

srcdir = "qq"
RenameFiles(srcdir)
