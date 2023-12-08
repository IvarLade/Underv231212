import os

def generate_html_page(page_number):
    page_name = f"page{page_number:02d}"
    image_name = f"{page_name}.png"
    next_page = f"page{page_number + 1:02d}.html"

    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{page_name}</title>
    </head>
    <body>
        <div>
            <a href="../page01.html">Next Page<img src="page01.png" alt="page01"></a>
        </div>
        <div>
            <img src="{image_name}" alt="{page_name}">
        </div>
        <a href="{next_page}">Next Page</a>
    </body>
    </html>
    """

    with open(f"{page_name}.html", "w") as file:
        file.write(html_content)

# Create 24 HTML pages
for page_number in range(1, 25):
    generate_html_page(page_number)
