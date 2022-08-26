import speedtest
import time
import ssl


while True:
	try:
		ssl._create_default_https_context = ssl._create_unverified_context
		st = speedtest.Speedtest()


		download_speed = st.download()
		upload_speed = st.upload(pre_allocate=False)


		print('Download Speed: {:5.2f} Mb'.format(download_speed/(1024*1024)))
		print('Upload Speed: {:5.2f} Mb'.format(upload_speed/(1024*1024)))
		f = open("logspeed.txt",'a+')
		f.write(str(download_speed/(1024*1024))+" "+str(upload_speed/(1024*1024))+"\n")
		f.close()

	except:
		print("Error de conexion con server")
		True
