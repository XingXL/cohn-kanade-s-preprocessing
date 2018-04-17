from utils import extract_names, extract_imgs, copyfile, Rename, sortimages,cutname
srcdir = "/home/media/ck+/Emotion"
dstdir = "/home/media/ck+/Emotions_t" # ***The chosen one***
dataimg = "/home/media/ck+/cohn-kanade-images"
images = "/home/media/ck+/cohn-images"
dddir = "/home/media/ck+/emotion"

if __name__ == '__main__': # You can Switch the function below manually.

    #Rename(dstdir)
    #copyfile(dataimg, images)
    #extract_names(dstdir)
    #extract_imgs(dstdir)
    sortimages(dddir)
    #cutname(dddir)