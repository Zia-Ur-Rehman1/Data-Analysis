import csv
import matplotlib.pyplot as plt
import functions
print("\t\t\t\tProject Created By Zia-Ur-Rehman")
        #First Thing is That I have Created My Own File OF CSV
        #The Reason Was That I have To Check Whether My Program Is Wroking Well And Gving All the Data OR Not
        #I have also Created A list And A Dictionary instead of File(That code will be provided At the End of File)
        #It Cotains Country Names And Average Sum of All max_values[i] Indicator
        #Check The (mycsv) File and You will get the Idea Of It
with open('C:\Python\Aoa\Project\mycsv.csv', 'r', newline='') as f:
    mydata = list(csv.reader(f, delimiter=','))


    	    #It Takes List OF File and A Column Index From Which It Access Data
            #Data Is A List Extracted from (mycsv) File
            #Column Index is the column form whihc data is fetched
def fetchColumnData(mydata, columnIndex, hasHeader):
    listData = []
    for i in range(0, len(mydata)):
        listData.append(mydata[i][columnIndex])
    if hasHeader:
        return listData[1:]
    else:
        return listData


                    #Storing All The Countries Name In A List#
                    #In Previous File We Have To USe set Becasue Of Repetition Of Names
                    #This file contains avg sum of all max_values[i] 
                    #So There is no Repetition
countries = list(fetchColumnData(mydata, 0, True))
max_values = []
min_values = []
                    #Getting Minimum and Maximum Values
                    #That I Stored At Creating This File
min_values = mydata[228][0:]
max_values = mydata[229][0:]
                    #Removing Them From Countries List 
                    # As They Are Not Required
countries.remove('Max')
countries.remove('Min')

indicators = mydata[0][1:]
countriesDict = {}

country_index = 0
indicator_index = 0
for countryName in countries:
    #This 0 will start the indicator  index from start for each country
    indicator_index = 0 
    #First Row Contain only Headers That's why move to next row
    country_index += 1 
    for indicatorName in indicators:
        indicator_index += 1 
        value = mydata[country_index][indicator_index]
        countriesDict[(countryName, indicatorName)] = value

rank_by_indicator = {}
                     ####     Creating A Dictionary rank_by_indicator ###########
                     #####    Cheecking Good And Bad Indicators And Giving Them Ranks ###
                     ####     Storing Them In rank_by_indicator #####
for country_name in countries:
    i = 1
    for indicator in indicators:
        obj_value = float(countriesDict[(country_name), (indicator)])
        res = float((obj_value/float(max_values[i])*101))
        rank_by_indicator[(country_name), (indicator)] = res
        i = i+1
                ##### Giving A Total Rank to A Country By Adding All Indicators Rank    #####
                #### Storing Them In total_rank_Dict={}
total_rank_Dict={}
for i in countries:
    total=0
    for j in indicators:
        total+=rank_by_indicator[(i),(j)]
    total_rank_Dict[(i)]=total

                ####### Top 10 Countries######   
print("Top 10 Countries ")                 
functions.Top(total_rank_Dict)                    
                    
                        #Printing Sorted Dictionary By Rank In Decending Order #####
# Funtions.py has Rank_Sort Funtions give him a Dictonary It will sort it by Value to Descending Order
#Now It has modified To Get Rank Of Specific Country
print("Pakistan Rank In World")                 
country_name='Pakistan'
functions.Rank_Sort(total_rank_Dict,country_name)
while True:
    check=int(input("\n\tIf you want to check Rank of Any Country:\n Press (1) else Press (0):"))
    if(check==1):
        country_name=str(input("Enter Country You Want To Check Rank In World:")) 
        functions.Rank_Sort(total_rank_Dict,country_name)
    else:
        break    
                                #Converting a sorted Dict Into List
                               # This will help to check FIrst 10 or last 10 Countries In The Dictionary Alphabetically

