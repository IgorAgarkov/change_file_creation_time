# -*- coding: utf8 -*-
import os
import pywintypes, win32file, win32con
from datetime import datetime
from PIL import Image  # , ExifTags

def changeFileCreationTime(fname, newtime):
    wintime = pywintypes.Time(newtime)
    winfile = win32file.CreateFile(
        fname, win32con.GENERIC_WRITE,
        win32con.FILE_SHARE_READ | win32con.FILE_SHARE_WRITE | win32con.FILE_SHARE_DELETE,
        None, win32con.OPEN_EXISTING,
        win32con.FILE_ATTRIBUTE_NORMAL, None)

    win32file.SetFileTime(winfile, wintime, None, None)

    winfile.close()

path = 'D:/tmp/Компас_backup/D/tmp/фланец 320х600.cdw'

tuch_time = os.path.getmtime(path)
create_time = os.path.getctime(path)

print('время изменения файла:', datetime.fromtimestamp(tuch_time))
print('время создания файла:', datetime.fromtimestamp(create_time))

new_time = 500000000
accessed_time = new_time
modified_time = new_time

changeFileCreationTime(path, int(new_time))     # меняем время создания файла
os.utime(path, (accessed_time, modified_time))  # меняем время обращения и время изменения файла

tuch_time = os.path.getmtime(path)
create_time = os.path.getctime(path)

print('новое время изменения файла:', datetime.fromtimestamp(tuch_time))
print('новое время создания файла:', datetime.fromtimestamp(new_time))





# читаем exif из фото
# img = PIL.Image.open('img.jpg')
# exif_data = img._getexif()