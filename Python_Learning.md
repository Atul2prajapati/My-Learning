
# Learning Python for DE

## Basics

## File Handling in Python 

#RAWX = Read , Append  , Write , Create

1) # *READ

A) Read Command - { 
         
         F = open("Practice.txt")
         print(F.read())

}

B) F.close() - { 

    it is important to close the file which we are reading so if we  do any change it get save in it.
}


C) File Handling if the file does not exist - {

    try:
    f = open("atul.txt")
    print(f.read())
    except:
        print("this file is not present")
    finally:
        f.close()

}

2) # Append -- Create the File if does not exist

A) #Appedn  -- Each time we hit this code every time it will add the data in out txt file {

    F = open("Practice.txt" , "a")
    F.write("Please also check the brand netting")
    F.close()


    F = open("Practice.txt")
    print(F.read())
    F.close()

}