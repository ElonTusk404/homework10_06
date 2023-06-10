types_of_people = 10
#Используя f строки в выводе добавляет пеменную
x = f"There are {types_of_people} types of people."



#Используя f строки в выводе добавляет 2 переменные 
binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."



print(x)
print(y)


#Печатает 2 строки текста, а в тексте добавляет переменную используя ф строки
print(f"I said: {x}")
print(f"I also said: '{y}'")



hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"


#Печатает текст используя .format и выбирает переменную которую нужно добавить
print(joke_evaluation.format(hilarious))


w = "This is the left side of..."
e = "a string with a right side."
#Конкатинация 
print(w + e)

#2. Find all the places where a string is put inside a string.
# Там где используется {} исключение hilarious
#3Are you sure there are only four places? How do you know? Maybe I like lying
#Не в 4 а в 5 местах
#4Explain why adding the two strings w and e with + makes a longer string
#Используя оператор + при строках происходит создание новой строки в которой конкатинируются две строки

