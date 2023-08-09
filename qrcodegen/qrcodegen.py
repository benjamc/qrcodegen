import qrcode
from PIL import Image
import argparse
import warnings

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-t", type=str, help="Text or url to encode.", default=""
    )
    parser.add_argument(
        "-l", choices=["github", "twitter", "paper", "None"], type=str, help="Logo to add."
    )
    parser.add_argument(
        "-o", type=str, help="Output filename.", default="qrcode.png"
    )
    parser.add_argument(
        "--logo-size", type=float, default=0.22, help="Proportion of logo [0,1]."
    )
    args = parser.parse_args()


    url = args.t  # 'https://github.com/automl/SAWEI'

    if len(url) == 0:
        warnings.warn("Did you provide text/url via the 't' option?")
    
    # taking image which user wants
    # in the QR code center
    if args.l == "github":
        Logo_link = 'icons/github-mark-white.png'
    elif args.l == "twitter":
        Logo_link = 'icons/twitter_black_square.png'
    elif args.l == "None":
        Logo_link = None
    elif args.l == "paper":
        Logo_link = "icons/paper_icon.png"
    else:
        raise ValueError("Please define the logo type via the 'l' option.")
    
    box_size = 10
    box_pixel = 33
    border = 1

    QRcode = qrcode.QRCode(
        box_size=box_size,
        border=border,
        error_correction=qrcode.constants.ERROR_CORRECT_H
    )
    
    
    # adding URL or text to QRcode
    QRcode.add_data(url)
    
    # generating QR code
    QRcode.make()
    
    # taking color name from user
    QRcolor = "Black"  # 'Green'
    
    # adding color to QR code
    QRimg = QRcode.make_image(
        fill_color=QRcolor, back_color="white").convert('RGB')
    
    print("QR Code size:", QRimg.size)

    if Logo_link:
        logo = Image.open(Logo_link)
        
        # adjust image size
        basewidth = int(box_pixel * 3.5)  # int(0.2 * QRimg.size[0])
        basewidth = int(args.logo_size * QRimg.size[0])
        
        print("Logo width:", basewidth)
        wpercent = (basewidth/float(logo.size[0]))
        hsize = int((float(logo.size[1])*float(wpercent)))
        logo = logo.resize((basewidth, hsize)) #, Image.ANTIALIAS)

        # set size of QR code
        pos = ((QRimg.size[0] - logo.size[0]) // 2,
            (QRimg.size[1] - logo.size[1]) // 2)
        QRimg.paste(logo, pos)
    
    # save the QR code generated
    if not args.o:
        raise ValueError("Please provide an output filename via the 'o' option.")
    QRimg.save(args.o)
    
    print('QR code generated!')
    print("Save as", args.o)


