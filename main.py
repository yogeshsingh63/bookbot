
def main():
    path = "books\frankenstein.txt"
    text = get_book_text(path)
    num_words = countWords(text)
    chars_dict = get_char_dict(text)
    print(chars_dict)

def get_char_dict(text):
    chars = {}
    for c in text:
        lowered=c.lower()
        if lowered in chars:
            chars[lowered]+=1
        else: 
            chars[lowered]=1
    return chars

def countWords(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()
