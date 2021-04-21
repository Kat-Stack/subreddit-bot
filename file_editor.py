

# separates titles and URLs
def separator(listOfWords, urls='data/urls', titles='data/titles'):
    urlList = []
    titleList = []
    # had to have the encoding bit or it messed up at around entry 43 of the reddit scrape
    title = open(titles, "w", encoding='utf-8')
    url = open(urls, "w", encoding='utf-8')
    for x in listOfWords:
        titleList.append(x[0] + "\n")
        urlList.append(x[1] + "\n")
    for item in titleList:
        title.write(item)
    for item in urlList:
        url.write(item)

def write_file(message, file):
    file.write(message.strip() + "\n")



# prints a file's text
def read_file(fileUrl):
    try:
        f = open(fileUrl, "r", encoding='utf-8')
        lines = []
        for x in f:
            lines.append(x.strip())
        return lines

    except IOError:
        print(fileUrl + " not accessible")

# Opens and returns a file
def open_file(fileUrl):
    try:
        f = open(fileUrl, "r")
        print(fileUrl + " has been opened")
        return f
    except IOError:
        print(fileUrl + " not accessible")


def main():
    print(read_file("data/urls"))


if __name__ == '__main__':
    main()
