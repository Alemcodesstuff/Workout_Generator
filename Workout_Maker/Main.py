import csv
import random


#create file for output ; Names of columns
file_to_output = open('workout.csv','w',newline='')
csv_writer = csv.writer(file_to_output,delimiter=',',)
csv_writer.writerow(['Body part', 'Exercise','Sets','Reps'])
file_to_output.close()

#reader for csv file
data = open('workout.csv',encoding="utf-8")
csv_data = csv.reader(data)
data_lines = list(csv_data)

body_parts = ['Lower', 'Upper']



#lower body program
if(random.choice(body_parts) == 'Lower'):
    
    exercises_legs = ['Squat','Deadlift','Goblet squat','Romanian Deadlift','Sumo Deadlift','Lunges','Bulgarian split squad','Hip trust','Calf raise', 'Leg extesions']
    exercises_stomach= ['Crunch','Climbers','Hanging raises','Leg raises','Back extension','Reverse crunch', 'Plank']
    pomocna = 0
    exercises_for_output = []

    
    while(pomocna < 5):
        ex = random.choice(exercises_legs)
        exercises_for_output.append(ex)
        exercises_legs.remove(ex)
        temp+=1

    csv_writer.writerow(exercises_for_output)



else:
    exercises_dict={'Chest':['Bench','Incline bench','Decline bench','Fly'],
                    'Shoulders':['Overhead press','Lat raise','Shrugs','Fly','Machine press'],
                    'Back':['Pullups','Pulldowns','Bar pulldowns','BB Row','Machine row','Cable row'],
                    'Biceps':['EZ curl','DB curl','Inner curl','Standing curl','Waiter curl'],
                    'Triceps':['Dips','Triceps ext','DB ext','Machine pulldown']}
    
    
    # dictionary unpacking
    for items,values in exercises_dict.items():
        body_part = items
        body_part_ex = []
        
        for i in range(0,3):
            exercise = random.choice(values)
            body_part_ex.append(exercise)
            values.remove(exercise)

        to_write = body_part, body_part_ex
        csv_writer.writerow(to_write)
