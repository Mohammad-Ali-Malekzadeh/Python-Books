languages = ["Farsi", "English", "Germany", "Turkish", "Arabic"]

print("------------ append() ------------")
languages.append('New Languages')
print(languages)

print("------------ insert() ------------")
languages.insert(0, 'New Languages')
print(languages)

print("------------ len() ------------")
print(len(languages))

print("------------ stored() ------------")
print(sorted(languages))
print(sorted(languages, reverse=True))

print("------------ reversed() ------------")
languages.reverse()
print(languages)
languages.reverse()
print(languages)

print("------------ pop() ------------")
languages.pop()
print(languages)

print("------------ remove() ------------")
languages.remove("Germany")
print(languages)

print("------------ sort() ------------")
languages.sort()
print(languages)
languages.sort(reverse=True)
print(languages)