
def main():

    def countCharacter(x):
        count = {}
        for character in x:
            character = character.lower()
            if character.isalpha():
                if character in count:
                    count[character] += 1
                else:
                    count[character] = 1
            
        return count

    def countWord(f):
        return len(f.split())
    
    def sortOn(dict):
        return dict["num"]
    
    def sortList(list):
        list.sort(reverse = True, key=sortOn)
        return list

    
    frankenstein = "books/frankenstein.txt"

    def writeReport(book):
        with open(book) as f:
            openBook = f.read()
        print("--- Begin report of ", book ," ---")
        bookChar = countCharacter(openBook)
        dictList = []
        for k, v in bookChar.items():
          tempDict = {"char": k, "num" : v}
          dictList.append(tempDict)
        sortedList = sortList(dictList)    
        print(countWord(openBook)," words were found in the document")
        for item in sortedList:
            print("the ",item['char'], " was found ", item["num"], " times")
        print("--- End report ---")
        
        

    
   # with open(frankenstein) as f:
   #     file_contents = f.read()
       # print(file_contents)
       # countWord(file_contents)
       # countCharacter(file_contents)
       # writeReport(file_contents)
    writeReport(frankenstein)
        
        
    




main()