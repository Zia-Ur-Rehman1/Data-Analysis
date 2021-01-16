import csv
import matplotlib.pyplot as plt

with open('C:\Python\Gapminder.csv', 'r') as myFile:
    data = list(csv.reader(myFile, delimiter=','))

#converting str data types to float and int
def dataTypeConversion(rawList, dataType):
    convertedList = []
    previousValue = 0
    for item in rawList:
        if item != '':
            convertedList.append(dataType(item))
            previousValue = dataType(item)
        else:
            # replacing missing value with previous value
            convertedList.append(previousValue)
    return convertedList


#Fetch secifc index of given item like for Pakistan
#It will fetch all the row number where Pakistan exits
def fetchIndices(data, columnIndex, searchItem):
    listRowIndices = []

    for i in range(len(data)):
        if data[i][columnIndex] == searchItem:
            listRowIndices.append(i)

    return listRowIndices
#It gives the data of given columnindex 
def fetchColumnData(data, columnIndex, hasHeader):
    listData = []

    for i in range(len(data)):
        listData.append(data[i][columnIndex])
    if hasHeader:
        return listData[1:]
    else:
        return listData


#It fetch the data from 2d_list 
#By passing row and column num to  it
def fetchData(data, columnIndex, listRowIndices):
    listDataValues = []

    for i in range(len(listRowIndices)):
        listDataValues.append(data[listRowIndices[i]][columnIndex])
    return listDataValues


paksitanIndices = fetchIndices(data, 0, 'Pakistan')
years = dataTypeConversion(fetchData(data, 4, paksitanIndices), int)

countries = set(fetchColumnData(data, 0, True))
indicators = data[0][6:]  
country = list(countries)
#making the dictionary for all countries and there indicators
countriesDict = {}
for countryName in countries:
    countryIndices = fetchIndices(data, 0, countryName)
    for indicatorName in indicators:
        countriesDict[(countryName, indicatorName)] = dataTypeConversion(
            fetchData(data, data[0].index(indicatorName), countryIndices), float)


#making a csv file from Dictionary 
#Ranking Code is in project.py file
list_sum = []
indicators.insert(0, 'Country')
with open('mycsv.csv', 'w+', newline='') as f:
    w = csv.writer(f)
    w.writerow(indicators)
    indicators.remove('Country')
    i = 0
    for countryN in countries:
        if(i != 0):
            w.writerow(list_sum)
            list_sum.clear()
        list_sum.append(countryN)
        i = i+1
        for indicatorN in indicators:
            value = (sum(
                countriesDict[(countryN), (indicatorN)])/len(years))
            list_sum.append((value))


with open('mycsv.csv', 'a', newline='') as f:
    w = csv.writer(f)
    w.writerow(list_sum)

