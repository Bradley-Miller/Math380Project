import csv

#Math 380 project, trying to give a probability of damage of a hurricane based on the HSI scale

model_city_pop = 100000 

historic_economic_damages = []
hsi_index_values = []
#Hurricane data from the NHC
hurricane_data_NW = []
hurricane_data_NE = []
hurricane_data_SW = []
hurricane_data_SE = []
#Re = 1/2 * (sqrt(RNE^2 + RNW^2 + RSW^2 + RSE^2))
effective_radius = 0

#reading in the first csv file with hurricane damage stats

with open('Hurricane_Data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print("names")
            line_count += 1
        else:
            historic_economic_damages.append(row[3])
            line_count += 1

    print(historic_economic_damages)

#read in the HSI index values
with open('HSI_Data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ',')
    line_count = 0
    for row in csv_reader:
        hsi_index_values.append 

#read in the hurricane radius data from the NHC
with open('NHC_Data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ',')
    #start the line count at the first hurricane that has the data for the radius
    line_count = 0
    for row in csv_reader:
        hurricane_data_NW.append()
        hurricane_data_NE.append()
        hurricane_data_SW.append()
        hurricane_data_SE.append()

#try to get a formula that will be used to estimate 1 point of damage


#try to get a formula that will estimate the economic impact of a hurricane on the model city

#Allow the user to input their own hurricane data and provide a probabilty of damage

#create graphs that will be outputted that shows the damage and probability.

