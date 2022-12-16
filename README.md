# QR Code Generator and Reader

This project allows you to generate QR codes from a link or a text, as well as read QR codes through a camera or an image file. It also includes a feature to take a screenshot of the page if the QR code is a link.
# Requirements

The following packages are required to run this project:

    
    Pillow
    OpenCV
    Pyzbar

You can install these packages by running the following command:

    pip install -r requirements.txt


# Running the code

To run the code, navigate to the project directory and run the following command:

    python main.py -i url 
or
    
    pyhton main.py -t file.txt

This will launch the QR code generator and reader application. You can then follow the prompts to generate a QR code from a link or text, or to read a QR code through a camera or an image file.
# Screenshots

The application includes a feature to take a screenshot of the page if the QR code is a link. To use this feature, simply scan a QR code that contains a link and the application will automatically take a screenshot of the page. The screenshot will be saved in the project directory with the filename screenshot.png.
# Additional notes
To read QR codes through the camera, you will need a webcam connected to your computer.
The OCR functionality used to read QR codes from image files is based on the pytesseract package, which uses Tesseract OCR under the hood. Make sure that Tesseract is installed and properly configured on your system in order to use this feature.
