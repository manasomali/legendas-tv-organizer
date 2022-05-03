import os
from zipfile import ZipFile
import shutil
from send2trash import send2trash

def get_size(start_path):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
    return total_size

def extract_zip():
    for name in os.listdir("."):
        if name[-4:]==".zip":    
            with ZipFile(name, 'r') as zipObj:
               zipObj.extractall()
    
def find_video_file():
    for name in os.listdir("."):
        if name[-4:]==".mp4" or name[-4:]==".mkv" or name[-4:]==".avi":
            return name[:-4]

def move_sub_to_root(correctsub):
    for dirpath, dirnames, filenames in os.walk("."):
        for f in filenames:
            if f==correctsub+str(".srt"):
                shutil.move(os.path.join(dirpath, f), os.path.join(os.getcwd(), f))

def delete_useless_files():
    for name in os.listdir("."):
        if os.path.isdir(name):
            if get_size(name) < 9000000:
                send2trash(name)
        else:
            ex=name[-4:].lower()
            if ex==".txt" or ex==".jpg" or ex==".exe" or ex==".zip" or ex ==".nfo":
                send2trash(name)

def get_names_subs():
    subs=[]
    for dirpath, dirnames, filenames in os.walk("."):
        for f in filenames:
            if f[-4:]==".srt":
                subs.append(f[:-4])
            
    return subs

def get_correct_sub(videoname,subs):
    points=[0]*(len(subs))
    for i in range(0, len(subs)):
        for wordsub in subs[i].lower().replace("-", ".").replace(" ", ".").split("."):
            if wordsub.lower() in videoname.lower().replace("-", ".").replace(" ", ".").split("."):
                points[i]+=1
            else:
                points[i]-=1

    return subs[points.index(max(points))]

def main():
    extract_zip()
    subs = get_names_subs()
    videoname = find_video_file()
    correctsub = get_correct_sub(videoname,subs)
    move_sub_to_root(correctsub)
    delete_useless_files()
    
main()
