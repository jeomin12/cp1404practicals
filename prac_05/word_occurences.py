"""
Word Occurrences
Estimate: 15 minutes
Actual:   10 minutes
"""
text = input("Text: ")

word_counts = {}
for word in text.split():
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

longest_word_length = max(len(word) for word in word_counts.keys())
for word in sorted(word_counts):
    print(f"{word:{longest_word_length}} : {word_counts[word]}")

