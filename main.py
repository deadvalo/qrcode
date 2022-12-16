import os

import qrcode
import argparse
import cv2
import pyzbar.pyzbar as pyzbar
from selenium import webdriver
'''
    This script generates a QR code from a given string.
    execute the script with the following command:
        python main.py -i https://tracker.gg/valorant/profile/riot/dead%202%234444/overview
        pyhton main.py -t file.txt
'''
#set up the argument parser
parser = argparse.ArgumentParser(description='Generate QR code')
parser.add_argument('-i','--link', help='Link to be encoded')
parser.add_argument('-t','--text', help='Text to be encoded')
#parse the arguments
args = parser.parse_args()



def create_qr_code(data):
    '''
    This function creates a QR code from the given data
    :param data:
    :return:
    '''
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save("qr.png")


def read_qr_code(qr_code):
    '''
    This function reads a QR code from an image
    :return:
    '''
    #read the image
    image = cv2.imread(qr_code)

    #decode the image
    decodedObjects = pyzbar.decode(image)

    #print the data
    return decodedObjects[0].data.decode("utf-8")

def read_using_camera():
    '''
    This function reads a QR code from the camera
    :return:
    '''
    #initialize the camera
    cap = cv2.VideoCapture(0)

    while True:
        #read the image
        _, image = cap.read()

        #decode the image
        decodedObjects = pyzbar.decode(image)

        #print the data
        for obj in decodedObjects:
            print("Data", obj.data)

        #display the image
        cv2.imshow("Frame", image)
        #press a key to exit
        key = cv2.waitKey(1)
        if key == 27: #esc key
            break
    #release the camera
    cap.release()
    #close all the windows
    cv2.destroyAllWindows()

def screenshot_link(link):
    '''
    This function takes a screenshot of a given link
    :param link:
    :return:
    '''
    driver = webdriver.Firefox()
    driver.get(link)
    driver.save_screenshot('screenshot.png')
    driver.quit()

if __name__ == '__main__':
    # open the text file
    if args.text:
        with open(args.text, 'r') as f:
            data = f.read()
    elif args.link:
        data = args.link
    else:
        print('No data to encode')
        exit()

    create_qr_code(data)
    image = os.path.join(os.getcwd(), 'qr.png')
    print(read_qr_code(image))

    #read using the camera
    #read_using_camera()

    #screenshot a link
    if args.link:
        screenshot_link(args.link)

