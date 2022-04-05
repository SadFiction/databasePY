class read:
    import os
    try:
        import simplejson as json
    except(ModuleNotFoundError):
        try:
            os.system("py -m pip install simplejson")
            import simplejson
        except(ModuleNotFoundError):
            import json

    try:
        import climage
    except(ModuleNotFoundError):
        os.system("py -m pip install climage")
    

    def __init__(self):
        self.jsonLocation = f"C:/Users/{self.os.getlogin()}/AppData/Local/databasePY/database.json"
        self.dataLocation = (
            f"C:/Users/{self.os.getlogin()}/AppData/Local/databasePY/").replace('/', '\\')

    def openDirLocation(self, name=None):
        if name is None:
            return

        else:
            if self.os.path.exists(f"{self.dataLocation}{name}\\ "):
                self.os.system(f"explorer \"{self.dataLocation}{name}\\\" ")

            else:
                return 1

    def openEntryLocation(self, name=None, directory=None):
        if name is None and directory is None:
            return

        else:
            if self.os.path.exists(f"{self.dataLocation}{directory}\\{name}\\"):
                self.os.system(
                    f"explorer \"{self.dataLocation}{directory}\\{name}\\\"")

            else:
                return 1

    def listDir(self):
        with open(self.jsonLocation, "r") as f:
            data = self.json.load(f)["dir"]
            for dir in data:
                print(
                    f"Name : {dir}; Description : {data[dir]['description']};")
            f.close()

    def listEntry(self, directory=None):
        if directory is None:
            return 1

        else:
            try:
                with open(self.jsonLocation, "r") as f:
                    data = self.json.load(f)["dir"][directory]["content"]

                    for entry in data:
                        print(
                            f"Name : {entry}; Description : {data[entry]['description']};")
                    f.close()

            except(Exception):
                return 1

    def listEntryContents(self, name=None, directory=None):
        if name is None or directory is None:
            return
        else:
            try:
                with open(self.jsonLocation, "r") as f:
                    data = self.json.load(
                        f)["dir"][directory]["content"][name]["content"]
                    print(f"MAIN > {data['main']}")

                    for item in data["images"]:
                        print(
                            f"Image > {item}; Size: {data['images'][item]['size']} Bytes")

                    for item in data["otherFiles"]:
                        print(
                            f"Files > {item}; Size: {data['otherFiles'][item]['size']} Bytes")

            except(Exception):
                return 1

    def viewMain(self, name=None, directory=None, option="in"):
        if name is None and directory is None:
            return

        else:

            if self.os.path.exists(f"{self.dataLocation}{directory}\\{name}\\main.txt"):
                if option == "in":
                    images = self.json.load(open(self.jsonLocation, "r"))[
                        "dir"][directory]["content"][name]["content"]["images"]
                    with open(f"{self.dataLocation}{directory}\\{name}\\main.txt") as f:
                        file = f.read()
                        file = (file.replace("#", "\t"))

                        for j in images:
                            if f"<<{images[j]['name']}>>" in file:
                                imagep = f'{self.dataLocation}{directory}\\{name}\\images\\{images[j]["name"]}'
                                image = self.climage.convert(filename=imagep)
                                file = file.replace(
                                    f"<<{images[j]['name']}>>", image)

                        print(file)

                elif option.lower() == "np" or option.lower() == "n":
                    self.os.system(
                        f"notepad {self.dataLocation}{directory}\\{name}\\main.txt")

            else:
                return 1

    def viewItem(self, name=None, entry=None, directory=None, type=None):
        if name is None or entry is None or directory is None or type is None:
            return

        else:
            try:
                with open(self.jsonLocation, "r") as f:
                    temp = self.json.load(f)

                    if type == "image" or type == "i":
                        fileName = temp["dir"][directory]["content"][entry]["content"]["images"][name]["name"]
                        self.os.system(
                            f"powershell -command \"{self.dataLocation}{directory}\\{entry}\\images\\{fileName}\"")

                    elif type == "other" or type == "o":
                        fileName = temp["dir"][directory]["content"][entry]["content"]["otherFiles"][name]["name"]
                        self.os.system(
                            f"powershell -command \"{self.dataLocation}{directory}\\{entry}\\otherFiles\\{fileName}\"")

            except(Exception):
                return 1


if __name__ == "__main__":
    while True:
        exec("read()." + input("--->"))
