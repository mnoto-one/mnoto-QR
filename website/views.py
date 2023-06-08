import qrcode
import datetime
from PIL import Image
from django.shortcuts import render
from .forms import FormDataForm

# Create your views here.
def home_view(request):
    return render(request, 'theme-i/pages/home.html') 


def generate_qr(request):
    if request.method == 'POST':
        form = FormDataForm(request.POST, request.FILES)
        if form.is_valid():
            form_data = form.save() 
            
            Logo_link = form_data.logo.path
 
            logo = Image.open(Logo_link)
 
            # taking base width
            basewidth = 100
             
            # adjust image size
            wpercent = (basewidth/float(logo.size[0]))
            hsize = int((float(logo.size[1])*float(wpercent)))
            logo = logo.resize((basewidth, hsize), Image.ANTIALIAS)
            QRcode = qrcode.QRCode(
                error_correction=qrcode.constants.ERROR_CORRECT_H
            )
             
            # taking url or text
            url = form_data.text_input
             
            # adding URL or text to QRcode
            QRcode.add_data(url)
             
            # generating QR code
            QRcode.make()
             
            # taking color name from user
            QRcolor = 'Black'
             
            # adding color to QR code
            QRimg = QRcode.make_image(
                fill_color=QRcolor, back_color="white").convert('RGB')
             
            # set size of QR code
            pos = ((QRimg.size[0] - logo.size[0]) // 2,
                   (QRimg.size[1] - logo.size[1]) // 2)
            QRimg.paste(logo, pos)
            timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
            filename = f"media/qr_code_{timestamp}.png"
            QRimg.save(filename)
             
            print('QR code generated!')
            context = {
                'filename' : filename,
            }
            return render(request, 'theme-i/pages/qr_code_generated.html', context=context)

    else:
        form = FormDataForm()

    return render(request, 'theme-i/pages/form_template.html', {'form': form})