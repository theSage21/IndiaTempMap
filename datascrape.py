import pickle
import requests
import datetime
from bs4 import BeautifulSoup

class scraper:
	def __init__(self):
		self.cities={}
		self.run()
	def __get_from_internet(self):
			"GETS data from internet"
			#get the main page
			print('Getting list of cities')
			page=requests.get('http://www.imd.gov.in/')
			#get city links from page
			soup=BeautifulSoup(page.text)
			#get city details
			print('Getting temperatures for cities.')
			for city in soup.find_all('area'):
				name=city['title']
				href=city['href']
				coord=city['coords']
				try:
					coord=list(map(int,coord.split(',')))
				except:
					print(coord)
					coord=(0,0)
				#get exception of delhi
				if len(coord)>3:
					coord=coord[:3]
					coord[2]=10
				#get temperatures for today.
				try:
					tempsoup=BeautifulSoup(requests.get(href).text)
					temp=tempsoup.body.center.font.table.tr.table.contents[3].contents[3].text.strip()
					temp=eval(temp)
				except Exception as e:
					#print(e)
					print(name,' Has not yet put up data.')
					temp=None
				#assign data
				self.cities[name]=[href,coord,temp]
			#set date
			date=str(datetime.date.today())
			#save to file
			print('Saving to file')
			f=open('cities.data.'+date,'wb')
			pickle.dump(self.cities,f)
			f.close()
			print('Done')
	def run(self):
		"Runs the scraper"
		#check if data on disk
		date=str(datetime.date.today())
		try:
			f=open('cities.data.'+date,'rb')
		except:
			self.__get_from_internet()
		else:
			print('Loading from file')
			self.cities=pickle.load(f)
			f.close()
			print('Done')
if __name__=='__main__':
	s=scraper()
		
