phrase = "Don't panic!"
plist = list(phrase)
print(phrase)
print(plist)

new_phrase=''.join(plist[1:3])+' '+''.join([plist[4],plist[-5],plist[-6]])


print(plist)
print(new_phrase)
