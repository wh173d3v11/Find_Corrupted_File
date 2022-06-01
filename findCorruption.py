import os
from pathlib import Path

rootBackup = Path("C:/MyFiles/backupBeta16DEC")
rootBackup2 = Path("C:/MyFiles/backup2")
root = Path("C:/MyFiles/Android_Beta_1/app/src/main")

totalCorruptedFiles = []

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
    createDir(rootBackup2)
    for file in root.glob('**/*.*'):
        size = os.path.getsize(file)
        if size == 0:
            print('**********Corrupted File Found - **********', file.name)
            print('Try to Moving Corrupted File - ', file.name)
            try:
               localDir = rootBackup / file.parent.name
               createDir(localDir)
               file.rename(localDir / file.name)
            except:
               print('File Already Exists!!')
               localDir2 = rootBackup2 / file.parent.name
               createDir(localDir2)
               file.rename(localDir2 / file.name)
               print('Moved in backupo 2')
            print('**********Corrupted File Moved :)********** \n')
            totalCorruptedFiles.append(file.name)

cleanup()
print('\n**********************************************************************')
print(len(totalCorruptedFiles))
# print(totalCorruptedFiles)
print('************************CLEAN UP DONE********************************\n')