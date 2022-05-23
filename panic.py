phrase = "Don't panic!"
plist = list(phrase)
print(phrase)
print(plist)

for x in range(5):
    plist.pop()
plist.pop(-2)
plist.pop(-3)
plist.pop(0)
plist.insert(2,' ')
plist.insert(-1,'a')

new_phrase =''.join(plist)
print(plist)
print(new_phrase)

