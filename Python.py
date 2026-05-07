
# File READing CODE 

F = open("Practice.txt")
#print(F.read())
#print(F.read(4))   #read only 4 words - ABCD 

#print(F.readline())

#for line in F:  
#    print(line)   #prints each line with Space between the lines

#F.close()

#File Handling 

try:
   F = open("atul.txt")
   print(F.read())
except:
    print("this file is not present")
finally:
    F.close()


#Appedn - creaete the file if it does not exist 

F = open("Practice.txt" , "a")
F.write("\nPlease also check the brand netting")
F.close()


F = open("Practice.txt")
print(F.read())
F.close()