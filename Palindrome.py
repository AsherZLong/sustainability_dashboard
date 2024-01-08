def string_reverser(str):
    if len(str) == 1:
        return str
    else:
        last_letter = str[-1]
        rest_of_str = str[:len(str)-1]
        str = string_reverser(rest_of_str)
        flipped_str = last_letter+str
        return flipped_str

def palindrome_tester(str):
    r = string_reverser(str)
    if r == str:
        print(str+' is a palindrome')
    else:
        print(str+' is not a palindrome')

print(string_reverser('play'))