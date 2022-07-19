
chosen_volume = input('Which volume of scripture would you like to learn about? ')
max_chapters = -1
book_with_max = ""

with open('books_and_chapters.txt') as books_and_chapters:
    next(books_and_chapters)

    output = []

    for data in books_and_chapters:
        clean_data = data.strip()
        split_data = clean_data.split(':')

        book = split_data[0]
        chapters = int(split_data[1])
        scriptures = split_data[2]

        output.append({'Book': book, 'Chapter': chapters, 'Scriptures': scriptures})

        if scriptures.lower() == chosen_volume.lower():

         if chapters > max_chapters:
            
            max_chapters = chapters 
            book_with_max = book 
            
print(f"The book with the most chapters is: {book_with_max}")
print(f"It has {max_chapters} chapters.")

