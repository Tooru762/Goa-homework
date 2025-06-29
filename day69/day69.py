def split_and_join_on_g(word):
    parts = word.split('g')  # ვყოფთ პატარა g-ზე
    result = 'G'.join(parts)  # ვაერთიანებთ დიდ G-თი
    return result
print(split_and_join_on_g("dogging"))  # შედეგი: doGGinG
def invert_case(word):
    return ''.join([char.lower() if char.isupper() else char.upper() for char in word])
print(join_numbers_with_at([1, 23, 456]))  # შედეგი: "1@23@456"
def join_numbers_with_at(numbers):
    str_numbers = [str(num) for num in numbers]  # რიცხვების სტრინგებად გადაქცევა
    return '@'.join(str_numbers)
