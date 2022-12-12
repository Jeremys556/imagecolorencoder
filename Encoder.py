from PIL import Image
import bitarray

endMessage = "11111111"

img = Image.open("encoderImage.png")
message = str(input("What text would you like to encode? "))
width, height = img.size

messageBitArray = bitarray.bitarray()
messageBitArray.frombytes(message.encode('utf-8'))
messageBitArray = list(messageBitArray)

x = 0
y = 0
for bit in messageBitArray:
    coordinate = (x,y)
    try:
        [r, g, b, a] = img.getpixel(coordinate)
    except: #incase image does not have alpha
        [r, g, b] = img.getpixel(coordinate)
        a = 255
    #Turn R into r, but remove last pixel and turn it into the bit we are encoding
    RIntString = list(str(r))
    lastRInt = RIntString[len(RIntString)-1]
    newRInt = ""

    #Only change the very last number of the r string to make a minimal change
    for rInt in range(len(RIntString)-2):
        newRInt = newRInt + str(rInt)
    newRInt = newRInt + str(bit)

    img.putpixel((coordinate), (int(newRInt), g, b, a))

    if x != width-1:
        x += 1
    else:
        y += 1
        x = 0

for bit in endMessage:
    coordinate = (x,y)

    #get pixel values
    try:
        [r, g, b, a] = img.getpixel(coordinate)
    except: #incase image does not have alpha
        [r, g, b] = img.getpixel(coordinate)
        a = 255

    #Turn R into r, but remove last pixel and turn it into the bit we are encoding
    RIntString = list(str(r))
    lastRInt = RIntString[len(RIntString)-1]
    newRInt = ""
    for rInt in range(len(RIntString)-2):
        newRInt = newRInt + str(rInt)
    newRInt = newRInt + str(bit)

    img.putpixel((coordinate), (int(newRInt), g, b, a))

    if x != width:
        x += 1
    else:
        y += 1
        x = 0

img.save("encoderImage.png")
print("Text successfully encoded into image!")