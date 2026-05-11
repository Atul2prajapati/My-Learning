import os

# File READing CODE 

F = open("Practice.txt")
#print(F.read())
#print(F.read(4))   #read only 4 words - ABCD 

#print(F.readline())

#for line in F:  
#    print(line)   #prints each line with Space between the lines

#F.close()

#File Handling 

#try:
#   F = open("atul.txt")
#   print(F.read())
#except:
#    print("this file is not present")
#finally:
#    F.close()


#Appedn - creaete the file if it does not exist 

#F = open("Practice.txt" , "a")
#F.write("\nPlease also check the brand netting")
#F.close()


#F = open("Practice.txt")
#print(F.read())
#F.close()

## Write (Overwrite) - To change the content of the whole txt file.

#F = open("NamingSheet.txt","r")
#print(F.read())
#F.close()

#F= open("NamingSheet.txt","w")
#F.write("we are deleting all contetn in this")
#F.close()

#F = open("NamingSheet.txt","r")
#print(F.read())
#F.close()

## Two ways to create a new file

#opens a file for writing , creates the file if it does not exist

f = open("FileCreated.txt","w")
f.close()

#creating the specific file but returning error if the file already exists
#we need to "import os module" for this

if os.path.exists("FileCreated.txt"):
    print("File already exists")
else:    
    f = open("FileCreated.txt","x")
    f.close()   

# Deleting a file

if os.path.exists("FileCreated.txt"):
    os.remove("FileCreated.txt")
else:      
    print("File does not exist")

# Creating the content of Another file

with open("Practice.txt") as F:
    content = F.read()

with open("Namingsheet.txt","w") as F:
    F.write(content)