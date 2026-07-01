from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

#  fond  https://fonts.google.com/specimen/Roboto


def get_image(image_file):
    try:
        image = Image.open(image_file)
        print(image.size)
        print(image.mode)
        print(image.format)
        # image.show()
        # image_blackwhite = image.convert("L")
        # image_blackwhite.show()
        # image_blackwhite.save("mine_bn.jpg")
        font = ImageFont.truetype(
            'fonts/Roboto-VariableFont_wdth,wght.ttf',
            25
            )
        draw = ImageDraw.Draw(image)
        draw.text(
            (50, 0),  # ubicación del texto
            "Mina Cerro Verde",
            (255, 255, 255),
            font
        )
        image.show()
        image.save("mine_font.jpg")

        # create thumbnail (imagen reducida)
        image.thumbnail((30, 30))
        image.show()
        image.save("mine_thumbnail.jpg")
    except FileNotFoundError:
        print("no se encontró la imagen")


if __name__ == "__main__":
    get_image("mine.jpg")
