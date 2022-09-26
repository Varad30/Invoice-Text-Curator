import os,cgi

print('content-type:text/html\r\n\r\n')
 

form = cgi.FieldStorage()
pn=form['filename']

pf=os.path.basename(pn.filename)
open("/Users/varadunhale/Desktop/VOIS/"+pf,"wb").write(pn.file.read())

# print('<html>')
# print('<body>,<center>')

print('</center></body></html>')