# zia=list(sorted(total_rank_Dict.keys()))[-10:]
# print(zia)
# for x in zia:
#     functions.Rank_Sort(total_rank_Dict,x)


                # This Will Check The Conditions Of indicators 
                # Whether It Is In Best Good Bad Or Worst Condition For A secific Country
                # This Will Help Us to Prove The Reason
                # Pakistan Aesa Q Hy
country_name=''
country_name=input("\nEnter Country Name You Want To Check Indicators For:") 
good_indicators={}
bad_indicators={}
best_indicators={}
worst_indicators={}
for indi in indicators:
    value=rank_by_indicator[(country_name),(indi)]
    if indi in ("Taxrevenue","YearlyCO2emission", "Urbanpopulationgrowth", "Trafficdeaths", "Suicideage15to29", "Residentialelectricityuseperperson", "Ratioofgirlstoboysinprimaryandsecondaryeducation", "Poverty", "Populationdensity", "Populationtotal", "Populationgrowth", "Oilconsumptionperperson", "Murderedwomen", "Murderedmen","Murder", "Ratioofgirlstoboysinprimaryandsecondaryeducation","Longtermunemploymentrate", "Femalesaged25to54labourforceparticipationrate","Literacyrateyouthtotal", "Inflation", "Infantmortality", "Imports", "EnergyUsePerPerson", "CO2Emissions", "ChildrenPerWoman"):
        if (value>=70):
            worst_indicators[(country_name),(indi)]='Worst'
        elif(value >=50 and value<70):
            bad_indicators[(country_name),(indi)]='Bad'
        elif(value>=20 and value<50):
            good_indicators[(country_name),(indi)]='Good'
        elif(value>=-3 and value<20):
            best_indicators[(country_name),(indi)]='Best'    
    else:
        if (value>=50):
            best_indicators[(country_name),(indi)]='Best'
        elif(value >=0 and value<50 ):
            good_indicators[(country_name),(indi)]='Good'
        elif(value>=-150 and value<0):
            bad_indicators[(country_name),(indi)]='Bad'
        elif(value>=-221 and value<-150):
            worst_indicators[(country_name),(indi)]='Worst'

#                      #this is converting a sorted deictonray into list and getting its first 10 elements  
# #print(list(sorted(total_rank_Dict.keys()))[:10])
#                     #this is converting a sorted deictonray into list and getting its last 10 elements  
# #print(list(sorted(total_rank_Dict.keys()))[-10:])


print('\nIf Bad Indicators Are Low They Are IN Best Condtiton')
print('If Good Indicators Are High They Are IN Best Condtiton')
print('\n')
print("Enter The Indicators Condition You Want To Check")
check=str(input("Option Best/Good/Bad/Worst:"))
if(check=='best' or check =='Best'):
    print('\n')
    print("Indicators Which Are In Best Conditions In",country_name)
    for k,v in best_indicators.items():
        print("\t","\t")
        print(k,v)
elif(check=='good' or check =='Good'):
    print('\n')
    print("Indicators Which Are In Good Conditions In",country_name)

    for k,v in good_indicators.items():
        print("\t","\t")
        print(k,v)

elif(check=='bad' or check =='Bad'):
    print('\n')
    print("Indicators Which Are In Bad Conditions In",country_name) 

    for k,v in bad_indicators.items():
        print("\t","\t")
        print(k,v)
elif(check=='worst' or check =='Worst'):
    print('\n')
    print("Indicators Which Are In Worst Conditions In",country_name)

    for k,v in worst_indicators.items():
        print("\t","\t")
        print(k,v)

print("Number of Best Indicators:",len(best_indicators))  

print("Number of Good Indicators:",len(good_indicators))  

print("Number of Bad Indicators:",len(bad_indicators))  

print("Number of Worst Indicators:",len(worst_indicators))  



##############                      Graphical Resppresentation              ##############

