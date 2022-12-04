from PIL import Image, ImageFilter

beforeBlur = Image.open("images/image1.jpg")
beforeBlur.show()

#3 types of blur (ImageFilter.BLUR) & (ImageFilter.BoxBlur(value)) third is below.
afterBlur = beforeBlur.filter(ImageFilter.GaussianBlur(5))
afterBlur.show()

afterBlur.save("images/GaussianBlur.jpg")