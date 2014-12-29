from datascrape import scraper
from PIL import Image

class WeatherMap:
	def __init__(self):
		self.MAX=55
		self.MIN=-15
		self.__map=Image.open('map.jpg')
		self.__col=Image.new(self.__map.mode,self.__map.size,(0,0,0))
		self.__data=scraper()
		self.__im=None
	def __temptocolour(self,temp):
		if temp==None:
			return (255,255,255)
		ran=float(self.MAX)
		tm=float(temp)/ran
		b=(1.0-tm)*255
		r=tm*255
		g=0
		color=(r,g,b)
		color=tuple(map(int,color))
		return color
		
	def make(self):
		for city in self.__data.cities:
			#get center
			href,coord,temp=self.__data.cities[city]
			temp=self.__temptocolour(temp)
			xy=(coord[0],coord[1])
			r=int(coord[2]*1.3)
			#paint center
			try:
				self.__col.putpixel(xy,temp)
			except:
				print(type(xy))
				print(xy)
				print(temp)
			#paint circle
			for xn in range(r):
				for yn in range(r):
					if ((xn**2)+(yn)**2)<=r**2:
						try:
							c=(int(xy[0]+xn),int(xy[1]+yn))
							self.__col.putpixel(c,temp)
							c=(int(xy[0]-xn),int(xy[1]-yn))
							self.__col.putpixel(c,temp)
							c=(int(xy[0]+xn),int(xy[1]-yn))
							self.__col.putpixel(c,temp)
							c=(int(xy[0]-xn),int(xy[1]+yn))
							self.__col.putpixel(c,temp)
						except Exception as e:
							print(e)
	def __mix_col(self):
		#simple way to create copy
		im=self.__map.copy()
		#complex way to do it
		X,Y=im.size
		for x in range(X):
			for y in range(Y):
				pix=self.__col.getpixel((x,y))
				if pix!=(0,0,0):
					im.putpixel((x,y),pix)
		#show it
		self.__im=im
	def show(self):
		if self.__im==None:
			self.__mix_col()
		self.__im.show()
	def save(self,path):
		if self.__im==None:
			self.__mix_col()
		self.__im.save(path)
		
if __name__=='__main__':
	w=WeatherMap()
	w.make()
	w.show()
	import datetime
	path=str(datetime.date.today())+'.jpg'
	w.save(path)
			
			
		
