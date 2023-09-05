from indexer import refreshIndex
from sqliteTools import makeIndex, searchIndex


def search(searchTerm: str) -> None:
    results: list = searchIndex(searchTerm)
    for result in results:
        print(result)
    if not results:
        print("No results! 'New' to refresh index")

def newIndex(root: str) -> None:
    contents: dict = refreshIndex(root)
    makeIndex(contents)

def main():
    root: str = "c:\\"
    
    command: str = input("Windexer > ").lower()
    if command.startswith("search "):
        search(command.replace("search ", "")) 
    if command == "new":
        newIndex(root)

if __name__ == "__main__":
    main()


