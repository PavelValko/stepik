# with open('dataset_3363_3.txt', 'r') as f:
#     text = f.read().lower().split()
# popular_word = max(set(text), key=text.count)
# print(popular_word, text.count(popular_word))


with open('dataset_3363_3.txt', 'r') as f:
    max_count = 0
    text = f.read().lower().split()
    text.sort()
    for word in text:
        counter = text.count(word)
        if counter > max_count:
            max_count = counter
            result = word

print(result, max_count)
