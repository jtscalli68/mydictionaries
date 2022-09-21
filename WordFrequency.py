

infile = open('sometext-4.txt','r')

read = infile.readlines()

wordbank = {}
count = 0

# for i in read: 
#     word = i.split()
              #```` add key value pair (word and count) 
    # if i in wordbank:           #if ii ni wordbank (count +1) else (add key to the dicgionary )
    #     count =+ 1
    # else:
    #     break
        


for i in read:
    word = i.split()
    if i in word:
        count += 1
    else:
        i = word
    for k, v in i.items():
        wordbank[k] = v

print(wordbank)