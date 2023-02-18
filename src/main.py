#Configparser Module
import configparser
import os  # To do changes in system with less commands
import platform  # To detect the current Platform
import time  # To do Stops in script

#A little bit of Color:
import colorama

import conf

configuration = configparser.ConfigParser()

#Cleaning Used Console:
if platform.system() == "Windows":
    os.system("cls")
else:
    os.system("clear")


#Important Variables
root_folder_name = None
child_folder_q = 0

inp_fold_name = None

child_folder_names = []

def tool():

    #Welcoming
    print("Welcome to the Practica 7.07 - Python Automation")
    print("================================================")
    print('\n')

    #Step 1: Taking root_folder name
    root_folder_name = input("Insert the *ROOT* Folder Name: ")

    #Extra: Adding some data to .ini file! (This is just for some scripts as clear to work!)
    conf.create_starter_config() #Config file creator.
    conf.config['DEFAULTS']['root_folder_name'] = root_folder_name # Changing the `root_folder_name` config value from None to root_folder_name variable value.
    conf.config['DEFAULTS']['machine_os'] = platform.system() # Appending the actual OS the machine is Using
    conf.config['DEFAULTS']['machine_username'] = os.getlogin() # Appending the actual User using the Machine
    with open('config.ini', 'w') as configfile: #Writing the changed values inside the .ini file.
        conf.config.write(configfile) 
        configfile.close() #Closing the file after finishing the writing.

    #Step 2: Take the quantity of child_folders to create:
    child_folder_q = input("Quantity of Child Folders to Create: ")

    #Step 3: For Loop to cycle for creating the folders (Taking the names and appending to list):
    for x in range(int(child_folder_q)):
        inp_fold_name = input("Insert the Child Folder " + str(x) + " Name: ")
        child_folder_names.append(inp_fold_name)

    #print(child_folder_names) //debuggin: Show list to see if appended correctly.

    #Step 4: Array Separation and Folder Creation:
    def create():
        print("Creating Root Dir: <==========> 100%")
        os.mkdir("./" + root_folder_name)
        time.sleep(0.5)
        print('\n')
        print("Creating Subdirs:")
        for x in child_folder_names:
            print(x + '\n') #//Debuggin: Show if values sepparated correcly.
            os.mkdir(os.getcwd() + "/" + root_folder_name + "/" + x)
            
    create()

    #Step 5: Ask if we finished creating directories or we want to generate more subdirectories:
    option_sub = None
    sub_folder_q = 0
    sub_folder_names = []
    sub_folder_inp = None
    
    #Function to create the assigned files in the assigned directories. (READ THE DOCS!!)
    def create_files():
        #Files on a JSON type variable
        march = ['marzo.ic', 'marzo.iv']
        april = ['abril.ic', 'abril.iv']
        proyects = ['1.p', '2.p', '3.p', '4.p', '5.p']

        #Marzo:
        for m in march:
            print("Creating files " + m + " in " + os.getcwd() + "/Informes/Marzo")
            if platform.system() == "Windows":
                os.system('type nul > ./' + root_folder_name + "/Informes/Marzo/" + march[0])
                os.system('type nul > ./' + root_folder_name + "/Informes/Marzo/" + march[1])
                time.sleep(3)
                break
            elif platform.system() == "Linux":
                os.system('touch ' + os.getcwd() + "/" + root_folder_name + "/Informes/Marzo/" + m)
                time.sleep(3)
                break
            break
        time.sleep(1)
        #Abril
        for a in april:
            print("Creating files " + a + " in " + os.getcwd() + "/Informes/Abril")
            if platform.system() == "Windows":
                os.system('type nul > ' + './' + root_folder_name + "\\Informes\\Abril/" + a)
                time.sleep(3)
                break
            elif platform.system() == "Linux":
                os.system('touch ' + os.getcwd() + "/" + root_folder_name + "/Informes/Abril/" + a)
                time.sleep(3)
                break
            break
        time.sleep(1)
        #Proyectos
        for p in proyects:
            print("Creating files " + p + " in " + os.getcwd() + "/Proyectos/")
            if platform.system() == "Windows":
                os.system('type nul > ' + './' + root_folder_name + "\\Proyectos/" + p)
                time.sleep(3)
                break
            elif platform.system() == "Linux":
                os.system('touch ' + os.getcwd() + "/" + root_folder_name + "/Proyectos" + p)
                time.sleep(3)
                break
            break

    #Function to run if opt is y:
    def c_subdir():
        
        #We are going to repeat the process but this time creating the subdirectories:
        sub_folder_q = input("Insert the quantity of SubDirectories to create: ")

        #Loop from Variable Value to determine the Folder Names to be created.
        for y in range(int(sub_folder_q)):
            sub_folder_inp = input("Insert the Subdirectory " + str(y) + " Name: ")
            sub_folder_names.append(sub_folder_inp) #With this we append the Val. of de Var. to the list.

        #Now we take all the folders on the root directory:
        rdir = os.listdir(os.getcwd() + "/" + root_folder_name + "/")
        
        #Step 6: Ask for the Directory Name where we create the subdirectries:
        
        for u in rdir: #We loop thru all the values in rdir (DIRECTORY)
            print("[" + str(rdir.index(u)) + "]" + u) #And we show the Index Number of Val in Array

        sub_dir_name = input("Insert the number of the Directory where you wan't to create this subdirs: ")
        
        #We are trying to use the List index to tell the Script were to create the subdirectory's
        # for o in rdir:
        #     if sub_dir_name == range(int(rdir.index(o))):
        #         print("Directory is avaliable")

        #Step 7: Take the Sub_Dir_Name and create a conditional 
        for o in rdir:

            index_num = rdir.index(o)

            if sub_dir_name in str(index_num):
                for k in sub_folder_names:
                    print('\n')
                    print("Creating Subdirectories: " + k + "...")
                    time.sleep(2)
                    os.mkdir(path=os.getcwd() + "/" + root_folder_name + "/" + rdir[int(sub_dir_name)] + "/marzo")
                    os.mkdir(path=os.getcwd() + "/" + root_folder_name + "/" + rdir[int(sub_dir_name)] + "/abril")
                    if os.path.exists(os.getcwd() + "/" + root_folder_name + "/Informes/" + k):
                        create_files()
                        break
            else:
                print("There was an Error while doing this!!")
                

    #Now we ask if we want to create subdirs
    option_sub = input("You wan't to create Subdirectories? [y/n]: ")

    if option_sub == "y":
        c_subdir()
    elif option_sub == "n":
        exit()


#Execute the script if condition is true
if __name__ == "__main__":
    tool()
