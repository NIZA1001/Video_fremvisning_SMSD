import qrcode as qr
print("succ")

url_kvæg = "https://lf.dk/om-os/sektorer-og-sektioner/sektor-for-kvaeg/sammen-mod-salmonella-dublin/"
url_kvæg2 = "https://www.landbrugsinfo.dk/public/a/7/8/tag_smitten_ved_hornene"

image1 = qr.make(url_kvæg)
image1.save("qr-1.png")

image2 = qr.make(url_kvæg2)
image2.save("qr-2.png")
