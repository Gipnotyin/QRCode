import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.colormasks import RadialGradiantColorMask


def GenerateQRcode(vin_number: str, host: str = "localhost", port: str = "8080") -> StyledPilImage:
    qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_L)
    qr.add_data('https://{}:{}/{}'.format(host, port, vin_number))

    img = qr.make_image(image_factory=StyledPilImage, color_mask=RadialGradiantColorMask())
    img.save("generate/generated_img/{}.png".format(vin_number))
    return img
