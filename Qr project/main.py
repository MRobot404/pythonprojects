#Import python module
import qrcode

#In data you will type your message
data="Gracias por cumplir los 10 hermosos meses mi amorcito lindo <3<3<3, te amooooooo <3<3<3"

img=qrcode.make(data=data)
#Save Code
img.save("Mensaje secreto.png")