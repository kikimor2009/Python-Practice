import requests

download_link = 'https://stepic.org/media/attachments/course67/3.6.3/'
filename = '699991.txt'
while filename:
    print(filename)
    r = requests.get(download_link + filename)
    filename = None if r.text.startswith('We') else r.text
ouf = open('out.txt', 'w')
ouf.write(r.text)
ouf.close()
