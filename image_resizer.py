import cv2

original_image = input('Name of your image: ')
original_image_extension = input('What is the extension of the image you provided? ')
resized_image = input('Name your resized image: ')
resized_image_extension = input('What extension should the resized image have? Please specify: ')

img = cv2.imread(original_image+original_image_extension, cv2.IMREAD_UNCHANGED)
# cv2.imshow('HRISHI', img)

print('\nHow much do you want your image to be resized?')
scale = int(input('Enter any number from 1 to 100: '))

width = int(img.shape[1] * scale / 100)
height = int(img.shape[0] * scale / 100)

output = cv2.resize(img, (width, height))

cv2.imwrite(resized_image+resized_image_extension, output)

print('\n          ---- Thank You ----')
print(f'{original_image+original_image_extension} has been resized to a scale of {scale}%')
print(f'You can view your resized image with the name {resized_image+resized_image_extension}')

cv2.waitKey(0)