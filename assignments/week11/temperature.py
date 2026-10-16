"""
Write a program that analyzes daily temperatures for a week:
 
Create a function get_temperatures() that:
 
- Uses a local list to store 7 temperature values (use input or predefined values)
- Returns the list
 
Create a function analyze_temps(temp_list) that:
 
- Calculates and returns the average temperature (local variable)
- Finds and returns the highest temperature
- Finds and returns the lowest temperature
- Returns all three values as a tuple
 
Create a function display_analysis(avg, high, low) that prints the results nicely formatted
 
Example Output:
Temperature Analysis for the Week:
Average: 23.5 C
Highest: 28 C
Lowest: 19 C
 
"""
 
def get_temperatures():
    temps = [31,31,32,29,33,31,27]
    return temps
 
def analyze_temps(temp_list):
    total = sum(temp_list)
    lowest = min(temp_list)
    highest = max(temp_list)
   
 
           
    average = total / 7
   
    return (average, highest, lowest)
 
 
def display_analysis(avg, high, low):
    print("Temperature Analysis for the Week: ")
    print("Average: %.1f C" %(avg))
    print(f"Highest: {high: .1f} C")
    print("Lowest: %.1f C" %(low))
   
 
temps = get_temperatures()            
avg, high, low = analyze_temps(temps)
display_analysis(avg, high, low)      