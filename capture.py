import time
import sys

import urllib2
def f_capture(url, tipo):
	archivo_salida= "news//news" +  time.strftime("%Y%m%d%H%M") + tipo + ".txt"
	try:
	
		descarga= urllib2.urlopen(url)
		print ("descargando...",  url)
		#modo b binario w de escritura
		output_file=open (archivo_salida, "wb")
		output_file.write(descarga.read())
		output_file.close()
		print ("Archivo Guardado: %s" % (archivo_salida))
   
	except urllib2.HTTPError, e:
		print( "Error HTTP: ", e.code,url)

	except urllib2.URLError, e:
		print ("Error URL:", e.code, url)

#noticias destacadas
url= "http://news.google.com.ar/news?cf=all&hl=es&pz=1&ned=es_ar&output=rss"
f_capture(url, "all")

#nacional
url= "http://news.google.com.ar/news?cf=all&hl=es&pz=1&ned=es_ar&topic=n&output=rss"
f_capture(url, "n")


#economia
url= "http://news.google.com.ar/news?cf=all&hl=es&pz=1&ned=es_ar&topic=b&output=rss"
f_capture(url, "b")

#Salud
url= "http://news.google.com.ar/news?cf=all&hl=es&pz=1&ned=es_ar&topic=m&output=rss"
f_capture(url, "m")

#Deportes
url= "http://news.google.com.ar/news?cf=all&hl=es&pz=1&ned=es_ar&topic=s&output=rss"
f_capture(url, "s")

#tecnologia
url= "http://news.google.com.ar/news?cf=all&hl=es&pz=1&ned=es_ar&topic=t&output=rss"
f_capture(url, "t")
