#DAY 1, I learnt about data structures, basically it's a way of organizinng and storing data efficiently#

#LIST, helps us store multiple values and ddata types in a variable#
names = ["Jedidiah", "David", "Abiodun"]
print(names)
print(names[0])
jedidiah = ["boy", 15, 6.5,]
print(jedidiah)
#We use "append" to add a value to a list and "remove" to remove a value from a list#
names.append("Joshua")
print(names)
names.remove("Joshua")
print(names)

#DICTIONARY, it stores data in key-value pairs#
intern = {
    "name": "jay",
    "occupation": "student",
    "course": "cmp sci",
    "height": "6.5"
}
print(intern)

#TUPLES, very similar to list in almost every way except that the values of tuples don't change, and it uses"()"#
mentor = ("Abiodun", 35, 6.0,)
print(mentor)

#SETS, a collection of items that cannot be duolicated, that is each one is unique#
my_set = {1, 2.2, "jay"}
print(my_set)
