import os
import shutil

path = 'C:/Users/net/Desktop/Mohit Gupta/Coding/phyton/bin'

folders = {
    "Images": ['.jpg', '.jpeg', '.png', '.gif', '.tiff', '.bmp', '.bpg', '.svg', '.helif', '.psd'],

    "Docs": ['.pdf', '.rtf', '.docx', '.pptx', '.pptm', '.ppt', '.oxps', '.epub', '.pages', '.doc', '.fdf', '.ods', '.odt', '.pwi', '.xsn', '.xps', '.dotx', '.docm', '.dox', '.rvg', '.rtf', '.rtfd', '.wpd', '.xls', '.xlsx'],

    "Coding": ['.html', '.htm', '.shtml', '.xhtml', '.js', '.css', '.py', '.php'],

    "Video": ['.mp4', '.avi', '.flv', '.wmv', '.mov', '.webm', '.vob', '.mng', '.qt', '.mpg', '.mpeg', '.3gp'],

    "Plain Text": ['.txt', '.in', '.out'],

    "Audio": ['.mp3'],

    "Application": ['.exe', '.apk'],

    "webpages": ['.mhtml', '.chm'],

    "Archives": ['.zip', '.a', '.ar', '.cpio', '.iso', '.tar', '.gz', '.rz', '7z', '.dmg', '.rar', '.xar']
}

html = '<!DOCTYPE html><html lang="en"><head><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>File Arranger</title><style>:root {--bs-font-sans-serif: system-ui,-apple-system,"Segoe UI",Roboto,"Helvetica Neue",Arial,"Noto Sans","Liberation Sans",sans-serif,"Apple Color Emoji","Segoe UI Emoji","Segoe UI Symbol","Noto Color Emoji";}a{text-align: center;display: inherit;text-decoration: none;color: #6495ed;}table{width: 90%;margin-left: auto;margin-right: auto;margin-bottom: 1rem;color: #212529;vertical-align: top;border-color: #dee2e6;box-shadow: 0 .125rem .25rem rgba(0,0,0,.075)!important}td{padding: 20px 26px;border-width: 0 1px;text-align: center;}h1{margin-top: 0;margin-bottom: .5rem;font-weight: 500;line-height: 1.2;}div{text-align: center;padding-top: 20px;}p{margin-top: 0;margin-bottom: 1rem;}body {margin: 0;font-family: var(--bs-font-sans-serif);font-size: 1rem;font-weight: 400;line-height: 1.5;color: #212529;background-color: #fff;-webkit-text-size-adjust: 100%;-webkit-tap-highlight-color: #0000;}</style></head><body><div><h1>FILE ARRANGER</h1><p>Here is complete list of files</p></div><table><tr><td>Name</td><td>Folder</td></tr>'
more_html = ''

def create_if_not_exist(x):
    list1 = os.listdir(path)
    if x not in list1:
        os.makedirs(x)

files = os.listdir(path)
files.remove('main.py')

def present_file():
    global more_html
    for x in folders:
        for y in files:
            name, exe = os.path.splitext(y)
            if exe in folders[x]:
                create_if_not_exist(x)
                shutil.move(y, x)
                more_html += '<tr><td>'+name+'</td><td>'+x+'</td></tr>' 

def others():
    global more_html
    newfiles = os.listdir(path)
    newfiles.remove('main.py')
    for y in newfiles:
        if os.path.isdir(y):
            continue
        elif y != '':
            create_if_not_exist('others')
            shutil.move(y, 'others')
            more_html += '<tr><td>'+y+'</td><td>Othes</td></tr>' 
        else:
            continue

present_file()
others()

with open('logs.html' ,'w') as f:
    f.write(html+more_html+'<a href=''>Fork on github</a></body></html>')