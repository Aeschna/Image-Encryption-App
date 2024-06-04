from PIL import Image
import numpy as np
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding

# Encrypts image using ECB
def encrypt_ecb(image_data, key):
    cipher = Cipher(algorithms.AES(key), modes.ECB())
    encryptor = cipher.encryptor()
    return encryptor.update(image_data) + encryptor.finalize()

# Encrypts image using CBC
def encrypt_cbc(image_data, key, iv):
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
    encryptor = cipher.encryptor()
    return encryptor.update(image_data) + encryptor.finalize()

# Load the image
image_path = r'C:\Users\furka\PycharmProjects\pythonProject4\Mario.jpg'
img = Image.open(image_path).convert('L')  # Convert to grayscale

#  reduce color depth
img = img.quantize(colors=16)

# Get the original dimensions of the image
original_width, original_height = img.size
image_array = np.array(img)

# Flatten the image array
image_data = image_array.flatten()

# Pad the image data
padder = padding.PKCS7(algorithms.AES.block_size).padder()
padded_image_data = padder.update(image_data) + padder.finalize()

# Generate a random key and IV
key = b'borakisfurkan424'
iv = b'Bu da ivkeyiv156'

# Encrypts the image using ECB
encrypted_ecb_data = encrypt_ecb(padded_image_data, key)

# Encrypts the image using CBC
encrypted_cbc_data = encrypt_cbc(padded_image_data, key, iv)

encrypted_ecb_img = Image.frombytes('L', (original_width, original_height), encrypted_ecb_data)
encrypted_cbc_img = Image.frombytes('L', (original_width, original_height), encrypted_cbc_data)

encrypted_ecb_img.save('encrypted_image_ecb.jpg')
encrypted_cbc_img.save('encrypted_image_cbc.jpg')

# comparison for ecb
concatenated_ecb_img = Image.new('L', (original_width * 2, original_height))
concatenated_ecb_img.paste(img, (0, 0))
concatenated_ecb_img.paste(encrypted_ecb_img, (original_width, 0))

# comparison for cbc
concatenated_cbc_img = Image.new('L', (original_width * 2, original_height))
concatenated_cbc_img.paste(img, (0, 0))
concatenated_cbc_img.paste(encrypted_cbc_img, (original_width, 0))



# Show  images
concatenated_ecb_img.show()
concatenated_cbc_img.show()
