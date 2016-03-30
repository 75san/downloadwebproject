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
    
    k = k + 1
    if temp:
        
        js_url=temp[0]
        strs=js_url.split('/')
        filename=strs[len(strs)-1]
        f=urllib.urlopen(js_url)
        data = urllib.urlopen(js_url).read()
        finalpath = savepath + "/" + filename
        jsfile = file(finalpath,"wb")  
        jsfile.write(data)  
        jsfile.close()
def savecssfile(html,savepath):
  if not os.path.exists(savepath):
    os.makedirs(savepath)
  reg = r"""href\s*="?(\S+)\.css""" 
  css = re.compile(reg)
  cslist = re.findall(css,html)
  for i in cslist:
   
   t=i+".css"
   filename = os.path.basename(t)
   finalpath = savepath + "/" + filename
   
   data = urllib.urlopen(t).read()
   cssfile = file(finalpath,"wb")  
   cssfile.write(data)  
   cssfile.close()	
   
  
def downloadImg(html,savepath):
  reg = r"""src\s*="?(\S+)\.jpg""" 
  imgre = re.compile(reg)
  imglist = re.findall(imgre, html)
  for i in imglist:
    t=i+".jpg"
    data = urllib.urlopen(t).read() 
    filename = os.path.basename(t)
    finalpath = savepath +  "/" + filename
    print savepath
    f = file(finalpath,"wb") 
    print finalpath	
    f.write(data)  
    f.close()
  print imglist
def downloadwebp(html,savepath):
  reg = r"""src\s*="?(\S+)\.webp""" 
  imgre = re.compile(reg)
  imglist = re.findall(imgre, html)
  for i in imglist:
    t=i+".webp"
    data = urllib.urlopen(t).read() 
    filename = os.path.basename(t)
    finalpath = savepath +  "/" + filename
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
    
    
    while (1) :
     curtime = time.strftime('%Y%m%d%H%M%S', time.gmtime()) 
     savepath = sys.argv[6] + "/" +curtime
     htm = getHtml(urlad,savepath)
     downloadImg(htm,savepath)
     savejsfile(htm,savepath)
     savecssfile(htm,savepath)
     downloadwebp(htm,savepath)
     time.sleep(int(updatetime))



  
