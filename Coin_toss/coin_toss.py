import random
import csv

for j in range(1,101):
    filepath = f"C:/Users/aryan/OneDrive/Desktop/coin/coin_toss{j}.csv"
    with open(filepath,"a",newline="") as csvfile:
        csv_writer = csv.writer(csvfile)

        csv_writer.writerow(["Trial Num","Random Numb","Result"])

        for i in range(1,10001):
            toss_result = random.uniform(0,1)
            if toss_result < 0.5 :
                result = "Heads"
            else :
                result = "Tails"
        
            csv_writer.writerow([i,toss_result,result])


    
print("done !!!!!!! ")
