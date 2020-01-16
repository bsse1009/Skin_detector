from PIL import Image

ratio = [[[0 for k in range(256)] for j in range(256)] for i in range(256)]

with open("./traindata.txt", "r") as file:
  for i in range(256):
    for j in range(256):
      for k in range(256):
        probability = file.readline()
        ratio[i][j][k] = float(probability)
print('data collected!')

image = Image.open("0004.jpg")
im = image.convert('RGB')
width, height = im.size

im2 = Image.new(im.mode, im.size)

skinPercentage = 0;
nonSkinPercentage = 0;

for y in range(height):
  for x in range(width):
    red, green, blue = im.getpixel((x, y))
    if(ratio[red][green][blue] > .25):
      im2.putpixel((x, y), (250, 250, 250))
      skinPercentage += 1
    else:
      im2.putpixel((x, y), (0, 0, 0))
      nonSkinPercentage += 1
  print("*", end="")
print("")
total = skinPercentage+nonSkinPercentage
skinPercentage = (skinPercentage*100)/total
nonSkinPercentage = (nonSkinPercentage*100)/total

print("Skin percentage : " ,skinPercentage,"non skin percentage : " , nonSkinPercentage)

im2.save("D:\\5th Semester\\DBMS2\\detected.jpg")