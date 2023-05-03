import csv
import math
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
#with open('HSI_Data.csv') as csv_file:
#    csv_reader = csv.reader(csv_file, delimiter = ',')
#   line_count = 0
#  for row in csv_reader:
#    hsi_index_values.append 

#read in the hurricane radius data from the NHC
with open('NHC_Data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ',')
    #start the line count at the first hurricane that has the data for the radius
    line_count = 0
    for row in csv_reader:
        if(line_count!=0):
            hurricane_data_NW.append(row[1])
            hurricane_data_NE.append(row[2])
            hurricane_data_SW.append(row[4])
            hurricane_data_SE.append(row[3])
        line_count+=1

#try to get a formula that will be used to estimate 1 point of damage
#NW=
#SW=hurricane_data_
#NE=hurricane_data_NE[0]
#SE=hurricane_data_SE[0]
#print(hurricane_data_NW[0])
#print(

windSpeed = 105
vMax = 0
if(windSpeed <30):
    vMax = 0
elif(windSpeed>=30 and windSpeed<=150):
     vMax = round(pow(windSpeed/30, 2))
else:
     vMax = 25
total_radii_points=0

effective_radius_32 = (1/2) * math.sqrt(pow(110, 2) + pow(175, 2) + pow(90, 2) + pow(75, 2))
effective_radius_50 = (1/2) * math.sqrt(pow(65, 2) + pow(60, 2) + pow(30, 2) + pow(30, 2))
effective_radius_65 = (1/2) * math.sqrt(pow(20, 2) + pow(20, 2) + pow(15, 2) + pow(20, 2))
effective_radius_87 = 0.5683 * effective_radius_65 + (0.0792 * windSpeed) - 9.5393

#assign points based on effective_radii
if(effective_radius_32<100):
    total_radii_points+=1
elif(effective_radius_32<155):
    total_radii_points+=2
else:
    total_radii_points+=3

if(effective_radius_50<50):
    total_radii_points+=1
elif(effective_radius_50<75):
    total_radii_points+=2
elif(effective_radius_50<105):
    total_radii_points+=3
else:
    total_radii_points+=4

if(effective_radius_65<25):
    total_radii_points+=1
elif(effective_radius_65<34):
    total_radii_points+=2
elif(effective_radius_65<42):
    total_radii_points+=3
elif(effective_radius_65<50):
    total_radii_points+=4
elif(effective_radius_65<58):
    total_radii_points+=5
elif(effective_radius_65<66):
    total_radii_points+=6
elif(effective_radius_65<74):
    total_radii_points+=7
else:
    total_radii_points+=8

if(effective_radius_87<13):
    total_radii_points+=1
elif(effective_radius_87<17):
    total_radii_points+=2
elif(effective_radius_87<22):
    total_radii_points+=3
elif(effective_radius_87<24):
    total_radii_points+=4
elif(effective_radius_87<30):
    total_radii_points+=5
elif(effective_radius_87<34):
    total_radii_points+=6
elif(effective_radius_87<38):
    total_radii_points+=7
elif(effective_radius_87<42):
    total_radii_points+=8
elif(effective_radius_87<48):
    total_radii_points+=9
else:
    total_radii_points+=10

total_points = vMax + total_radii_points

ida_points = 18
ida_damage = 2200000000
ida_impact = 57565950
total_damage = (ida_damage/ida_points)

print(effective_radius)

print(total_damage)
print(total_points)

#try to get a formula that will estimate the economic impact of a hurricane on the model city

#Allow the user to input their own hurricane data and provide a probabilty of damage

#create graphs that will be outputted that shows the damage and probability.


