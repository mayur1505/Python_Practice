#measure total distance from new york to baltimore to pittsburg
nyc_bal=188
bal_pitt=247
total_dist=nyc_bal+bal_pitt
print(total_dist)

#total to reach assuming 65mph as avg speed
mph=65
time=total_dist/mph
print(time)
print(round(time,2))#rounded off to 2 decimals
#12,14,65,235 are all integers
#2.334555 , 4.899  are float numbers
#python follows bodmos rule for operation
print(10+2*3)
