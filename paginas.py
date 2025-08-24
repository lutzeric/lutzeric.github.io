import os

def generate_book_detail_html(book_name, price, main_image, detail_images, long_description, filename):
    """
    Generates a single HTML file for a book's detailed description.
    """
    # Ensure the main image path is correctly relative or a full URL
    main_image_src = main_image
    if not main_image.startswith('http') and not main_image.startswith('/'):
        main_image_src = f"{main_image}" # Assumes images are in the same directory for simplicity

    # Generate HTML for detail images, using placeholders if none are provided
    detail_images_html = ""
    if detail_images:
        detail_images_html = ''.join([f"""
                        <img src="{img_src}"
                             alt="{book_name} - Vista {i+1}"
                             class="w-24 h-24 object-cover rounded-md cursor-pointer hover:border-2 hover:border-purple-500 transition duration-150"
                             onerror="this.onerror=null; this.src='https://placehold.co/100x100/BBBBBB/000000?text=Error';">
                        """ for i, img_src in enumerate(detail_images)])
    else:
        # Default placeholder if no detail images are provided
        for i in range(4): # Generate 4 generic placeholders
            detail_images_html += f"""
                        <img src="https://placehold.co/100x100/A0A0A0/FFFFFF?text=Vista+{i+1}"
                             alt="{book_name} - Vista {i+1}"
                             class="w-24 h-24 object-cover rounded-md cursor-pointer hover:border-2 hover:border-purple-500 transition duration-150"
                             onerror="this.onerror=null; this.src='https://placehold.co/100x100/BBBBBB/000000?text=Error';">
            """

    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{book_name} - Detalles</title>
        <script src="https://cdn.tailwindcss.com"></script>
        <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
        <style>
            body {{
                font-family: 'Inter', sans-serif;
                -webkit-font-smoothing: antialiased;
                -moz-osx-font-smoothing: grayscale;
            }}
        </style>
    </head>
    <body class="bg-gray-100 text-gray-800">

        <header class="bg-gradient-to-r from-purple-600 to-pink-500 text-white p-4 shadow-lg rounded-b-lg">
            <div class="container mx-auto flex flex-col sm:flex-row justify-between items-center px-4">
                <h1 class="text-3xl font-bold mb-2 sm:mb-0">My Awesome Store</h1>
                <nav>
                    <ul class="flex space-x-4">
                        <li><a href="index.html" class="hover:text-purple-200 transition duration-300">Home</a></li>
                        <li><a href="instrumentos.html" class="hover:text-purple-200 transition duration-300">Instrumentos</a></li>
                        <li><a href="libros.html" class="hover:text-purple-200 transition duration-300">Libros</a></li>
                        <li><a href="otros.html" class="hover:text-purple-200 transition duration-300">Otros</a></li>
                    </ul>
                </nav>
            </div>
        </header>

        <main class="container mx-auto my-8 p-4 bg-white rounded-xl shadow-lg">
            <div class="grid grid-cols-1 lg:grid-cols-2 gap-8">
                <div class="flex flex-col items-center">
                    <img src="{main_image_src}"
                         alt="{book_name} - Imagen Principal"
                         class="w-full max-w-md h-auto rounded-xl shadow-md mb-4 object-cover"
                         onerror="this.onerror=null; this.src='https://placehold.co/600x400/CCCCCC/000000?text=Main+Image+Not+Found';">
                    <div class="flex space-x-2 overflow-x-auto w-full max-w-md">
                        {detail_images_html}
                    </div>
                </div>

                <div>
                    <h2 class="text-4xl font-extrabold mb-4 text-purple-700">{book_name}</h2>
                    <p class="text-gray-600 text-lg mb-6">
                        {long_description}
                    </p>
                    <div class="flex items-center justify-between mb-6">
                        <span class="text-5xl font-bold text-green-600">${price:.2f}</span>
                        <button class="bg-purple-600 hover:bg-purple-700 text-white font-bold py-3 px-8 rounded-full shadow-lg transition duration-300 ease-in-out transform hover:scale-105">
                            Añadir al Carrito
                        </button>
                    </div>
                    <div class="mt-8 border-t border-gray-200 pt-6">
                        <h3 class="text-2xl font-semibold mb-3 text-purple-800">Opiniones de Clientes</h3>
                        <div class="space-y-4">
                            <div class="bg-gray-50 p-4 rounded-lg shadow-sm">
                                <p class="font-semibold text-gray-900">Usuario Anónimo <span class="text-yellow-500">★★★★★</span></p>
                                <p class="text-gray-700">"¡Un libro fantástico! Totalmente recomendado."</p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </main>

        <footer class="bg-gray-800 text-white p-6 mt-10 rounded-t-lg">
            <div class="container mx-auto text-center px-4">
                <p>&copy; 2025 My Awesome Store. Todos los derechos reservados.</p>
                <p class="mt-2">
                    <a href="#" class="text-purple-400 hover:text-purple-300 transition duration-300">Política de Privacidad</a> |
                    <a href="#" class="text-purple-400 hover:text-purple-300 transition duration-300">Términos de Servicio</a>
                </p>
                <div class="flex justify-center space-x-4 mt-4">
                    <a href="#" class="text-gray-400 hover:text-white transition duration-300">Facebook</a>
                    <a href="#" class="text-gray-400 hover:text-white transition duration-300">Instagram</a>
                    <a href="#" class="text-gray-400 hover:text-white transition duration-300">Twitter</a>
                </div>
            </div>
        </footer>

    </body>
    </html>
    """
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html_content)

def generate_libros_html(books_data, output_filename="libros.html"):
    """
    Generates the main libros.html category page with cards for each book.
    Also calls generate_book_detail_html for each book.
    """
    header = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Libros - My Awesome Store</title>
        <script src="https://cdn.tailwindcss.com"></script>
        <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
        <style>
            body {
                font-family: 'Inter', sans-serif;
                -webkit-font-smoothing: antialiased;
                -moz-osx-font-smoothing: grayscale;
            }
        </style>
    </head>
    <body class="bg-gray-100 text-gray-800">

        <header class="bg-gradient-to-r from-purple-600 to-pink-500 text-white p-4 shadow-lg rounded-b-lg">
            <div class="container mx-auto flex flex-col sm:flex-row justify-between items-center px-4">
                <h1 class="text-3xl font-bold mb-2 sm:mb-0">My Awesome Store</h1>
                <nav>
                    <ul class="flex space-x-4">
                        <li><a href="index.html" class="hover:text-purple-200 transition duration-300">Home</a></li>
                        <li><a href="instrumentos.html" class="hover:text-purple-200 transition duration-300">Instrumentos</a></li>
                        <li><a href="libros.html" class="hover:text-purple-200 transition duration-300">Libros</a></li>
                        <li><a href="otros.html" class="hover:text-purple-200 transition duration-300">Otros</a></li>
                    </ul>
                </nav>
            </div>
        </header>

        <main class="container mx-auto my-8 p-4">
            <h2 class="text-4xl font-extrabold text-center mb-10 text-purple-700">Nuestra Colección de Libros</h2>

            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
    """

    footer = """
            </div>
        </main>

        <footer class="bg-gray-800 text-white p-6 mt-10 rounded-t-lg">
            <div class="container mx-auto text-center px-4">
                <p>&copy; 2025 My Awesome Store. Todos los derechos reservados.</p>
                <p class="mt-2">
                    <a href="#" class="text-purple-400 hover:text-purple-300 transition duration-300">Política de Privacidad</a> |
                    <a href="#" class="text-purple-400 hover:text-purple-300 transition duration-300">Términos de Servicio</a>
                </p>
                <div class="flex justify-center space-x-4 mt-4">
                    <a href="#" class="text-gray-400 hover:text-white transition duration-300">Facebook</a>
                    <a href="#" class="text-gray-400 hover:text-white transition duration-300">Instagram</a>
                    <a href="#" class="text-gray-400 hover:text-white transition duration-300">Twitter</a>
                </div>
            </div>
        </footer>

    </body>
    </html>
    """

    book_cards = []
    for book in books_data:
        # Generate filename for detail page
        # Converts "Book Name Example" to "libro-book-name-example-detail.html"
        detail_filename = f"libro-{book['name'].lower().replace(' ', '-')}-detail.html"

        # Generate the card for libros.html
        card = f"""
                <!-- Item Card: {book['name']} -->
                <div class="bg-white rounded-xl shadow-lg hover:shadow-2xl transition duration-300 overflow-hidden">
                    <a href="{detail_filename}" class="block">
                        <img src="{book['main_image']}"
                             alt="{book['name']}"
                             class="w-full h-48 object-cover rounded-t-xl"
                             onerror="this.onerror=null; this.src='https://placehold.co/600x400/CCCCCC/000000?text=Image+Not+Found';">
                        <div class="p-6">
                            <h3 class="text-2xl font-semibold mb-2 text-purple-800">{book['name']}</h3>
                            <p class="text-gray-600 mb-4 line-clamp-3">
                                {book['short_description']}
                            </p>
                            <div class="flex items-center justify-between">
                                <span class="text-3xl font-bold text-green-600">${book['price']:.2f}</span>
                                <button class="bg-purple-600 hover:bg-purple-700 text-white font-bold py-2 px-6 rounded-full shadow-md transition duration-300 ease-in-out transform hover:scale-105">
                                    Ver Detalles
                                </button>
                            </div>
                        </div>
                    </a>
                </div>
        """
        book_cards.append(card)

        # Generate the individual book detail HTML page
        generate_book_detail_html(
            book_name=book['name'],
            price=book['price'],
            main_image=book['main_image'],
            detail_images=book['detail_images'],
            long_description=book['long_description'],
            filename=detail_filename
        )

    full_html_content = header + "\n".join(book_cards) + footer

    with open(output_filename, 'w', encoding='utf-8') as f:
        f.write(full_html_content)

