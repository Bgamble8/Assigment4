
class Country:
    def __init__(self,name,pop,area,continent):
        self._name = name
        self._pop = pop
        self._area = area
        self._continent = continent 

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
        self._countryFile = open(countryFile,"r")
        self._countryCat = {}
        self._countryList = []
        self._countryFile.readline()
        for line in self._countryFile:
            line = line.replace("\n","")
            line = line.split("|")
            temp = Country(str(line[0]),str(line[2]),str(line[3]),str(line[1]))
            self._countryCat[line[0]] = temp
            self._countryList.append(temp)
 
    def setPopulationOfCountry(self,name,pop):
    	if name in self._countryCat:
    		self._countryCat[name].setPopulation(pop)

    def setAreaOfCountry(self,name,area):
        if name in self._countryCat:
            self._countryCat[name].setArea(area)
        else:
            print("Country not in database")

    def setContinentOfCountry(self,name,continent):
        if name in self._countryCat:
            self._countryCat[name].setContinent(continent)
        else:
            print("Country not in database")
    
    def findCountry(self,name):
        if name in self._countryCat:
        	return self._countryCat[name]
        else:
            None

    def addCountry(self,countryName,pop,area,cont):
        if countryName not in self._countryCat:
            self._countryCat[countryName] = Country(countryName,pop,area,cont)
            return True
        else:
            return False


    def printCountryCatalogue(self):
        for i in self._countryCat:
            print(self._countryCat[i])




    def saveCountryCatalogue(self,fname):
        self._fname = open(fname,"w")
        self._fname.write("Country|Continent|Population|Area\n")
        for i in self._countryCat:
            self._fname.write(str(self._countryCat[i].getName()) + "|" + str(self._countryCat[i].getContinent()) + "|" + str(self._countryCat[i].getPopulation()) + "|" + str(self._countryCat[i].getArea())  + "\n")


test = CountryCatalogue("data.txt")
test.saveCountryCatalogue("test.txt")