for indicatorName in indicators:
    plt.figure()
    if indicatorName in ("Taxrevenue","YearlyCO2emission", "Urbanpopulationgrowth", "Trafficdeaths", "Suicideage15to29", "Residentialelectricityuseperperson", "Ratioofgirlstoboysinprimaryandsecondaryeducation", "Poverty", "Populationdensity", "Populationtotal", "Populationgrowth", "Oilconsumptionperperson", "Murderedwomen", "Murderedmen","Murder", "Ratioofgirlstoboysinprimaryandsecondaryeducation","Longtermunemploymentrate", "Femalesaged25to54labourforceparticipationrate","Literacyrateyouthtotal", "Inflation", "Infantmortality", "Imports", "EnergyUsePerPerson", "CO2Emissions", "ChildrenPerWoman"):
            
        plt.plot([-3,101],[-3,rank_by_indicator[(
            'Pakistan', indicatorName)]], 'green', label="Pakistan")
        plt.plot([-3,101],[-3, rank_by_indicator[(
            'India', indicatorName)]], 'red', label="India")
        plt.plot([-3,101],[-3, rank_by_indicator[(
            'United States of America', indicatorName)]], 'blue', label="USA")
        plt.plot([-3,101],[-3, rank_by_indicator[(
            'China', indicatorName)]], 'black', label="China")
        plt.plot([-3,101],[-3, rank_by_indicator[(
            'Somalia', indicatorName)]], 'orange', label="Somalia")
        plt.plot([-3,101],[-3, rank_by_indicator[(
            'Bangladesh', indicatorName)]], 'yellow', label="Bangladesh")
        plt.plot([-3,101],[-3, rank_by_indicator[(
            'United Kingdom', indicatorName)]], 'cyan', label="UK")
        plt.plot([-3,101],[-3, rank_by_indicator[(
            'Norway', indicatorName)]], 'magenta', label="Norway")
        plt.title(indicatorName)
    else:
        plt.plot([-221,101],[-200, rank_by_indicator[(
            'Pakistan', indicatorName)]], 'green', label="Pakistan")
        plt.plot([-221,101],[-200, rank_by_indicator[(
            'India', indicatorName)]], 'red', label="India")
        plt.plot([-221,101],[-200, rank_by_indicator[(
            'United States of America', indicatorName)]], 'blue', label="USA")
        plt.plot([-221,101],[-200, rank_by_indicator[(
            'China', indicatorName)]], 'black', label="China")
        plt.plot([-221,101],[-200, rank_by_indicator[(
            'Somalia', indicatorName)]], 'orange', label="Somalia")
        plt.plot([-221,101],[-200, rank_by_indicator[(
            'Bangladesh', indicatorName)]], 'yellow', label="Bangladesh")
        plt.plot([-221,101],[-200, rank_by_indicator[(
            'United Kingdom', indicatorName)]], 'cyan', label="UK")
        plt.plot([-221,101],[-200, rank_by_indicator[(
            'Norway', indicatorName)]], 'magenta', label="Norway")
        plt.title(indicatorName)
    plt.legend(loc="best")
plt.show()



#                             ################### Optional Code ########################
    


#                                 ######  convert gapminder to list like my file   #####
# # list_1=[]
# # list_1=indicators.copy()
# # list_1.insert(0,'Country')
# # matrix=[]
# # matrix.append(list_1)
# # index=1
# # for countryN in countries:
#     matrix.append([]) 
#     for indicatorN in indicators:
#         value = (sum(
#             countriesDict[(countryN), (indicatorN)])/len(years))
#         matrix[index].append(countryN)    
#         matrix[index].append(value)
#     index+=1
#                                 ######  convert gapminder to Dictionary   #####

# countries_data{}
# # for countryN in countries:
#     for indicatorN in indicators:
#         value = (sum(
#             countriesDict[(countryN), (indicatorN)])/len(years))
#         countries_data[(countryN), (indicatorN)]]=value



                                ##########          Max Value Dictionary   ##################
# max_dict={}
# for i in indicators:
#     max=0
#     for j in countries:
#         value = (sum(
#             countriesDict[(j), (i)])/len(years))
#         if(max<value):
#             max=value
#     max_dict[(i)]=max