# --- Example Usage ---
# Define your book data here
books_to_generate = [
    {
        'name': 'El Principito',
        'price': 15.50,
        'main_image': 'https://placehold.co/600x400/FFD1DC/FF0000?text=El+Principito',
        'detail_images': [
            'https://placehold.co/100x100/FFD1DC/FF0000?text=P1',
            'https://placehold.co/100x100/FFD1DC/FF0000?text=P2',
            'https://placehold.co/100x100/FFD1DC/FF0000?text=P3'
        ],
        'short_description': 'Una hermosa historia sobre un pequeño príncipe de un planeta lejano.',
        'long_description': 'El Principito es una novela corta y la obra más famosa del escritor y aviador francés Antoine de Saint-Exupéry. Fue publicado en 1943 en Estados Unidos y cuenta con ilustraciones del propio autor. Es un libro universalmente conocido y apreciado por lectores de todas las edades.'
    },
    {
        'name': 'Cien Años de Soledad',
        'price': 22.00,
        'main_image': 'https://placehold.co/600x400/B0E0E6/000080?text=Cien+Anos+Soledad',
        'detail_images': [
            'https://placehold.co/100x100/B0E0E6/000080?text=S1',
            'https://placehold.co/100x100/B0E0E6/000080?text=S2'
        ],
        'short_description': 'La obra maestra de Gabriel García Márquez, un pilar del realismo mágico.',
        'long_description': 'Cien años de soledad es una novela del escritor colombiano Gabriel García Márquez, ganador del Premio Nobel de Literatura en 1982. Es considerada una obra maestra de la literatura hispanoamericana y universal, así como una de las obras más traducidas y leídas en español. Fue publicada por primera vez en 1967.'
    },
    {
        'name': 'Don Quijote de la Mancha',
        'price': 18.75,
        'main_image': 'https://placehold.co/600x400/DAA520/8B4513?text=Don+Quijote',
        'detail_images': [
            'https://placehold.co/100x100/DAA520/8B4513?text=Q1',
            'https://placehold.co/100x100/DAA520/8B4513?text=Q2',
            'https://placehold.co/100x100/DAA520/8B4513?text=Q3',
            'https://placehold.co/100x100/DAA520/8B4513?text=Q4'
        ],
        'short_description': 'La icónica novela de Miguel de Cervantes, un clásico de la literatura española.',
        'long_description': 'El ingenioso hidalgo Don Quijote de la Mancha es una novela escrita por Miguel de Cervantes Saavedra. Publicada su primera parte con fecha de 1605, es una de las obras más destacadas de la literatura española y la literatura universal, y una de las más traducidas. Es considerada la primera novela moderna.'
    },
]

# Run the generator
generate_libros_html(books_to_generate)
print("HTML files for 'Libros' category and individual book pages have been generated!")

