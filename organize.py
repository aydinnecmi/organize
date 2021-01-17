import os
import shutil

def organize():
    
    directory_path = os.getcwd()    
    files = os.listdir(directory_path)
        
    date = []
    for i in files:
        a= i.split('_')[0]
        date.append(a)
        
        
    dirPaths = list()  #Klasörlerin pathleri tutuluyor
    new = list(set(date)) #tekrar eden değerleri kaldırdık
    for i in new :
        fileName = i.startswith('2021') 
        
        if fileName == True :       
            dirName = (directory_path + '/' + i)
                    
            if i not in os.listdir(directory_path): #Eğer dizinde o klasör yoksa oluşturur
                os.mkdir(dirName)        
            dirPaths.append(dirName)          

    #dosya isimlerini aldık
    fileNames = [] #Dosya isimlerini tutuyor
    for i in files:
        a= i.split('_')[0]
        a = a.startswith('2021')
        b = os.path.isfile(directory_path + '\\' + i)
        if a == True and b == True:             
            fileNames.append(i)   

        
    file_paths = [] #Dosya pathleri tutuyor
    for i in files:
        if i.startswith("2021") and i.endswith('.jpg'):           
            a= os.path.join(directory_path, i) 
            file_paths.append(a)
        if i.startswith("2021") and i.endswith('.mp4'):
            b= os.path.join(directory_path, i)
            file_paths.append(b) 
    bare = []             
    extensions =('.jpg','.mp4')
    for j in file_paths:
        if j.endswith(extensions):        
            j =j.split("\\")[6] #C:\Users\userName\folderName\folderName2\folderName3 eğer klasör sayısı az ise 6 yerine 5,4 filan verilebilir  
            j =j.split("_")[0]
            bare.append(j)     

    try:
        for sıra, eleman in enumerate(bare, 0):        
            if eleman == eleman:
                index = "{}".format(sıra)
                index = int(index)
                dest = directory_path + "\\{}".format(eleman) + "\\" + fileNames[sıra]
                src = file_paths[index]
                shutil.move(src, dest) 
    except:
        pass
    
if __name__ == "__main__":

    organize()
        
        
                
                    
        
            

        







        
