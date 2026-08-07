paragraph = input("Enter a paragraph: ")
print(list[paragraph.split()])
word=list(paragraph.split())

total_words=len(word)

unique_words=set(word)

longest_word=max(word,key=len)

shortest_word=min(word, key=len)

duplicate_words = []

for a in word:
    if word.count(a) > 1 and a not in duplicate_words:
        duplicate_words.append(a)

print("Total number of words :", total_words)
print("Number of unique words :", unique_words)
print("Longest word :", longest_word)
print("Shortest word :", shortest_word)
print("Words appearing more than once :", duplicate_words)
