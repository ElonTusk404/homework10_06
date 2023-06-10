formatter = "{} {} {} {}"
print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    "Жили были",
    "Поживали",
    "Обитали",
    "Выживали"
))
#1 Take the formatter string defined on line 1.
#{}{}{}{}{}
#3. Pass to format four arguments, which match up with the four {} in the formatter variable. This is like passing arguments to the command line command format
print(formatter.format('Дом', 'Дома', 'Много домов', 'Несколько домов'))

