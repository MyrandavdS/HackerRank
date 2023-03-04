s = input()

news = []
# split() splits on every space, split(" ") splits only on one space
new = s.split(" ")
for i in new:
    # append so it will add to the list and not overwrite it.
    # capitalize is making the first letter a capital of the word
    news.append(str(i.capitalize()))
    print(str(i.capitalize()))
    print(i)
    print(news)

joins = ' '.join(news)
print(joins)
#132 456 Wq M E
#132 456 Wq M E