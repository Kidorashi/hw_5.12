import urllib.request
import re

def MakeSet(text):
    cou=set()
    mas=text.split(' ')
    for word in mas:
        word=word.strip('.,-;(–:")?!')
        for let in word:
            let.lower()
        cou.add(word)
    return cou

def Mnoji(path, mn1, mn2, mn3, mn):
    uniq=set()
    uniq=mn-mn1
    uniq=uniq-mn2
    uniq=uniq-mn3
    fi=open(path, "w", encoding="UTF-8")
    for part in sorted(uniq):
        fi.write(part)
        fi.write('\n')
    fi.close()
    return uniq

def For10(text, x, mas):
    tx=text.split()
    d={}
    for part in x:
        for word in tx:
            if part==word:
                if part in d:
                    mas.append(part)
                else:
                    d[part]=1
    return mas

f=open("C:\\Users\\777\\Desktop\\urls.txt", "r", encoding="UTF-8")
file=f.read()
mas_url=file.split('\n') #в mas_url массив с ссылками
f.close()

url1=mas_url[0]
url2=mas_url[1]
url3=mas_url[2]
url4=mas_url[3] #в переменных отдельные ссылки

url_open=urllib.request.urlopen(url1)
html_text=url_open.read().decode('utf-8')
html_text=str(html_text)
mas=html_text.split('\n')
html_text=''.join(mas)
mas=html_text.split('\t')
html_text=''.join(mas)

res=re.search('<p>(.*?)<p>Фото: Я вижу</p> ', html_text)
if res!=None:
    text1=res.group(1)
    text1=text1.replace('<p>', '')
    text1=text1.replace('</p>', '')
    text1=text1.replace('.', ' ')

url_open=urllib.request.urlopen(url2)
html_text=url_open.read().decode('utf-8')
html_text=str(html_text)
mas=html_text.split('\n')
html_text=''.join(mas)
mas=html_text.split('\t')
html_text=''.join(mas)

res=re.search('<p>(.*?)ЧИТАЙТЕ ТАКЖЕ', html_text)
if res!=None:
    text2=res.group(1) 
    text2=text2.replace('<p>', '')
    text2=text2.replace('</p>', '')
    text2=text2.replace('.', ' ')

url_open=urllib.request.urlopen(url3)
html_text=url_open.read().decode('utf-8')
html_text=str(html_text)
mas=html_text.split('\n')
html_text=''.join(mas)
mas=html_text.split('\t')
html_text=''.join(mas)
res=re.search('</figure><p>(.*?)<p style=', html_text)
if res!=None:
    text3=res.group(1)
    text3=text3.replace('<a href="https://rueconomics.ru/209317-operacii-po-peresadke-glaz-zhdat-ostalos-nedolgo" target="_blank" title="Операции по пересадке глаз - ждать осталось недолго">', '')
    text3=text3.replace('<p>', '')
    text3=text3.replace('</p>', '')
    text3=text3.replace('</a>', '')
    text3=text3.replace('.', ' ')

url_open=urllib.request.urlopen(url4)
html_text=url_open.read().decode('utf-8')
html_text=str(html_text)
mas=html_text.split('\n')
html_text=''.join(mas)
mas=html_text.split('\t')
html_text=''.join(mas)

res=re.search('<p>(.*?)<section class="ok-content-tags">', html_text)
if res!=None:
    text4=res.group(1)
    text4=text4.replace('<a href="https://rueconomics.ru" target="_blank">', '')
    text4=text4.replace('<p>', '')
    text4=text4.replace('</p>', '')
    text4=text4.replace('</a>', '')
    text4=text4.replace('<span>', '')
    text4=text4.replace('</span>', '')
    text4=text4.replace('.', '')
    
mnoj1=set()
mnoj1=MakeSet(text1)
mnoj2=set()
mnoj2=MakeSet(text2)
mnoj3=set()
mnoj3=MakeSet(text3)
mnoj4=set()
mnoj4=MakeSet(text4)

f=open("C:\\Users\\777\\Desktop\\crossings.txt", "w", encoding="UTF-8")
cros=set()
cros=mnoj1&mnoj2&mnoj3&mnoj4

for part in sorted(cros):
    f.write(part)
    f.write('\n')
f.close()

uniq1=set()
a="C:\\Users\\777\\Desktop\\uniq_for_1.txt"
uniq1=Mnoji(a, mnoj2, mnoj3, mnoj4, mnoj1)

uniq2=set()
a="C:\\Users\\777\\Desktop\\uniq_for_2.txt"
uniq2=Mnoji(a, mnoj1, mnoj3, mnoj4, mnoj2)

uniq3=set()
a="C:\\Users\\777\\Desktop\\uniq_for_3.txt"
uniq3=Mnoji(a, mnoj1, mnoj2, mnoj4, mnoj3)

uniq4=set()
a="C:\\Users\\777\\Desktop\\uniq_for_4.txt"
uniq1=Mnoji(a, mnoj1, mnoj2, mnoj3, mnoj4)

massive=[]
massive=For10(text1, uniq1, massive)
massive=For10(text2, uniq2, massive)
massive=For10(text3, uniq3, massive)
massive=For10(text4, uniq4, massive)

f=open("C:\\Users\\777\\Desktop\\notveryuniq.txt", "w", encoding="UTF-8")
for part in sorted(massive):
    f.write(part)
    f.write('\n')
f.close()
