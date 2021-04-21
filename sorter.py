import os
import file_editor as fe

CATS = []
catArr = os.listdir('./data/cats')


def sorter(unsortedList):
    # manual sorting of a list
    print("Welcome to the sorter. Here are a few tips:")
    print("1. Sort strings by typing in the number associated with the category you want")
    print("2. You can create a new category by entering NEW or N.")
    print("3. Delete a category by entering DELETE or D")
    print("4. Don't create categories with a first letter of t. Doesn't work, don't ask me why")
    print("5. When you're ready to begin, press enter. Enter EXIT or E to stop.")
    print("ENTER to begin...")
    input()
    flag = True
    wordSorted = 0
    numInputFlag = False
    while flag:
        if len(unsortedList) > 0:
            listFlag = True
            print("Categories:")
            print_cats()
            print("String:")
            print(unsortedList[0])
            choice = input()
            try:
                choice = int(choice)
                numInputFlag = True
            except ValueError:
                pass
            finally:
                pass
            if numInputFlag:
                if choice < len(CATS):
                    fileString = "./data/cats/" + CATS[choice] + ".txt"
                    file = open(fileString, 'a+')
                    fe.write_file(unsortedList[0], file)
                    file.close()
                numInputFlag = False
            else:
                if choice.upper().__eq__("NEW") or choice.upper().__eq__("N"):
                    print("What is the name of your new category?")
                    nameChoice = input()
                    add_cat(nameChoice)
                    listFlag = False
                elif choice.upper().__eq__("EXIT") or choice.upper().__eq__("E"):
                    flag = False
                elif choice.upper().__eq__("DELETE") or choice.upper().__eq__("D"):
                    print_cats()
                    print("Which category do you want to delete?")
                    catChoice = int(input())
                    catArr = os.listdir('./data/cats')
                    delCat = "./data/cats/" + catArr[catChoice]
                    if os.path.exists(delCat):
                        os.remove(delCat)
                    else:
                        print("The file does not exist")
                    listFlag = False
                else:
                    print("Bad input")
                    listFlag = False
            if listFlag:
                wordSorted += 1
                unsortedList.pop(0)

        else:
            print("You have reached the end of the list. Congratulations!")
            print("You sorted " + str(wordSorted) + " words!")
            print("ENTER to exit. Feel free to compile another list and come again!")
            input()
            flag = False



def add_cat(catName, content=None):
    #creates a new category file in /data/cats
    trunc = "./data/cats/" + catName + '.txt'
    newFile = open(trunc, 'w')
    print(catName + " created. ")
    if content is not None:
        for item in content:
            newFile.write(item+'\n')
        newFile.close()
        print("+content")


def delete_cat(cat):
    if os.path.exists(cat):
        os.remove(cat)
    else:
        print("The file does not exist")


def print_cats():
    catArr = os.listdir('./data/cats')
    for item in range(0, len(CATS)):
        CATS.pop()
    for item in catArr:
        CATS.append(item.strip('txt').strip('.'))
    counter = 0
    for item in CATS:
        print(str(counter) + ". " + item)
        counter += 1


def main():
    exampleContent = ['she is the coolest cat', 'EVER', 'and I mean EVER EVER']
    sorter(exampleContent)
    print("Please run reddit_bot.py. Goodbye")


if __name__ == '__main__':
    main()
