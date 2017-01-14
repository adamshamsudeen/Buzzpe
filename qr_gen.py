import qrcode
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data('866356-13')
qr.make(fit=True)

img = qr.make_image()

img.save('qr.png')
