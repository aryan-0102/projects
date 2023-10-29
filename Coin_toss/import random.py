import random
import csv


filepath = f"C:/Users/aryan/OneDrive/Desktop/coin_toss.csv"
with open(filepath,"a",newline="") as csvfile:
        csv_writer = csv.writer(csvfile)

        csv_writer.writerow(["Trial Num","Random Numb","Result"])

        for i in range(1,1000001):
            toss_result = random.uniform(0,1)
            if toss_result < 0.5 :
                result = "Heads"
            else :
                result = "Tails"
        
            csv_writer.writerow([i,toss_result,result])


    
print("done !!!!!!! ")