def alternate(n, first_value, second_value):
    return [first_value if i % 2 == 0 else second_value for i in range(n)]
print(alternate(5, 'true', 'false'))  # ['true', 'false', 'true', 'false', 'true']
def split_by_a(sentence):
    return sentence.split("ა")
print(split_by_a("მესამე ეტაპი წავიდა კარგად"))  
# ['მეს', 'მე ეტაპი წავიდ', ' კ', 'რად']
print(join_with_star(["ეს", "არის", "ტესტი"]))  
# 'ეს*არის*ტესტი'
def count_positives_sum_negatives(arr):
    if not arr:
        return []
    count_positives = sum(1 for x in arr if x > 0)
    sum_negatives = sum(x for x in arr if x < 0)
    return [count_positives, sum_negatives]
def digitize(n):
    return [int(d) for d in str(n)][::-1]
