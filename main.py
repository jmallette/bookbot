def openbook():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        return(file_contents)

def wc(textbody):
    return len(textbody.split())

def lettercount(textbody):
    lc = {}
    textbody = textbody.lower()
    for l in textbody:
        if l in lc:
            lc[l] += 1
        elif l not in lc:
            lc[l] = 1
    return lc

def bookreport(wc, letterdict):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{wc} words found in the document.\n")
    for letter in letterdict:
        if letter.isalpha():
            print(f"The character '{letter}' was found {letterdict[letter]} times.")

def main():
    body = openbook()
    get_wc = wc(body)
    lc_dict = lettercount(body)
    bookreport(get_wc, lc_dict)

main()