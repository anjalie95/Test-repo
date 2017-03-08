def reverse(word):
    s = []
    reverseword = ""
    for i in word:
        s.append(i)
    while(len(s)!=0):
        reverseword+=s.pop()
    return reverseword
print(reverse("eranga"))

