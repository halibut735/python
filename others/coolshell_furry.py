def find_palindrome(raw_text):
    length = len(raw_text)
    for i in range(length-3):
        if (raw_text[i] == raw_text[i+2]) and (raw_text[i-1] == raw_text[i+3]):
            if raw_text[i-1:i+4].isalnum():
                print raw_text[i-1:i+4],

f = open('palindrome.txt','r')
text = f.read()
find_palindrome(text)
