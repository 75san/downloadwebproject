#!/usr/bin/python
# FileName :main.py
import urllib
import os
import re
import shutil
import sys
import time
def getHtml(url,savepath):
  page = urllib.urlopen(url)
  html = page.read()
  if not os.path.exists(savepath):
    os.makedirs(savepath)
  finalpath = savepath + "/index.html"
  htmlfile  = file(finalpath,"wb")
  htmlfile.write(html)
  htmlfile.close()
  return html
def savejsfile(html,savepath):
  if not os.path.exists(savepath):
    os.makedirs(savepath)
  js_url_pattern=r'.+?src="(\S+)"'
  r=re.compile(r'<script[^>].*?</script>',re.DOTALL)
  temp=[1]
  k = 1
  for js in r.findall(html):
    temp = re.findall(js_url_pattern,js)
    finalpath = savepath + "/" + str(k) + ".js"
    k = k + 1
    if temp:
        js_url=temp[0]
        strs=js_url.split('/')
        filename=strs[len(strs)-1]
        f=urllib.urlopen(js_url)
        data = urllib.urlopen(js_url).read()
        jsfile = file(finalpath,"wb")  
        jsfile.write(data)  
        jsfile.close()
def savecssfile(html,savepath):
  if not os.path.exists(savepath):
    os.makedirs(savepath)
  reg = r"""href\s*="?(\S+)\.css""" 
  css = re.compile(reg)
  cslist = re.findall(css,html)
  k = 1
  for i in cslist:
   
   t=i+".css"
   finalpath = savepath + "/" +str(k) + ".css"
   k = k + 1
   
   data = urllib.urlopen(t).read()
   cssfile = file(finalpath,"wb")  
   cssfile.write(data)  
   cssfile.close()	
   
  
def downloadImg(html,savepath):
  reg = r"""src\s*="?(\S+)\.jpg""" 
  imgre = re.compile(reg)
  imglist = re.findall(imgre, html)
  k=0
  for i in imglist:
    t=i+".jpg"
    k = k + 1
    data = urllib.urlopen(t).read() 
    finalpath = savepath +  "/" + str(k) +".jpg"
    print savepath
    f = file(finalpath,"wb") 
    print finalpath	
    f.write(data)  
    f.close()
  print imglist
if __name__ == '__main__':
 
    if len(sys.argv)!=7:
     print "python main.py -d 60 -u http://m.sohu.com -o /tmp/backup"
     exit()
    updatetime = sys.argv[2]
    urlad = sys.argv[4]
    curtime = time.strftime('%Y%m%d%H%M%S', time.gmtime()) 
    savepath = sys.argv[6] + "/" +curtime
    print savepath
    if not os.path.exists(savepath):
      os.makedirs(savepath)
    while (1) :
     htm = getHtml(urlad,savepath)
     downloadImg(htm,savepath)
     savejsfile(htm,savepath)
     savecssfile(htm,savepath)
     time.sleep(int(updatetime))
 

  
