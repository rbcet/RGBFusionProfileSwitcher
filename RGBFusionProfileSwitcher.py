import os
import subprocess

RGB_FUSION_PATH = 'C:/Program Files (x86)/GIGABYTE/RGBFusion/'

os.system("taskkill /F /IM RGBFusion.exe")

os.rename(RGB_FUSION_PATH + 'Pro1.xml', RGB_FUSION_PATH + 'Pro1.xml.old') 
os.rename(RGB_FUSION_PATH + 'ExtPro1.xml', RGB_FUSION_PATH +  'ExtPro1.xml.old')

os.rename(RGB_FUSION_PATH + 'Pro2.xml.old', RGB_FUSION_PATH + 'Pro1.xml') 
os.rename(RGB_FUSION_PATH + 'ExtPro2.xml.old', RGB_FUSION_PATH + 'ExtPro1.xml')

os.rename(RGB_FUSION_PATH + 'Pro1.xml.old', RGB_FUSION_PATH + 'Pro2.xml.old')
os.rename(RGB_FUSION_PATH + 'ExtPro1.xml.old', RGB_FUSION_PATH + 'ExtPro2.xml.old')

subprocess.Popen(["cmd.exe", "/c", RGB_FUSION_PATH + "Check_Kill.exe"], creationflags=0x08000000)
