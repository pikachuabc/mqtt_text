import base64
import os

base64_data= base64.b64encode(open('chuanganqi.jpg','rb').read())
print(base64_data)

img_data = base64.b64decode(base64_data)
file = open('1.jpg','wb')
file.write(img_data)
file.close()




