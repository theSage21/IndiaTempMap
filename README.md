IndiaTempMap
============
Creates a live map of colour coded temperatures in India.
Red=55 degree Celcius
Blue=0 degree Celcius

Data pulled from 
http://imd.gov.in/

Cities with no data uploaded appear white.  
![Temperature map](2014-12-29.jpg)


Useage
======
    import mapgen

    Wmap=mapgen.WeatherMap()
    Wmap.make()
    Wmap.show()
    Wmap.save('myfile.jpg')

