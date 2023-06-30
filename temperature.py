#create class Temperature
class Temperature:
    def convertFahrenheit(self, celsius):#create method convertFahrenheit and input attribute celsius
        fahrenheit = (celsius * 9/5) + 32# formula to convert fahrenheit to celsius
        print(f"{celsius} degrees Celsius is equal to {fahrenheit} degrees Fahrenheit.")#prints temp in fahrenheit

    def convertCelsius(self, fahrenheit):#create method convertcelsius and input attribute fahrenheit
        celsius = (fahrenheit - 32) * 5/9#formula to convert celsius to fahrenheit
        print(f"{fahrenheit} degrees Fahrenheit is equal to {celsius} degrees Celsius.")#this prints temp in celsius 

# Creating an instance of the Temperature class
temp = Temperature()

# Converting Celsius to Fahrenheit
#prompt user to input temp in celsius
celsius=float(input("enter temp in celsius\n"))
temp.convertFahrenheit(celsius)  

# Converting Fahrenheit to Celsius
#promt user to input temp in fahrenheit
fahrenheit=float(input("enter temp in celcius\n"))
temp.convertCelsius(fahrenheit)  