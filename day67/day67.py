# 1. წინადადება
sentence = "ეს არის ჩემი პირველი წინადადება პითონში"

# 2. წინადადების გადაქცევა სიად
words = sentence.split()

# შედეგი
print(words)
# 1. სიტყვების სია
words = ["პითონი", "არის", "ძალიან", "მოსახერხებელი", "ენა"]

# 2. სიიდან სტრინგის მიღება
sentence = " ".join(words)

# შედეგი
print(sentence)
# 1. წინადადება
sentence = "ეს#არის#მაგალითი#დავალება"

# 2. დაშლა სიად
words = sentence.split('#')

# 3. გაერთიანება $-ით
new_sentence = "$".join(words)

# შედეგი
print(new_sentence)
