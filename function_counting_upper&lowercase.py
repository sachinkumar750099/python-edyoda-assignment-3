
def count_letters(string):
    lower=0
    upper=0
    for t in string:
        for i in t:
            if i.isupper():
                upper+=1
            elif i.islower():
                lower+=1
    print("the no os upper case letters",upper)
    print("the no of lower case letters",lower)
count_letters('The quick Brown Fox')