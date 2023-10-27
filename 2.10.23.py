car = {
"brand": "Ford",
"model":"mustang",
"year":1964
}
print(car)
#принт 

car = {
"brand": "Ford",
"model":"mustang",
"year":1964
}
car.update({"year": 2018})
print(car)
#обновляет но новое название

car = {
"brand": "Ford",
"model":"mustang",
"year":1964
}
car["color"] = "red"
print(car)
#добовляет новый элемент


car = {
"brand": "Ford",
"model":"mustang",
"year":1964
}
car.pop("model")
print(car)
#удаляет !

car = {
"brand": "Ford",
"model":"mustang",
"year":1964
}
car.popitem()
print(car)
#удаляет последний

car = {
"brand": "Ford",
"model":"mustang",
"year":1964
}
del car["brand"]
print(car)
#тоже удаляет


pist = {
"perezaryd": "glock",
"razal": "odan",
"grizlyy": "onetwo"
}
x = pist.get("razal")
print(x)
#выводит тот ключ

pist = {
"perezaryd": "glock",
"razal": "odan",
"grizlyy": "onetwo"
}
print(pist.keys())
#показывает все ключи


#            новый этап set


set = {"one",1,2,3,4}
set.remove("one")
print(set)
#удаляет тот элемент который ты выбрал
set = {"one",1,2,3,4}
x = set.pop()
print(x)
print(set)
#удаляет любой элемент

set = {"one",1,2,3,4}
for i in set:
    print(i)
#показать все значение

set1 = {"one",1,2,3,4}
set2 = {99, 11, "n"}

set1.update(set2)
print(set1)
#обьедениение


set6 = {"ttree","daad"}
set2 = {1,2,3}

set6.update(set2)
print(set6)

#1
pist = {
"perezaryd": "glock",
"razal": "odan",
"grizlyy": "onetwo"
}
print(pist)



#2
pist = {
"perezaryd": "glock",
"razal": "odan",
"grizlyy": "onetwo"
}
pist["str"] = 1234
print(pist)


#3
pist = {
"perezaryd": "glock",
"razal": "odan",
"grizlyy": "onetwo",
}
pist["tuple"] = "[1,2,3,4,5]"
print(pist)



#4
pist = {
"perezaryd": "glock",
"razal": "odan",
"grizlyy": "onetwo"
}
x = pist.get("razal")
print(x)



#5
pist = {
"perezaryd": "glock",
"razal": "odan",
"grizlyy": "onetwo"
}
del pist["razal"]
print(pist)



#6
pist = {
"perezaryd": "glock",
"razal": "odan",
"grizlyy": "onetwo"
}
print(pist.keys())

