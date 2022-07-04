sentence = input()
l = sentence.split()
l1 =[]

for word in l:
    wr = ''
    for i in range(len(word)):
        if i == 0:
            wr += word[i]
        elif word[i] > word[i-1]:
            wr += word[i].upper()
        elif word[i] < word[i-1]:
            wr += word[i].lower()
        else:
            wr += word[i]
    l1.append(wr)
print(" ".join(l1))
