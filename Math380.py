import csv
import math
#Math 380 project, trying to give a probability of damage of a hurricane based on the HSI scale

hurricane_names = []
total_points = []
economic_damages = []
wind_speeds = []

hurricane_cat_1 = []
hurricane_cat_2 = []
hurricane_cat_3 = []
hurricane_cat_4 = []
hurricane_cat_5 = []

hurricane_cat_1_names = []
hurricane_cat_2_names = []
hurricane_cat_3_names = []
hurricane_cat_4_names = []
hurricane_cat_5_names = []

with open('NHC_Data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ',')
    line_count = 0
    for row in csv_reader:
        if(line_count!=0):
            windSpeed = int(row[1]) 
            wind_speeds.append(windSpeed)
            if(windSpeed<=82):
                hurricane_cat_1.append(int(row[14]))
                hurricane_cat_1_names.append(row[0])
            elif(windSpeed<=95):
                hurricane_cat_2.append(int(row[14]))
                hurricane_cat_2_names.append(row[0])
            elif(windSpeed<=112):
                hurricane_cat_3.append(int(row[14]))
                hurricane_cat_3_names.append(row[0])
            elif(windSpeed<=136):
                hurricane_cat_4.append(int(row[14]))
                hurricane_cat_4_names.append(row[0])
            else:
                hurricane_cat_5.append(int(row[14]))
                hurricane_cat_5_names.append(row[0])
            
            vMax = 0
            if(windSpeed <30):
                vMax = 0
            elif(windSpeed>=30 and windSpeed<=150):
                vMax = round(pow(windSpeed/30, 2))
            else:
                vMax = 25
            total_radii_points=0

            P134 = int(row[2])
            P234 = int(row[3])
            P334 = int(row[4])
            P434 = int(row[5])
            P150 = int(row[6])
            P250 = int(row[7])
            P350 = int(row[8])
            P450 = int(row[9])
            P165 = int(row[10])
            P265 = int(row[11])
            P365 = int(row[12])
            P465 = int(row[13])

            effective_radius_32 = (1/2) * math.sqrt(pow(P134, 2) + pow(P234, 2) + pow(P334, 2) + pow(P434, 2))
            effective_radius_50 = (1/2) * math.sqrt(pow(P150, 2) + pow(P250, 2) + pow(P350, 2) + pow(P450, 2))
            effective_radius_65 = (1/2) * math.sqrt(pow(P165, 2) + pow(P265, 2) + pow(P365, 2) + pow(P465, 2))
            effective_radius_87 = 0.5683 * effective_radius_65 + (0.0792 * windSpeed) - 9.5383
            
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
            
            total_points_current = vMax + total_radii_points
            total_points.append(total_points_current)
            hurricane_names.append(row[0])
            economic_damages.append(int(row[14]))
        line_count+=1

count=0

get_all_hurricanes = input("Do you want to list all the HSI values of hurricanes that made landfall? Enter Y if so, enter N if not: ")

if(get_all_hurricanes == 'Y'):
    for name in hurricane_names:
        print(hurricane_names[count], ":" ,total_points[count], economic_damages[count])
        count+=1


#time to get the averages per point
#first get all the points into their own respective arrays
hurricane_names_1 = []
hurricane_names_2 = []
hurricane_names_3 = []
hurricane_names_4 = []
hurricane_names_5 = []
points_holder_1 = []
points_holder_2 = []
points_holder_3 = []
points_holder_4 = []
points_holder_5 = []
economic_damages_1 = []
economic_damages_2 = []
economic_damages_3 = []
economic_damages_4 = []
economic_damages_5 = []

count2 = 0
for item in hurricane_names:
    if(total_points[count2] <=22):
        hurricane_names_1.append(hurricane_names[count2])
        points_holder_1.append(total_points[count2])
        economic_damages_1.append(economic_damages[count2])
    elif(total_points[count2]<=35 ):
        hurricane_names_2.append(hurricane_names[count2])
        points_holder_2.append(total_points[count2])
        economic_damages_2.append(economic_damages[count2])
    elif(total_points[count2]<=44 ):
        hurricane_names_3.append(hurricane_names[count2])
        points_holder_3.append(total_points[count2])
        economic_damages_3.append(economic_damages[count2])
#    else:
 #       hurricane_names_4.append(hurricane_names[count2])
  #      points_holder_4.append(total_points[count2])
   #     economic_damages_4.append(economic_damages[count2])
    #elif(total_points[count2 ):
     #   hurricane_names_5.append(hurricane_names[count2])
      #  points_holder_5.append(total_points[count2])
       # economic_damages_5.append(economic_damages[count2])
    count2+=1

def get_average(array):
    temp_avg = 0
    itemCount = 0
    for item in array:
        temp_avg += int(array[itemCount])
        itemCount+=1
    return temp_avg/len(array)


def print_array(array):
    for x in range(0, len(array)):
        print(array[x])

cat_1_avg = get_average(hurricane_cat_1)
cat_2_avg = get_average(hurricane_cat_2)
cat_3_avg = get_average(hurricane_cat_3)
cat_4_avg = get_average(hurricane_cat_4)
cat_5_avg = get_average(hurricane_cat_5)

section_1_avg = get_average(economic_damages_1)
section_2_avg = get_average(economic_damages_2)
section_3_avg = get_average(economic_damages_3)

#Allow the user to input their own hurricane data and provide a probabilty of damage
#this probability is based on the historic hurricanes with the same/similar points.
#Also give various percentiles of damage.

hurricane_name = input("Enter the name of the hurricane: ")
hurricane_speed = int(input("Enter the wind speed of the hurricane in knots: "))
#34kt wind speed inputs from the user
hurricane_34kt_NW = int(input("Enter the 34kt wind speed in the NW direction: "))
hurricane_34kt_NE = int(input("Enter the 34kt wind speed in the NE direction: "))
hurricane_34kt_SW = int(input("Enter the 34kt wind speed in the SW direction: "))
hurricane_34kt_SE = int(input("Enter the 34kt wind speed in the SE direction: "))
#50kt wind speed inputs from the user
hurricane_50kt_NW = int(input("Enter the 50kt wind speed in the NW direction: "))
hurricane_50kt_NE = int(input("Enter the 50kt wind speed in the NE direction: "))
hurricane_50kt_SW = int(input("Enter the 50kt wind speed in the SW direction: "))
hurricane_50kt_SE = int(input("Enter the 50kt wind speed in the SE direction: "))
#64kt wind speed inputs from the user
hurricane_64kt_NW = int(input("Enter the 64kt wind speed in the NW direction: "))
hurricane_64kt_NE = int(input("Enter the 64kt wind speed in the NE direction: "))
hurricane_64kt_SW = int(input("Enter the 64kt wind speed in the SW direction: "))
hurricane_64kt_SE = int(input("Enter the 64kt wind speed in the SE direction: "))
windSpeed_user = 0

if(hurricane_speed < 30):
    windSpeed_user = 0
elif(hurricane_speed>30 and hurricane_speed <150):
    windSpeed_user = round(pow(hurricane_speed/30, 2))
else:
    windSpeed_user = 25

effective_radius_32_user = (1/2) * math.sqrt(pow(hurricane_34kt_NW, 2) + pow(hurricane_34kt_NE, 2) + pow(hurricane_34kt_SW, 2) + pow(hurricane_34kt_SE, 2))
effective_radius_50_user = (1/2) * math.sqrt(pow(hurricane_50kt_NW, 2) + pow(hurricane_50kt_NE, 2) + pow(hurricane_50kt_SW, 2) + pow(hurricane_50kt_SE, 2))
effective_radius_65_user = (1/2) * math.sqrt(pow(hurricane_64kt_NW, 2) + pow(hurricane_64kt_NE, 2) + pow(hurricane_64kt_SW, 2) + pow(hurricane_64kt_SE, 2))
effective_radius_87_user = 0.5683 * effective_radius_65_user + (0.0792 * hurricane_speed) - 9.5383

total_radii_points_user = 0

if(effective_radius_32_user<100):
    total_radii_points_user+=1
elif(effective_radius_32_user<155):
    total_radii_points_user+=2
else:
    total_radii_points_user+=3

if(effective_radius_50_user<50):
    total_radii_points_user+=1
elif(effective_radius_50_user<75):
    total_radii_points_user+=2
elif(effective_radius_50_user<105):
    total_radii_points_user+=3
else:
    total_radii_points_user+=4

if(effective_radius_65_user<25):
    total_radii_points_user+=1
elif(effective_radius_65_user<34):
    total_radii_points_user+=2
elif(effective_radius_65_user<42):
    total_radii_points_user+=3
elif(effective_radius_65_user<50):
    total_radii_points_user+=4
elif(effective_radius_65_user<58):
    total_radii_points_user+=5
elif(effective_radius_65_user<66):
    total_radii_points_user+=6
elif(effective_radius_65_user<74):
    total_radii_points_user+=7
else:
    total_radii_points_user+=8

if(effective_radius_87_user<13):
    total_radii_points_user+=1
elif(effective_radius_87_user<17):
    total_radii_points_user+=2
elif(effective_radius_87_user<22):
    total_radii_points_user+=3
elif(effective_radius_87_user<24):
    total_radii_points_user+=4
elif(effective_radius_87_user<30):
    total_radii_points_user+=5
elif(effective_radius_87_user<34):
    total_radii_points_user+=6
elif(effective_radius_87_user<38):
    total_radii_points_user+=7
elif(effective_radius_87_user<42):
    total_radii_points_user+=8
elif(effective_radius_87_user<48):
    total_radii_points_user+=9
else:
    total_radii_points_user+=10


total_points_user = windSpeed_user + total_radii_points_user

names_with_points_that_match = []
countForPrint = 0
for name in hurricane_names:
    if(total_points[countForPrint] == total_points_user):
        names_with_points_that_match.append(hurricane_names[countForPrint])
    countForPrint+=1
#print("Hurricanes with matching points:")
#print_array(names_with_points_that_match)

points_list = []
damage_list =[]


with open('Average_Damage.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter =',')
    line_count = 0
    for row in csv_reader:
        if(line_count!=0):
            points_list.append(int(row[1]))
            damage_list.append(float(row[0]))
        line_count+=1

exist_count = points_list.count(total_points_user)
length = len(damage_list)
point_count = 0

def get_closest_hurricane(score):
    for x in damage_list:
        score+=1
        if(points_list.count(score)>0):
            return score

damage_of_hurricane = 0
average_of_all_three=0
print("\n")
for x in points_list:
    if(total_points_user <= 9):
        print("Your hurricane has a total score of: ",total_points_user)
        damage_of_hurricane = damage_list[0]
        if(total_points_user==9):
            print("The average economic damage of the hurricane with the same score is: ",damage_list[0])
            print("Hurricane(s) with matching points:")
            print_array(names_with_points_that_match)
        else:
            print("The average economic damage of the hurricane(s) with the closest score is: ",damage_list[0])
        print("The average economic damage of the hurricane(s) with a score 1 point above your hurricane is: ",damage_list[1])
        average_of_all_three = (damage_list[0] + damage_list[1])/2
        print("The average between these values is:",average_of_all_three)
        break
    elif(total_points_user >= 41):
        print("Your hurricane has a total score of: ",total_points_user)
        damage_of_hurricane = damage_list[length-1]
        if(total_points_user==41):
            print("The average economic damage of the hurricane(s) with the same score is ",damage_list[length-1])
            print("Hurricane(s) with matching points:")
            print_array(names_with_points_that_match)
        else:
            print("The average economic damage of the hurricane(s) with the closest score is: ",damage_list[length-1])
        print("The average economic damage of the hurricane(s) with a score 1 point below your hurricane is: ",damage_list[length-2])
        average_of_all_three = (damage_list[length-1]+damage_list[length-2])/2
        print("The average between these values is:",average_of_all_three)
        break
    elif(exist_count==0):
        print("Your hurricane has a total score of: ",total_points_user)
        new_position = damage_list[getclosest_hurricane(total_points_user)]
        damage_of_hurricane = damage_list[new_position]
        print("The average economic damage of the hurricane(s) with the closest score is: ",damage_list[new_position])
        print("The average economic damage of the first hurricane(s) with a score lower than your hurricane is: ",damage_list[new_position-1])
        print("The average economid damage of the first hurricane(s) with a score higher than your hurricane is: ",damage_list[new_position+1])
        average_of_all_three = (damage_list[new_position] + damage_list[new_position-1] + damage_list[new_position+1])/3
        print("The average between these values is:",average_of_all_three)
    if(total_points_user == points_list[point_count]):
        print("Your hurricane has a total score of: ",total_points_user)
        print("Hurricane(s) with matching points:")
        print_array(names_with_points_that_match)
        damage_of_hurricane = damage_list[point_count]
        print("The average economic damage of the hurricane(s) with the same score is: ",damage_list[point_count])
        print("The average economic damage of the hurricane(s) with a score 1 point below your hurricane is: ",damage_list[point_count-1])
        print("The average economic damage of the hurricane(s) with a score 1 point above your hurricane is: ",damage_list[point_count+1])
        average_of_all_three = (damage_list[point_count] + damage_list[point_count-1] + damage_list[point_count+1])/3
        print("The average between these values is:",average_of_all_three)
        break
    point_count+=1

#damage_count = 0
def get_damage_under(damage_array,damage_amount):
    hold_damage = []
    damage_count = 0
    for x in damage_array:
        if(damage_array[damage_count]<damage_amount):
            hold_damage.append(damage_array[damage_count])
        damage_count+=1
    return hold_damage

damage_under_singular = get_damage_under(damage_list,damage_of_hurricane)
damage_under_average = get_damage_under(damage_list,average_of_all_three)

length_sing = len(damage_under_singular)
length_avg = len(damage_under_average)

percentile_of_damage_singular= (length_sing/length) * 100 
percentile_of_damage_average = (length_avg/length) * 100

scores_under_total = get_damage_under(points_list,total_points_user)
length_score = len(scores_under_total)
percentile_of_score = (length_score/len(points_list)) * 100

print("The percentile of the damage of hurricane(s) with your score is: ",percentile_of_damage_singular)
print("The percentile of the average damage of the hurricane(s) just below, at, and just above your score is: ",percentile_of_damage_average)
print("the percentile of your hurricane's score is: ",percentile_of_score)


