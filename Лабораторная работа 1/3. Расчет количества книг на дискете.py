weight_of_one_character = 4
characters_per_line = 25
lines_on_the_page = 50
number_of_pages = 100

#вес книги в байтах
book0 = weight_of_one_character * characters_per_line * lines_on_the_page * number_of_pages
#вес книги в килобайтах
book01 = book0 / 1024
#вес книги в мегабайтах
book012 = book01 / 1024

#информационный объем дискеты
volume = 1.44

number_of_books = volume // book012

print("Количество книг, помещающихся на дискету:", number_of_books)
