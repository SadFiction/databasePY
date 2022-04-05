class Main():
    import Read
    import Write
    import Other
    import sys
    import Help

    def __init__(self):
        self.Other.create().checkBAT()
        self.Write.write().createJson()

        self.fileType = None
        self.dir = None
        self.entry = None
        self.fileName = None
        self.mode = None
        self.description = None
        self.change = None
        self.path = None

        self.args = self.sys.argv
        del self.args[0]

        for i in self.args:
            if "-ft:" in i.lower():
                self.fileType = i.lower().replace("-ft:", "")
            elif "-m:" in i.lower():
                self.mode = i.lower().replace("-m:", "")
            elif "-dir:" in i:
                self.dir = i.replace("-dir:", "")
            elif "-en:" in i :
                self.entry = i.replace("-en:", "")
            elif "-entry:" in i:
                self.entry = i.replace("-entry:", "")
            elif "-fn:" in i:
                self.fileName = i.replace("-fn:", "")
            elif "-d:" in i:
                self.description = i.replace("-d:", "")
            elif "-c:" in i:
                self.change = i.replace("-c:", "")
            elif "-p:" in i:
                self.path = i.replace("-p:", "")

    def main(self):
        """Read Section"""

        # checks to see if a primary arg has been specified;
        # If not it wil ask the user if they need help
        if len(self.args) == 0:
            if input("\nIf you need self.Help enter '?' else press enter: ") == "?":
                self.Help.Help().simple()

            else:
                return

        # "?" or "help" (primary arg option)
        elif self.args[0].lower() == "help" or self.args[0] == "?":
            if len(self.args) < 2:
                self.Help.Help().simple()

            elif self.args[1].lower() == "ls":
                self.Help.Help().ls()

            elif self.args[1].lower() == "goto":
                self.Help.Help().goto()

            elif self.args[1].lower() == "view":
                self.Help.Help().view()

            elif self.args[1].lower() == "mkdir":
                self.Help.Help().mkdir()
            
            elif self.args[1].lower() == "mken":
                self.Help.Help().mken()
           
            elif self.args[1].lower() == "deldir":
                self.Help.Help().deldir()
           
            elif self.args[1].lower() == "delen":
                self.Help.Help().delen()
           
            elif self.args[1].lower() == "moddir":
                self.Help.Help().modir()
           
            elif self.args[1].lower() == "moden":
                self.Help.Help().moden()
           
            elif self.args[1].lower() == "writem":
                self.Help.Help().writem()
           
            elif self.args[1].lower() == "addi":
                self.Help.Help().addi()
           
            elif self.args[1].lower() == "rmi":
                self.Help.Help().rmi()
            
            elif self.args[1].lower() == "backup":
                self.Help.Help().backup()            
            else:
                print("### Command you looking for is invalid ###")

        # Read type arg
        # "ls" (primary arg option)
        elif self.args[0].lower() == "ls":
            if len(self.args) < 2:
                self.Help.Help().defineType()

            # "dir" (secondary arg option)
            elif self.args[1].lower() == "dir":
                self.Read.read().listDir()

            # "entry" (secondary arg option)
            elif self.args[1].lower() == "entry":
                if self.dir is None:
                    self.Help.Help().specifyDir()

                else:
                    if self.Read.read().listEntry(self.dir) == 1:
                        self.Help.Help().smthWrong()

            # "entrycon" (secondary arg option)
            elif self.args[1].lower() == "entrycon":
                if self.entry is None or self.dir is None:
                    self.Help.Help().specifyDir()
                    self.Help.Help().specifyEntry()

                else:
                    if self.Read.read().listEntryContents(name=self.entry, directory=self.dir) == 1:
                        self.Help.Help().smthWrong()

        # "goto" (primary arg option)
        elif self.args[0].lower() == "goto":
            if len(self.args) < 2:
                self.Help.Help().defineType()

            # "dir" (secondary arg option)
            elif self.args[1].lower() == "dir":
                if self.dir is None:
                    self.Help.Help().specifyDir()

                else:
                    if self.Read.read().openDirLocation(self.dir) == 1:
                        self.Help.Help().smthWrong()

            # "entry" (secondary arg option)
            elif self.args[1].lower() == "entry":
                if self.dir is None or self.entry is None:
                    self.Help.Help().specifyDir()
                    self.Help.Help().specifyEntry()

                else:
                    if self.Read.read().openEntryLocation(name=self.entry, directory=self.dir) == 1:
                        self.Help.Help().smthWrong()

        # "view" (primary arg option)
        elif self.args[0].lower() == "view":
            if len(self.args) < 2:
                self.Help.Help().defineType()

            # "main" (secondary arg option)
            elif self.args[1].lower() == "main":
                extra = "in"
                if self.entry is None or self.dir is None:
                    self.Help.Help().specifyDir()
                    self.Help.Help().specifyEntry()

                else:
                    if self.mode is not None:
                        extra = self.mode

                    if self.Read.read().viewMain(directory=self.dir, name=self.entry, option=extra) == 1:
                        self.Help.Help().smthWrong()

            # "item" (secondary arg option)
            elif self.args[1].lower() == "item":
                if self.entry is None or self.dir is None or self.fileName is None or self.fileType:
                    print(
                        "### Syntax invalid: Specify Dir, Entry, name (of file), (file)type  ### ")

                else:
                    if self.Read.read().viewItem(directory=self.dir, entry=self.entry, name=self.fileName, type=self.fileTypeda) == 1:
                        self.Help.Help().smthWrong()

        # Write type arg
        # "mkdir" (primary arg option)
        elif self.args[0].lower() == "mkdir":
            if self.dir is None:
                self.Help.Help().specifyDir()

            else:
                if self.Write.write().createDir(name=self.dir, description=self.description) == 1:
                    self.Help.Help().smthWrong()

        # "mken" (primary arg option)
        elif self.args[0].lower() == "mken":
            if self.dir is None or self.entry is None:
                self.Help.Help().specifyDir()
                self.Help.Help().specifyEntry()

            else:
                if self.Write.write().createEntry(name=self.entry, directory=self.dir, description=self.description) == 1:
                    self.Help.Help().smthWrong()

        # "deldir" (primary arg option)
        elif self.args[0].lower() == "deldir":
            if self.dir is None:
                self.Help.Help().specifyDir()

            else:
                if self.Write.write().deleteDir(self.dir) == 1:
                    print("### Sorry something went wrong ###")

        # "delen" (primary arg option)
        elif self.args[0].lower() == "delen":
            if self.dir is None or self.entry is None:
                self.Help.Help().specifyDir()
                self.Help.Help().specifyEntry()

            else:
                if self.Write.write().deleteEntry(name=self.entry, directory=self.dir) == 1:
                    self.Help.Help().smthWrong()

        # "moddir" (primary arg option)
        elif self.args[0].lower() == "moddir":
            if self.dir is None or self.mode is None or self.change is None:
                print("### Syntax invalid: please specify dir, mode and change")

            else:
                if self.Write.write().modifyDir(name=self.dir, option=self.mode, change=self.change) == 1:
                    self.Help.Help().smthWrong()

        # "moden" (primary arg option)
        elif self.args[0].lower() == "moden":
            if self.dir is None or self.entry is None or self.mode is None or self.change is None:
                print("Syntax invalid: Please specify dir, entry, mode and change")

            else:
                if self.Write.write().modifyEntry(name=self.entry, directory=self.dir, option=self.mode, change=self.change) == 1:
                    self.Help.Help().smthWrong()

        # "writem" (primary arg option)
        elif self.args[0].lower() == "writem":

            if self.entry is None or self.dir is None :
                print("### Syntax invalid: Please specify dir, entry, mode and change")
            else:
                extra = "a"
                if self.mode is not None:
                    extra = self.mode
                if extra == "a" and self.change is None:
                    self.change = input("Enter text (append mode) >>> ")
                if self.Write.write().writeMain(name=self.entry, directory=self.dir, write=self.change, mode=extra) == 1:
                    self.Help.Help().smthWrong()

        # "addi" (primary arg option)
        elif self.args[0].lower() == "addi":
            if self.entry is None or self.dir is None or self.fileType is None or self.path is None:
                print(
                    "### Syntax invalid: please specify dir, entry, filename, filepath and filetype ###")
            else:
                if self.Write.write().addItem(name=self.fileName, path=self.path, entry=self.entry, directory=self.dir, type=self.fileType) == 1:
                    self.Help.Help().smthWrong()

        # "rmi" (primary arg option)
        elif self.args[0].lower() == "rmi":
            if self.fileName is None or self.entry is None or self.dir is None or type:
                print(
                    "### Syntax invalid: Please specifyh dir, entry, filename and filetype")
            else:
                if self.Write.write().removeItem(name=self.fileName, entry=self.entry, directory=self.dir, type=self.fileType) == 1:
                    self.Help.Help().smthWrong()

        #other type arg
        #"backup"
        elif self.args[0].lower() == "backup":
            if self.path is None:
                print("### Syntax invalid: please specify path")
            else:
                if self.Other.Copy().database(self.path) == 1:
                    print("### Path provided is not valid")
        else:
            print("### Thats not a valid command ###")



#entry point
Main().main()