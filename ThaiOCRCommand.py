from parinya import LINE
line = LINE('Gbwdy9oUHXTDDBWqynIC8fLC1qy5EcQUfByh26M82fb')
import os 
import pandas as pd
from pywebio.input import input, FLOAT
from pywebio.output import put_text
from pywebio.output import put_row
from pywebio.output import put_column
import subprocess
import requests
import getpass
from tkinter import Tk
from tkinter import filedialog

#userfile = file_upload('Upload file')

#open(userfile['filename'], 'wb').write(userfile['content'])

#img = file_upload("Select a image:", accept="image/*")

from pywebio.input import *
from pywebio.output import *
from pywebio.session import *
from pywebio.pin import *
from pywebio import start_server

url = 'https://notify-api.line.me/api/notify'

def send_text(token, text):
    LINE_HEADERS = {'content-type':'application/x-www-form-urlencoded','Authorization':'Bearer '+token}
    session_post = requests.post(url, headers=LINE_HEADERS , data = {'message':text})
    print(session_post.text)

'''
def getpath(set_value):
    root = Tk()
    root.withdraw()
    imagepath = filedialog.askopenfilename()
    with popup(''):
        put_buttons(['Upload'], onclick=[lambda: set_value(imagepath)])
    root.destroy()
'''

def main():
    global filename, language, dpi, savefilename, computername, img, imgs, imgspath

    data = input_group("การปรับแต่ง",[
        file_upload("กรุณาเลือกรูปเอกสาร:", name='imgs', accept="image/*", multiple=True),
        #input("กรุณาเลือกรูปเอกสาร:", name='imgs', action=('Select', getpath)),
        select('กรุณาเลือกภาษา', ['tha', 'eng', 'tha+eng'], name='language'),
        input('ขนาด dpi', name='dpi', type=NUMBER),
        input('กรุณาเลือกชื่อไฟล์ที่ต้องการ Save', name='saving')
    ])


    imgs = data['imgs']
    for img in imgs:
        #put_image(img['content'])
        put_image(img['filename'])
    filename = str(img['filename'])


    language = data['language']
    dpi = data['dpi']
    savefilename = data['saving']
    computername = getpass.getuser()
    print(filename)

def webhook():
    if requests.method == 'POST':
        print(requests.json)
        return 200
    
    elif requests.method == 'GET':
        return 'This is method GET', 200

def select_lang(set_value):
    with popup('Select Language'):
        put_buttons(['tha'], onclick=[lambda: set_value('tha')])
        put_buttons(['tha+eng'], onclick=[lambda: set_value('tha+eng')])

def yesno(set_value):
    with popup('Select Yes or No'):
        put_buttons(['Yes'], onclick=[lambda: set_value('Yes')])
        put_buttons(['No'], onclick=[lambda: set_value('No')])

def setting():
    global language, dpi, savefilename, computername
    data = input_group("การปรับแต่ง",[
            input('กรุณาเลือกภาษา', name='language', action=('Select', select_lang), readonly=True),
            input('ขนาด dpi', name='dpi', type=NUMBER),
            input('กรุณาเลือกชื่อไฟล์ที่ต้องการ Save', name='saving')
    ])
    language = data['language']
    dpi = data['dpi']
    savefilename = data['saving']
    computername = getpass.getuser()

def find_file_by_name(file_path):
    for root, dirs, files in os.walk(path):
        if filename in files:
            return os.path.join(root, filename)
            

if __name__=="__main__": 
    put_text("Thai-OCR").style('font-size: 48px')
    dummyvariable1 = 1
    while dummyvariable1 == 1:
        '''
        put_column([
            put_code(main()), None,
            put_code(setting())
        ])
        '''
        main()
        '''
        imgs = file_upload("Select some pictures:", accept="image/*", multiple=True)
        for img in imgs:
            put_image(img['content'])
            put_image(img['filename'])
        '''
        #filename = str(input("Enter file name: "))
        #filename = ("{}".format(print(img['filename'])))
        #str(filename)
        #filename()


        path = os.getcwd()

        file_path = find_file_by_name(filename)


        '''
        data = input_group("การปรับแต่ง",[
            input('กรุณาเลือกภาษา', name='language', action=('Select', select_lang), readonly=True),
            input('ขนาด dpi', name='dpi', type=NUMBER),
            input('กรุณาเลือกชื่อไฟล์ที่ต้องการ Save', name='saving')
        ])
        language = data['language']
        dpi = data['dpi']
        savefilename = data['saving']
        computername = os.environ.get('USERNAME')
        '''
        

        subprocess.call(r'tesseract -l {} --dpi {} {} C:\Users\{}\Downloads\{}'.format(language, dpi, file_path, computername, savefilename), shell=True)
        

            
        answer = str(input("คุณต้องการ Share เอกสารลง Line หรือไม่: ", action=('Select', yesno), readonly=True))
        answer = answer.lower()
        if answer == "yes":
            print("234")
            filepath1 = r"C:\Users\{}\Downloads\{}.txt".format(computername, savefilename)

            f = open(filepath1, "r", encoding='utf8')
                
            xx = 1
            while xx == 1:
                try:
                    line = f.readline()
                except UnicodeDecodeError:
                    #f.close()
                    encodeing = 'TIS-620'
                    break
                if not line:
                    #f.close()
                    encoding = 'utf8'
                    break

            with open(filepath1, "r", encoding=encoding) as f:
                string1 = f.read()

            token = 'Gbwdy9oUHXTDDBWqynIC8fLC1qy5EcQUfByh26M82fb'
            text = string1
            msg = send_text(token, text)
            print(msg)

            #textscan = requests.get(string1).text
            #line.sendtext(string1)  
            #line.sendtext('{}'.format(string1))
            
            continue
        elif answer == "no":
            continue
        else:
            print("ตอบ Yes หรือ No เท่านั้น")

        '''
        cont = str(input("ต้องการใช้ต่อหรือไม่", action=('Select', yesno), readonly=True))
        cont = cont.lower()
        if cont == "yes":
            continue
        elif cont == "no":
            break
        '''
