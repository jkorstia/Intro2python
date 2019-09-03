# a program to calculate population size after a user specified time (in years) 
# demographic rates are fixed, initial population size is 307357870 selfie taking quokkas
# This script is designed to model quokka populations! Use with other species at your own risk.

# ask user for number of years (inputs as string)
yr_str=input("How many years into the future would you like to predict the population size?")
# convert year string to integer
yr_int=int(yr_str)
# define demographic statistics in seconds
birth_s=7
death_s=13
imm_s=35
# starting population size in quokkas
pop=307357870
# convert demographic statistics to years.  31536000 seconds are in a year (60s*60m*24hrs*365days).
birth_y=birth_s*31536000
death_y=death_s*31536000
imm_y=imm_s*31536000

#since the population changes every year, this must be re-evaluated after each year
#sets up the initial population for the loop
initial_population=pop
count=0
while(count < yr_int):
	#counter for number of years
	count = count + 1
	#figures out the final population after i years
	final_population=initial_population+birth_y+imm_y-death_y
	#prints out results
	print("After", count, "years the population is", final_population)
	# readjusts the initial population for subsequent years
	initial_population=final_population
