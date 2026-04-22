from collections import Counter

text = input("Enter text: ").lower().split()
freq = Counter(text)

for word, count in freq.items():
    print(word, ":", count)
