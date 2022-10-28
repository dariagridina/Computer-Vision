import cv2
from cryptosteganography import CryptoSteganography

img = cv2.imread('bloom.jpg')
print(f'Image shape is: {img.shape}')

crypto_steganography = CryptoSteganography('CV')
crypto_steganography.hide('bloom.jpg', 'bloom_encode.png', 'Wizja Komputerowa 2022')
secret = crypto_steganography.retrieve('bloom_encode.png')
print(secret)
