import os
from pathlib import Path

rootBackup = Path("C:/findfiles/picture_icon_video_play/")
root = Path("C:/MyFiles/AndroidProd/app/src/main/res")
searchFileName = [ "picture_icon_video_play"
    # "drop",
    # "friends",
    # "picture_icon_grey_org_normal",
    # "user",
    # "add_img",
    # "like",
    # "ic_icon_after_like",
    # "img_seekbar",
    # "logo_text",
    # "img_mve",
    # "img_ovrlap",
    # "like_img",
    # "ic_frndreq","ic_backgrnd_img","ic_icon_cmnt","icon_eyes"
]
totalFilesCopies = []

def createDir(dirName):
    try :
        print(dirName) 
        os.mkdir(dirName)
    except FileExistsError :   
        print("Folder Already Exsist") 
    except:
        print('Something Wrong')
        raise


def cleanup():
    createDir(rootBackup)
    
    for file in root.glob('**/*.*'):
        base=os.path.basename(str(file))
        baseName = os.path.splitext(base)[0]
        if (baseName in searchFileName ):
            print('********** File Found**********', file.name)
            print('Try to COPY File - ', file.name)
            try:
               localDir = rootBackup / file.parent.name
               createDir(localDir)
               os.system('copy '+ str(file) + ' '+ str(localDir/file.name))
            except:
              raise
            print('********** File Copied :)********** \n')
            totalFilesCopies.append(file.name)

cleanup()
print('\n**********************************************************************')
print(len(totalFilesCopies))
# print(totalFilesCopies)
print('************************File Copy DONE********************************\n')