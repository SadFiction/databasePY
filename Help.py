class Help:
    def simple(self):

        print("\nHere's the list of commands: \n")

        print("Read type commands:\n")
        print("\tls : list the items of the specified targets e.g a dir an entry or the contents of an entry ")
        print("\tgoto : goes to the location  of the specified target e.g dir or entry")
        print("\tview : displays the contents of a file")
        
        print("\nWrite type commands:\n")
        print("\tmkdir <options> : creates a directory for entries to be created ")
        print("\tmken <options> : creates a entry in the specified directory")
        print("\tdeldir <options> : deletes specified directory")
        print("\tdelen <options> : deletes specified entry in the specified directory")
        print("\tmoddir <options> : allows user to modify certain attributes of a dir")
        print("\tmoden <options> : allows user to modify certain attributes of an entry")
        print("\twritem <options> : allow user to write to main.txt of an entry through [2] modes; append and notepad")
        print("\taddi <options> : adds item to the entry specified by copying the item in path provided to entry")
        print("\trmi <options> : removes an item from an entry")

        print("\Other type commands:\n")

        print("\tbackup <options> : copies all of the database into the specified path ")
        print("\nFor more info type help(or ?) <primary command>\n")

    def ls(self):

        print("ls <secondary arg> : list the items of the specified target")
        print("Secondary arg: ")
        print("\tdir : lists all dir")
        print("\t\toptions: none")
        print("\tentry : lists all entries in dir specified ")
        print("\t\toptions: -dir:<mendatory>")
        print("\tentrycon : lists all of the contents of the entry specified")
        print("\t\toptions: -dir:<mendatory> -en(entry):<mendatory>")

    def goto(self):

        print("goto <secondary arg> : goes to the location of the target specified in the explorer")
        print("Secondary arg:")
        print("\tdir : opens the directory specified in the explorer")
        print("\t\toptions: -dir:<mendatory> ")
        print("\tentry : opens the entry (which is inside a directory) in the exploer")
        print("\t\toptions : -dir:<mendatory> -en(entry):<mendatory>")

    def view(self):
        print("view <secondary arg> : displays file in some factor")
        print("Secondary option:")
        print("\tmain : allow user to open the main file(a txt file with main info) in console or notepad ")
        print("\t\toptions: -dir:<mendatory> -en(entry):<mendatory> -m(mode)<optional; options = in (integrated) , np (notepad)> ")
        print("\titem : allows users to open file in an entry to view in the default manner the system usually does")
        print("\t\toptions: -dir:<mendatory> -en(entry):<mendatory> -fn(file name)<mendatory> -ft(file type)<mendatory;  option = i (image) , o (other)> ")

    def mkdir(self):
        print("mkdir <options> : creates a directory for entries to be created ")
        print("\toptions: -dir:<mendatory>(name for dir) ")

    def mken(self):
        print("mken <options> : creates a entry in the specified directory")
        print("\toptiions: -dir:<mendatory>(creation dir) -entry:<mendatory>(name of entry) ")

    def deldir(self):
        print("deldir <options> : deletes specified directory")
        print("\toptions: -dir:<mendatory>(target dir)")
    
    def delen(self):
        print("delen <options> : deletes specified entry in the specified directory")
        print("\toptions: -dir:<mendatory>(dir) -en(try):<mendatory>(target entry)")
    
    def modir(self):
        print("moddir <options> : allows user to modify certain attributes of a dir")
        print("\toptions: -dir:<mendatory>(target dir) -m:(what aspect to be modified)<mendatory; options: content , description, name> -c:(what it should be changed to)<mendatory>")
    
    def moden(self):
        print("moden <options> : allows user to modify certain attributes of an entry")
        print("\toptions: -dir:<mendatory> -en:<mendatory>(target entry)  -m:(what aspect to be modified)<mendatory; options: content , description, name> -c:(what it should be changed to)<mendatory>")

    def writem(self):
        print("writem <options> : allow user to write to main.txt of an entry through [2] modes; append and notepad")
        print("\toptions: -dir:<mendatory> -en(try):<mendatory> -c(hange):<optional(technicaly, user will still be prompted to enter text)>(text to be writen)  -m(ode):<optional; options = a (append) and np (notepad)")

    def addi(self):
        print("addi <options> : adds item to the entry specified by copying the item in path provided to entry")
        print("\toptions: -p:<mendatory(path of file) -dir:<mendatory> -en:<mendatory> -fn(filename)<optional; one will be optained from path received> -ft:<mendatory; options= image/i and other/o>(file type)>")

    def rmi(self):
        print("rmi <options> : removes an item from an entry")
        print("\toptions: -dir:<mendatory> -en:<mendatory> -fn:<mendatory> -ft:<mendatory; options= image/i and other/o>(file type)")
   
    def backup(self):
        print("backup <options> : copies all of the database into the specified path ")
        print("\toptions: -p(ath):<mendatory> ")

    def defineType(self):
        print("### Syntax invalid: Specify type ### ")

    def specifyDir(self):
        print("### Syntax invalid: Specify dir ###")

    def specifyEntry(self):
        print("### Syntax invalid: Specify Entry ### ")

    def smthWrong(self):
        print("### Sorry something went wrong ###")
