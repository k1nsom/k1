import requests
import re
def main(url):
    html=requests.get(url)
    regrule1='src=".*?.jpg'
    regrule2='src=".*?.png'
    regrule3='src=".*?.gif'
    regrule4='src=".*?.mp3'
    imgre1=re.compile(regrule1)
    imgre2=re.compile(regrule2)
    imgre3=re.compile(regrule3)
    imgre4=re.compile(regrule4)
    urls1=imgre1.findall(html.text)
    urls2=imgre2.findall(html.text)
    urls3=imgre3.findall(html.text)
    urls4=imgre4.findall(html.text)
    x1=0
    print(urls2,urls3)
    for key1 in urls1:
         spli1 = re.split('src="', key1)
         flo=requests.get(spli1[1])
         filename='c:/kinsom 2022 9/python 2022 autumn/img/%d.jpg'%x1
         f1=open(filename,'wb')
         filesize=f1.write(flo.content)
         print(filename,filesize,'Bytes')
         x1+=1
    x2 = 0
    for key2 in urls2:
        spli2 = re.split('src="', key2)
        flo = requests.get(url + spli2[1])
        filename = 'c:/kinsom 2022 9/python 2022 autumn/img/%d.png' % x2
        f1 = open(filename, 'wb')
        filesize = f1.write(flo.content)
        print(filename, filesize, 'Bytes')
        x2 += 1
    x3 = 0
    for key3 in urls3:
        spli3 = re.split('src="', key3)
        flo = requests.get(url + spli3[1])
        filename = 'c:/kinsom 2022 9/python 2022 autumn/img/%d.gif' % x3
        f1 = open(filename, 'wb')
        filesize = f1.write(flo.content)
        print(filename, filesize, 'Bytes')
        x3 += 1
    x4 = 0
    for key4 in urls3:
        spli3 = re.split('src="', key4)
        flo = requests.get(url + spli3[1])
        filename = 'c:/kinsom 2022 9/python 2022 autumn/img/%d.mp3' % x4
        f1 = open(filename, 'wb')
        filesize = f1.write(flo.content)
        print(filename, filesize, 'Bytes')
        x4 += 1
    f1.close()
main('http://www.taobao.com')
main('http://www.nipic.com')