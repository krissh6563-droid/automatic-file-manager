import shutil
import os 

#function tp check file exit to the destinatio folder or not
def file_check(source_path, des_path):
    dir = os.listdir(des_path)
       
#function to make a foler named Executable
def folder_create(source_path):
    dir = os.listdir(source_path)
    for item in dir:
        if item.endswith('.exe') or item.endswith('.msi') :
            os.chdir(r"C:\Users\Shri Krishan\Downloads")
            os.mkdir("Executable files")
            break
        elif item.endswith('.zip'):
            os.chdir(r"C:\Users\Shri Krishan\Downloads")
            os.mkdir("Zip files")
            break

#function to move file
def move_file(source_path, des_path):
    shutil.move(source_path,des_path)



if __name__ == "__main__":

    #source path 
    source_path = r"C:\Users\Shri Krishan\Downloads"

    #list all the file in that folder 
    dir = os.listdir(r"C:\Users\Shri Krishan\Downloads")
    
    #run folder create function to create Executable folder
    folder_create(source_path)

    for item in dir:
        if item.endswith('.png') or item.endswith('.jpeg') or item.endswith('.jpg') or item.endswith('.gif') or item.endswith('.raw'):
            temp = item
            #source path 
            source_path  = r"C:\Users\Shri Krishan\Downloads"  + "\\" +  temp 
            #destination path 
            des_path  = r"C:\Users\Shri Krishan\Pictures"
            #move the file to destination folder
            try:
                move_file(source_path,des_path)
            except:
                print("file already exit")

            
        
        elif item.endswith('.mp4') or item.endswith('.mkv') or item.endswith('.mov') or item.endswith('.avi') or item.endswith('.wmv'):
            temp = item
            #source path 
            source_path  = r"C:\Users\Shri Krishan\Downloads"  + "\\" +  temp
            #destination path 
            des_path  = r"C:\Users\Shri Krishan\Videos"
            #move file to the destination folder
            try:
                move_file(source_path,des_path)
            except:
                print("file already exit")
    
        elif item.endswith('.mp3') or item.endswith('.wav') or item.endswith('.m4a') or item.endswith('.flac') or item.endswith('.wma') or item.endswith('.aac'):
            temp = item
            #source path 
            source_path  = r"C:\Users\Shri Krishan\Downloads"  + "\\" +  temp
            #destination path 
            des_path  = r"C:\Users\Shri Krishan\Music"
            #move file to the destination folder
            try:
                move_file(source_path,des_path)
            except:
                print("file already exit")

        elif item.endswith('.txt') or item.endswith('.doc') or item.endswith('.docx') or item.endswith('.pdf') or item.endswith('.ppt') or item.endswith('.pptx') or item.endswith('.xls') or item.endswith('.xlsx') or item.endswith('.odt'):
            temp = item
            #source path 
            source_path  = r"C:\Users\Shri Krishan\Downloads"  + "\\" +  temp 
            #destination path 
            des_path  = r"C:\Users\Shri Krishan\Documents"
            #move file to the destination folder
            try:
                move_file(source_path,des_path)
            except:
                print("file already exit")

        elif item.endswith('.exe') or item.endswith('.msi'):
            temp = item
            #source path 
            source_path  = r"C:\Users\Shri Krishan\Downloads"  + "\\" +  temp
            #destination path 
            des_path  = r"C:\Users\Shri Krishan\Downloads\Executable files"
            try:
                move_file(source_path,des_path)
            except:
                print("file already exit")

        elif item.endswith('.zip'):
            temp = item
            #source path 
            source_path  = r"C:\Users\Shri Krishan\Downloads"  + "\\" +  temp
            #destination path 
            des_path  = r"C:\Users\Shri Krishan\Downloads\Zip files"
            try:
                move_file(source_path,des_path)
            except:
                print("file already exit")
    


        

