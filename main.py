import os, shutil, time, sys

#python main.py C:/Users/Ondrej/Desktop/source/ C:/Users/Ondrej/Desktop/replica/ 5 C:/Users/Ondrej/Desktop/

source = sys.argv[1]
destination = sys.argv[2]
delay = sys.argv[3]
logpath = sys.argv[4]+"log.txt"

#print(logpath)
#print(source)
#print(destination)

###LOOP FOREVER###
try:
    while True:
        time.sleep(int(delay))
        ####SAVE INTO LIST WHAT FILES ARE IN DIRS####
        files = os.listdir(source)
        #print(files)
        files2 = os.listdir(destination)
        #print(files2)

        ##########FILE CREATED (log)########

        difference_result2 = []
        for item in files:
            if item not in files2:
                difference_result2.append(item)

        for item in difference_result2:
            print("file " + item + " created")
            f = open(logpath, "a")
            f.write("file " + item + " created\n")
            f.close()

        ###########FILE COPY (copy, log)##########
        for name in difference_result2:
            sourcefile = source + name
            destinationfile = destination + name

            shutil.copy2(sourcefile, destinationfile)
            print("File " + sourcefile + " copied to " + destination)
            f = open(logpath, "a")
            f.write("File " + sourcefile + " copied to " + destination + "\n")
            f.close()

            #print(sourcefile)
            #print(destinationfile)

        #########FILE REMOVE (remove, log)###########
        difference_result = []
        for item in files2:
            if item not in files:
                difference_result.append(item)

        for item in difference_result:
            print("File " + item + " removed")
            os.remove(f"C:/Users/Ondrej/Desktop/replica/{item}")
            f = open(logpath, "a")
            f.write("file " + item + " removed\n")
            f.close()

except KeyboardInterrupt:
        print('Program closed')

#recieved 5.5.2023 17:16
#finished 7.5.2023 0:18