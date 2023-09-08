from pathlib import WindowsPath, Path


def mergeContents(contents: dict, newContents: dict) -> dict:
    for newObject in newContents:
        if newObject not in contents:
            contents[newObject] = []
        contents[newObject].extend(newContents[newObject])
    return contents

def recursiveIndex(root: str) -> dict:
    root: WindowsPath = Path(root)
    fsContents: dict = {}

    def handleObject(fsObject: WindowsPath, fsContents: dict):
        fName: str = str(fsObject.name)

        # Early return to avoid extra indent 
        if fsObject.is_dir():
            newContents: dict = recursiveIndex(str(fsObject))
            fsContents = mergeContents(fsContents, newContents)
            return fsContents

        if not fName in fsContents:
            fsContents[fName] = []
            fsContents[fName].append(str(fsObject)) 

        return fsContents

    for fsObject in root.iterdir():
        try:
            fsContents = handleObject(fsObject, fsContents)
        except Exception as err:
            print(f"{err:>256}", end="\r")

    return fsContents

def refreshIndex(root: str) -> dict:
    return recursiveIndex(root)