from PIL import Image
import bitarray

endMessage = "11111111"

img = Image.open("encoderImage.png")
width, height = img.size

x = 0
y = 0
bits = 0
bitsArray = []
bytesArray = []
while True:
    if(bits != 8):
        coordinate = (x,y)
        try:
            [r, g, b, a] = img.getpixel(coordinate)
        except: #incase image does not have alpha
            [r, g, b] = img.getpixel(coordinate)
            a = 255
        lastR = list(str(r))
        lastR = lastR[len(lastR)-1]
        bitsArray.append(lastR)
        bits += 1
        if x != width-1:
            x += 1
        else:
            y += 1
            x = 0
    else:
        byte = ''.join(bitsArray)
        if byte == endMessage:
            break
        else:
            bytesArray.append(byte)
            bits = 0
            bitsArray = []

allBitArrayStr = ''.join(bytesArray)
messageDecoded = bitarray.bitarray(allBitArrayStr).tobytes().decode('utf-8')
print("Decoded Message: " + messageDecoded)

    
