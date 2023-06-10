tabby_cat = "\tI'm tabbed in."
persiancat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""
print(tabby_cat)
print(persiancat)
print(backslash_cat)
print(fat_cat)
#2. Use ''' (triple-single-quote) instead. Can you see why you might use that instead of """?
#можно использовать оба варианта как удобно
#3Combine escape sequences and format strings to create a more complex format.
country = 'Russia'
print(f"I live in \n {country}")
print('I live in {}'.format(country))