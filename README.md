IndiaTempMap
============
Creates a live map of colour coded temperatures in India.

Data pulled from 
http://imd.gov.in/

Cities with no data uploaded appear white.



Useage
======

import mapgen

Wmap=mapgen.WeatherMap()
Wmap.make()
Wmap.show()
Wmap.save('myfile.jpg')
