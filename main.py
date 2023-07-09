import qrcode

imagem_qrcode = qrcode.make("https://www.linkedin.com/in/eik-camargo/")
imagem_qrcode.save("qrcode.png")