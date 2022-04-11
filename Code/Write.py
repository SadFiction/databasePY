from unittest.mock import NonCallableMagicMock


class write:
    try:
        import simplejson as json
    except(ModuleNotFoundError):
        import json
    import os

    def __init__(self):
        self.jsonLocation = f"C:/Users/{self.os.getlogin()}/AppData/Local/databasePY/database.json"
        self.dataLocation = f"C:/Users/{self.os.getlogin()}/AppData/Local/databasePY/"
        self.disallowed = ["<", ">", ":", "\"", "/", "|", "?", "*"]

    def createJson(self):
        
        try:
            if not self.os.path.exists(self.dataLocation):
                self.os.system(
                    f"cd \"C:/Users/{self.os.getlogin()}/AppData/Local/\" & mkdir databasePY")

            with open(self.jsonLocation, "x") as f:
                temp = {"dir": {}}
                self.json.dump(temp, f, indent=3)
                f.close()

        except(Exception):
            return

    def createDir(self, name=None, description=None):
        if name is None:
            return

        else:
            for i in self.disallowed:
                if i in name:
                    name = name.replace(i, "")

            try:
                with open(self.jsonLocation, "r") as f:
                    temp = self.json.load(f)

                    data = {"content": {},
                            "description": description}

                    temp["dir"][name] = data
                    f.close()

                self.__complete(temp)
                self.os.system(
                    f"cd \"{self.dataLocation}\" & mkdir  \"{name}\"")

            except(Exception):
                return 1

    def createEntry(self, name=None, directory=None, description=None):
        if name is None or directory is None:
            return

        else:
            for i in self.disallowed:
                if i in name:
                    name = name.replace(i, "")

            try:
                with open(self.jsonLocation, "r") as f:
                    temp = self.json.load(f)

                    data = {"content": {
                        "main": "main.txt",
                        "images": {},
                        "otherFiles": {}
                    },
                        "description": description}

                    temp["dir"][directory]["content"][name] = data
                    f.close()

                self.__complete(temp)
                self.os.system(
                    f"cd \"{self.dataLocation}{directory}/\" & mkdir \"{name}\"")
                self.os.system(
                    f"cd \"{self.dataLocation}{directory}/{name}/\"  & mkdir images")
                self.os.system(
                    f"cd \"{self.dataLocation}{directory}/{name}/\"  & mkdir otherFiles")
                self.os.system(
                    f"cd \"{self.dataLocation}{directory}/{name}/\" & echo {name.capitalize()} > main.txt")

            except(Exception):
                return 1

    def deleteDir(self, name=None):
        if name is None:
            return

        else:
            try:
                with open(self.jsonLocation, "r") as f:
                    temp = self.json.load(f)

                    del temp["dir"][name]
                    f.close()

                self.__complete(temp)
                self.os.system(
                    f"cd \"{self.dataLocation}\" & rmdir /q /s \"{name}\"")

            except(Exception):
                return 1

    def deleteEntry(self, name=None, directory=None):
        if name is None or directory is None:
            return

        else:
            try:
                with open(self.jsonLocation, "r") as f:
                    temp = self.json.load(f)

                    del temp["dir"][directory]["content"][name]
                    f.close()
                self.__complete(temp)
                self.os.system(
                    f"cd \"{self.dataLocation}{directory}/\" & rmdir /q /s \"{name}\"")

            except(Exception):
                return 1

    def modifyDir(self, name=None, option=None, change=None):
        if name is None or option is None or change is None:
            return

        else:

            try:
                with open(self.jsonLocation, "r") as f:
                    temp = self.json.load(f)

                    if option.lower() == "content":
                        temp["dir"][name]["content"] = change

                    elif option.lower() == "description":
                        temp["dir"][name]["description"] = change

                    elif option.lower() == "name":
                        data = {"content": temp["dir"][name]["content"],
                                "description": temp["dir"][name]["description"]}
                        temp["dir"][change] = data
                        del temp["dir"][name]

                        self.os.system(
                            f"cd \"{self.dataLocation}\" & rename \"{name}\" \"{change}\"")

                    else:
                        return
                    f.close()

                self.__complete(temp)

            except(Exception):
                return 1

    def modifyEntry(self, name=None, directory=None, option=None, change=None):
        if name is None or option is None or change is None or directory is None:
            return

        else:
            try:

                with open(self.jsonLocation, "r") as f:
                    temp = self.json.load(f)

                    if option.lower() == "content":
                        temp["dir"][directory]["content"][name]["content"] = change

                    elif option.lower() == "description":
                        temp["dir"][directory]["content"][name]["description"] = change

                    elif option.lower() == "name":
                        data = {"content": temp["dir"][directory]["content"][name]["content"],
                                "description": temp["dir"][directory]["content"][name]["description"]}
                        temp["dir"][directory]["content"][name] = data
                        del temp["dir"][directory]["content"][change]
                        self.os.system(
                            f"cd \"{self.dataLocation}{directory}/\" & rename \"{name}\" \"{change}\"")

                    else:
                        return
                    f.close()

                self.__complete(temp)

            except(Exception):
                return 1

    def writeMain(self, name=None, directory=None, write=None, mode="a"):
        if name is None and directory is None:
            return

        else:
            try:
                if mode.lower() == "a" or mode.lower() == "a":
                    with open(f"{self.dataLocation}{directory}/{name}/main.txt", "a") as f:
                        f.write(write)
                        f.close()

                elif mode.lower() == "np" or mode.lower() == "n":
                    location = self.dataLocation.replace('/', '\\')
                    self.os.system(
                        f"notepad \"{location}{directory}\\{name}\\main.txt\"")

            except(Exception):
                return 1

    def addItem(self, name=None, path=None, entry=None, directory=None, typ=None):
        if path is None or entry is None or directory is None or typ is None:
            return

        else:
            if "," in path:
                    pathItems = path.split(",")
                    nameItems = None
                    try:
                        if "," in name:
                            nameItems = name.split(",")#
                    except(Exception):
                        pass
                    
                    for i in range(len(pathItems)):
                        if type(nameItems) == list:
                            try:
                                tempName = (nameItems[i]).strip()
                            except(Exception):
                                tempName = None
                        print(tempName)
                        self.addItem(name=tempName, path=pathItems[i].strip(), entry=entry, directory=directory, typ=typ)

            elif self.os.path.exists(path):
               
                try:
                    
                    rname, exten = self.os.path.splitext(
                            self.os.path.basename(path))
                    if name is None:
                        name = rname
                    
                    if typ.lower() == "image" or typ.lower() == "i":
                        path = path.replace                                                    ("/", "\\")
                        location = self.dataLocation.replace("/", "\\")
                        self.os.system(
                            f" copy \"{path}\" \"{location}{directory}\\{entry}\\images\"")
                        with open(self.jsonLocation, "r") as f:
                            temp = self.json.load(f)
                            data = {"name": rname + exten,
                                    "size": self.os.path.getsize(path)}
                            temp["dir"][directory]["content"][entry]["content"]["images"][name] = data
                            self.__complete(temp=temp)
                            f.close()

                    elif typ.lower() == "other" or typ.lower() == "o":
                        path = path.replace("/", "\\")
                        location = self.dataLocation.replace("/", "\\")
                        self.os.system(
                            f"copy \"{path}\" \"{location}{directory}\\{entry}\\otherFiles\"")
                        with open(self.jsonLocation, "r") as f:
                            temp = self.json.load(f)
                            data = {"name": rname + exten,
                                    "size": self.os.path.getsize(path)}
                            temp["dir"][directory]["content"][entry]["content"]["otherFiles"][name] = data
                            self.__complete(temp=temp)
                            f.close()

                except(Exception):
                    return 1

            else:
                return 1

    def removeItem(self, name=None, entry=None, directory=None, typ=None):
        if name is None or entry is None or directory is None or typ is None:
            return

        else:
            if "," in name:
                    nameItems = name.split(",")        
                    for i in range(len(nameItems)):
                        self.removeItem(name=nameItems[i].strip(),entry=entry, directory=directory, typ=typ )
                        
            else:
                try:
                    location = self.dataLocation.replace("/", "\\")
                    if typ.lower() == "image" or typ.lower() == "i":
                        with open(self.jsonLocation, "r") as f:
                            temp = self.json.load(f)
                            rname = temp["dir"][directory]["content"][entry]["content"]["images"][name]["name"]
                            self.os.system(
                                f"del \"{location}{directory}\\{entry}\\images\\{rname}\"")
                            del temp["dir"][directory]["content"][entry]["content"]["images"][name]
                            self.__complete(temp=temp)

                    elif typ.lower() == "other" or typ.lower() == "o":
                        with open(self.jsonLocation, "r") as f:
                            temp = self.json.load(f)
                            rname = temp["dir"][directory]["content"][entry]["content"]["otherFiles"][name]["name"]
                            self.os.system(
                                f"del \"{location}{directory}\\{entry}\\otherFiles\\{rname}\"")
                            del temp["dir"][directory]["content"][entry]["content"]["otherFiles"][name]
                            self.__complete(temp=temp)

                except(Exception):
                    return 1

    def __complete(self, temp):
        with open(self.jsonLocation, "w") as f:
            self.json.dump(temp, f, indent=3)
            f.close()


if __name__ == "__main__":
    while True:
        exec("write()." + input("--->"))
