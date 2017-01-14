import qrcode
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
id='866356-13'
n='(210) 526-0549'
msg='SMSTO:'+str(n)+':'+id
qr.add_data(msg)
qr.make(fit=True)

img = qr.make_image()

img.save('qr.png')
