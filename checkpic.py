from PIL import Image
import imagehash,os,imghdr,sys

def makehach(path):
    with open(path+'/hash.txt','w+') as file:
        for root, dirs, files in os.walk(path):
            for filename in files:
                if imghdr.what(os.path.join(root, filename)) in ['jpeg','png']:
                    hash = imagehash.average_hash(Image.open(os.path.join(root, filename)))
                    file.write(f"{hash},{os.path.join(root, filename)}\n")
    print("finish")

def checkhash(filename):
    if imghdr.what(filename) in ['jpeg', 'png']:
        hash = imagehash.average_hash(Image.open(filename))
    with open('hash.txt', 'r') as file:
        for i in file:
            hashfile = file.readline().split(',')
            if str(hash)==hashfile[0]:
                print(f'they are same pic: {filename}, {hashfile[1]}')
    print("finish")
                    

if len(sys.argv)<2:
    print("no argument")
    sys.exit()
elif sys.argv[1]=="makehash":
    makehach(sys.argv[2])
elif sys.argv[1]=='checkhash':
    checkhash(sys.argv[2])
else:
    print("cmd wrong,please input makehash or checkhash")
