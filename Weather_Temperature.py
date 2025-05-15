# Question :
#Ask the user to enter the current temperature.

#	•	If it’s above 30°C, print “It’s hot, stay hydrated!”
#	•	If it’s below 10°C, print “It’s cold, wear a jacket!”
#	•	Otherwise, print “The weather is fine.”

temperature = int(input("What is the temperature: "))

if temperature > 30:
    print("It's hot, stay hydrated!")
elif temperature < 10:
    print("It's cold, wear a jacket!")
else:
    print("The weather is fine.")