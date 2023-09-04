class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age


def oldestCat(*cat_objects):
    oldest_age = 0
    oldest_cat = ''
    cat_objects = list(filter(lambda cat: cat is not None, cat_objects))
    for cat in cat_objects:
        if cat.age > oldest_age:
            oldest_age = cat.age
            oldest_cat = cat.name
    return print(f'the oldest cat is {oldest_cat} : {oldest_age} years old')


cat1 = Cat('bruno', 3)
cat2 = Cat('kicik', 4)
cat3 = Cat('oyen', 7)
cat4 = Cat('bandel', 5)

oldestCat(cat1, cat2, cat3, cat4)
