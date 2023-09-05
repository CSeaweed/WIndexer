from pathlib import WindowsPath, Path


def mergeContents(contents: dict, newContents: dict) -> dict:
    for newObject in newContents:
        if newObject not in contents:
            contents[newObject] = []
        contents[newObject].extend(newContents[newObject])
    return contents

def idenfity_fsObjet(fsObject: WindowsPath):
    pass

def recursiveIndex(root: str) -> dict:
    root: WindowsPath = Path(root)
    fsContents: dict = {}

    # Too deep please fix < 5 indents
    for fsObject in root.iterdir():
        fName: str = str(fsObject.name).lower()
        try:
            if fsObject.is_file():
                if fName not in fsContents:
                    fsContents[fName] = []
                fsContents[fName].append(str(fsObject))

            if fsObject.is_dir():
                newContents: dict = recursiveIndex(str(fsObject))
                fsContents: dict = mergeContents(fsContents, newContents)
        except Exception as err:
            print(f"{err}")
    return fsContents

def refreshIndex(root: str) -> dict:
    return recursiveIndex(root)