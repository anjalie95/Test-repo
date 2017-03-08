def decrypt(statement):
    list1=[]
    count=0
    while count<len(statement):
        asci=ord(statement[count])
        if asci==97:
            asci=122
            new=chr(122)
        else:
            new=chr(ord(statement[count])-1)
        list1.append(new)
        count+=1
    glue=""
    newWord=glue.join(list1)
    match(newWord)
    
def match(word):
    if "find" in word:
        print (word)
    else:
        decrypt(word)
   
decrypt("ldepctilcplcctgtyrqtyolawlnpezstop")
