import os
import shutil


def copyfile(srcdir, dstdir):
    if not os.path.exists(srcdir):
        print ("src path not exist!")
    if not os.path.exists(dstdir):
        os.mkdir(dstdir)

    for Dir, subdir, files in os.walk(srcdir):
        for srcfile in files:
            shutil.copy(os.path.join(Dir, srcfile), dstdir)
            print("srcfile:"+srcfile + " copy succeeded !")


def Rename(path):
    for files in os.listdir(path):
        portion = os.path.splitext(files)
        print portion
        if portion[1] ==".txt":
            newname = portion[0]+".png"
            os.chdir("/home/media/ck+/Emotions_t")
            os.rename(files, newname)

def cutname(path):
    for files in os.listdir(path):
        olddir = os.path.join(path, files)
        filesname = files[:17] + files[-4:]
        print files
        Newdir = os.path.join(path, filesname)
        os.rename(olddir, Newdir)

def extract_names(path):
    dict = {}
    x = os.listdir(path)
    #print len(os.listdir(path))
    for i in range(len(os.listdir(path))):
        #print i, x[i]
        f = open(os.path.join(path, x[i]), 'r')
        dict[x[i]] = f.read().strip()[:1]
        f.close()
        #print dict
    return dict

def get_keys(d, value):

    for k, v in d.items():
        if v == value:
            return k


def extract_imgs(dir):
    #list = ['neutral', 'anger', 'contempt', 'disgust', 'fear', 'happy', 'sadness','surprise']
    #srcdir = "/"
    imgdir = "/home/media/ck+/cohn-images"
    #imgpath = "/home/media/ck+/imgs/anger"
    #idir = "/home/media/ck+/Emotions_txt"
    for img in os.listdir(imgdir):
        for tfiles in os.listdir(dir):
            #for images in img:
                if os.path.splitext(img)[0] == os.path.splitext(tfiles)[0]:
                    #shutil.copy(os.path.join(imgdir, img), dir)
                    shutil.copyfile(os.path.join(imgdir, img), os.path.join(dir, tfiles))
                    print("image %s has been covered with %s" % (img, tfiles))

def sortimages(dir):
    Dir = "/home/media/ck+/imgs/anger"
    dict = extract_names(dir)
    print dict
    for k, v in dict.items():
        if v == 1:
            shutil.copyfile(os.path.join(dir, k), os.path.join(Dir, k))
