class create:
    import os, ctypes, sys
    def __init__(self):
        self.location = self.sys.argv[0].replace("Other.py", "Database.py")
    def checkBAT(self):
        if self.os.path.exists(f"C:\Windows\database.bat"):
            return
        else:
            self.__createBAT()

    def __is_admin(self):
        try:
            return self.ctypes.windll.shell32.IsUserAnAdmin()
        except:
            return False

    def __createBAT(self):
        if self.__is_admin():
                
                with open(f"C:\Windows\database.bat", "x") as f:
                    f.write(f"@Echo off \npy {self.location} %*")
        else:
            # Re-run the program with admin rights
            self.ctypes.windll.shell32.ShellExecuteW(None, "runas", self.sys.executable, " ".join(self.sys.argv), None, 1)
        

class Copy:
    import os, sys
    def __init__(self):
        self.dataLocation = (f"C:/Users/{self.os.getlogin()}/AppData/Local/databasePY").replace('/', '\\')
    
    def database(self, destination):
        if self.os.path.exists(destination):
            self.os.system(f"Xcopy \"{self.dataLocation}\" \"{destination}\" /E /H /C /I")
        
        else:
            return 1




