import sqlite3
from compressions import compress, decompress


def connect(dbName: str) -> sqlite3.Cursor:
    connection = sqlite3.connect(dbName)
    return connection.cursor()

def searchIndex(searchTerm: str, dbName: str = "index.db") -> list:
    db: sqlite3.Cursor = connect(dbName)

    # This is horrible pleas# This is hrorrible please fix
    rawResults: list = db.execute(f"SELECT FS.paths FROM Filesystem AS FS WHERE FS.filename = '{searchTerm}'").fetchone()
    results: list = decompress(rawResults[0]).split("<new>")

    return results

def makeIndex(filesystem: dict, dbName: str = "index.db"):
    with open(dbName, mode="w+"): pass
    db: sqlite3.Cursor = connect(dbName)

    db.execute("CREATE TABLE Filesystem (id INTEGER PRIMARY KEY, filename TEXT, paths TEXT);")

    db.execute("Begin;")
    for fsObject in filesystem:
        try:
            paths: str = "<new>".join(filesystem[fsObject])
            paths: bytes = compress(paths)
            statement: str = "INSERT inTO Filesystem (filename, paths) VALUES (?, ?)"
            db.execute(statement, (fsObject, paths))
        except UnicodeEncodeError as err:
            print(err)
    db.execute("Commit;")

