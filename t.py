from functools import partial
import os,time,subprocess
from Tkinter import *
os.system("sudo pip install youtube-dl")
time.sleep(3);
def status():
	fileBytePos = 0
	while True:
		#print 'gandu'
    		inFile = open('fdata.txt','r')
    		inFile.seek(fileBytePos)
    		data = inFile.read()
    		print data
    		fileBytePos = inFile.tell()
    		#print fileBytePos
    		inFile.close()
    		time.sleep(1)
		if '100' in data:
			break
def login():
   
   master = Tk()
   
   def gg(x):
	s = e1.get()
	l = 'youtube-dl -f '+str(x)+' '+s+' >fdata.txt'
	#subprocess.call(['python', 'don.py'],shell=False)
	os.system(l)
	os.system("gnome-terminal")
	os.system("python don.py")
	#status()
	
        
   def plot_graph():
    Label(master, text="-------------------------").grid(row=6)
    Label(master, text="Choose the quality of video that you wish to download").grid(row=8)
    s = e1.get()
    l = 'youtube-dl -F '+s+' >fname'
   
    os.system(l)
    
    file = open('fname')
    ss = file.readlines()[::-1]
    i = 0
    
    while i<4:
        temp = ss[i]
        temp = temp.split()
        action_with_arg = partial(gg,temp[0])
        Button(master, text=temp[1]+" "+temp[2], command= action_with_arg).grid(row=9+i)
	#print temp[1]
        i = i+1
	
   
   
  
   master.title('Youtube Downloader Beta')
   Label(master, text="Welcome folks!").grid(row=2, column=0, columnspan=4, rowspan=1,sticky=W+E+N+S, padx=5, pady=5)
   Label(master, text="Enter the link of the video:").grid(row=4)
   e1 = Entry(master)
   e1.grid(row=4, column=1)
   Button(master, text='Exit', command=master.quit).grid(row=12, column=3, sticky=W,)
   Button(master, text='Download', command=plot_graph).grid(row=14, column=3, sticky=W, pady=4)

login()
mainloop( )

