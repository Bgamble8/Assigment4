



class Country:
   def __init__(self,name,pop,area,continent):
       self._name = name
       self._pop = pop
       self._area = area
       self._continent = continent
       self._popDensity = round((self._pop/self._area), 2)

   def __repr__(self):
       return self._name + "(pop:" + str(self._pop) + ", size: " + str(self._area) + ") in " + str(self._continent)

   def getName(self):
       return self._name

   def getPopulation(self):
       return self._pop

   def getArea(self):
       return self._area

   def getContinent(self):
       return self._continent

   def setPopulation(self,pop):
       self._pop = pop

   def setArea(self,area):
       self._area = area

   def setContinent(self,continent):
       self._continent = continent


class CountryCatalogue:
    def __init__(self,countryFile):
        self._countryFile = open(countryFile)
        self._countryCat = {}

    def setPopulationOfCountry(self,name,pop):
        



    def findCountry(self,country):
        if country in self._countryCat: