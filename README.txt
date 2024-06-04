First of all I chose my language as python. Because its libraries are really useful. 
I imported my libraries like numpy, PIL, cryptography.hazmat.primitives.ciphers. I am not sure 
but code is probably older version of cryptography because I could not manage to apply last ver.
I started with craeting functions for encrypting images with ecb and cbc. I read image from path. 
I used this line -> img = img.quantize(colors=16) for better image results. 
I padded the images with padding scheme. Key and iv generated and with these encrypting in funbctions.
Then I created a image object using frombytes. L mode is for grayscale images. Images are saved to where
your code file. Lastly I added a code which we can observe images side by side. In code you can check comment lines 
for each step. When code is runned, images will be automatically opened.