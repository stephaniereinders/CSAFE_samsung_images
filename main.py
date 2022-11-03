from PIL import Image, ExifTags
import os


def print_exif(img):
    img = Image.open(img)
    img_exif = img.getexif()

    if img_exif is None:
        print('Sorry, image has no exif data.')
    else:
        for key, val in img_exif.items():
            if key in ExifTags.TAGS:
                print(f'{ExifTags.TAGS[key]}:{val}')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # specify the img directory path
    path = "/Users/stephanie/Documents/non_version_control/CSAFE/CSAFE_Samsung_Images/Samsung Galaxy S21-2 (black)"

    # list images in img directory
    files = os.listdir(path)

    print_exif(img=os.path.join(path, files[0]))

