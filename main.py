import re

# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}


def read_file_content(filename):
    # [assignment] Add your code here 
    my_file = open(filename)
    b = my_file.read()
    c = re.sub(r'[^\w\s]', ' ', b)
    my_array = []
    
    for x in c.split():
        my_array.append(x)
        my_file.close()
    return my_array


#read_file_content("story.txt")


def count_words():
    dic_key = read_file_content("./story.txt")
    # [assignment] Add your code here
    dic_value = []
    
    for x in dic_key:
        dic_value.append( dic_key.count(x))
    
    mydict = {dic_key[i]: dic_value[i] for i in range(len(dic_key))}
 
    return mydict


    
#    return {"as": 10, "would": 20}
   
#count_words()   
