try:
    Data=float(input("For Celsius to Fahrenheit type 1 for Fahrenheit to Celsius type 2 -> "));
    if Data == 1:
        print("\n\n°Celcius to °Fahrenheit\n");
        Celcius = float(input("Enter the °Celcius --> "));
        Fahrenheit = (9/5 * Celcius) + 32;
        print(f"\n{Celcius}°C = {Fahrenheit}°F")

    elif Data == 2: 
        print("\n\n°Fahrenheit to °Celcius\n");
        Fahrenheit = float(input("Enter the °Fahrenheit --> "));
        Celcius = ((Fahrenheit -32) * 5/9);
        print(f"\n{Fahrenheit}°F = {Celcius}°C");
    
    else:
        if type = int;
except:
    print("Invalid Input");