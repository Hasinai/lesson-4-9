
from hw_5.fizzbuzz import FizzBuzz
from package_images import Im_PIL
from HomeLibrary.HomeLibrary import HomeLibrary
from package_images.Im_PIL import (ImageReader,Monochrome,Vector)
from PIL.ImageFilter import (
    BLUR, CONTOUR, DETAIL, EDGE_ENHANCE, EDGE_ENHANCE_MORE,
    EMBOSS, FIND_EDGES, SMOOTH, SMOOTH_MORE, SHARPEN
)

if __name__ == "__main__":
	"""
	fizzbuzz
	"""
	print("Calculation FizzBuzz. Please, input itertation count ")
	n = input("int = ")
	fizzbuzz = FizzBuzz(n)
	print(fizzbuzz.calculate())
	#class HomeLibrary work
	
	#мої улюблені книги
	library = HomeLibrary()

	library.add_book(1, {
		'author': 'Гаррі Гаррісон',
		'title': 'Машина часу Техніколор',
		'publisher': 'Doubleday',
		'genre': 'роман',
		'year': 1967 })

	library.add_book(2, {
		'author': 'Кліффорд Саймак',
		'title': 'Кільце навколо Сонця',
		'publisher': 'Simon & Schuster',
		'genre': 'науково-фантастичний роман',
		'year': 1953 })

	

	print(library.get_book(1))  # Виведе інформацію про книгу з ID 1
	print(library.search_by_author('Гаррі Гаррісон'))  # Виведе всі книги автора George Orwell
	print(library.search_by_year(1953))  # Виведе всі книги, видані у 1960 році
	print(library.search_by_genre('Simon & Schuster'))  # Виведе всі книги жанру Dystopian

	#список усіх книг
	library.list_books()
	# видалити книгу по ІД
	library.remove_book(1)
    
    #image processing
	mono = Monochrome("novogrodovka.jpg")
	mono.apply_monochrome(10)
	mono.save_image("stop.jpg")

	filter_im = Vector("stop.jpg")
	filter_im.apply_filter(CONTOUR)
	filter_im.save_image("stop_filter.jpg")