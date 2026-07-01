from PIL import Image
import os


def compress_images(image_folder):
    try:
        for file in os.listdir(image_folder):
            file_path = os.path.join(image_folder, file)
            file_name, file_extension = os.path.splitext(file)
            print("comprimiendo archivo: " + file_name + file_extension)
            if file_extension == ".png":
                file_compress = Image.open(file_path)
                output_path = os.path.join(
                    image_folder,
                    file_name + "_comprimido.png"
                    )
                file_compress.save(output_path,
                                   optimize=True,
                                   quality=70)
    except FileNotFoundError as error:
        print(error)


if __name__ == "__main__":
    compress_images(r"C:\Development\prueba")
