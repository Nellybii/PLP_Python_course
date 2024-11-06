my_list = [23, 24, 25, 26, 27, 28]
sum_list = sum(my_list)
print(sum_list)

books = ("The Stong Workbook", "A Parallel Life Cycle", "A Strong Woman")

for book in books:
    print(book)


person = {
    "name": "John Doe",
    "age": 30,
    "favourite_color": "green",	
    }

print(person)

words = ["apple", "banana", "cherry", "date", "fig", "grape"]
for word in words:
    if len(word) % 2 == 0:
        print(word)