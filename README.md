# C-IP4RIoT-PRJ-V2-OOP
This is the Car Park project

Q. Which class is responsible for the number of available bays (and why)?

> The CarPark class is responsible for the number of available bays.
The number of available bays is tied to the capacity of the car park, which is a property 
> of the CarPark class. It is essential for tracking how many spots are available for new car

Q. Which class is responsible for the current temperature (and why)?

> Since sensors are designed to collect real-world data like temperature, it makes sense for this responsibility 
> to fall under the Sensor class.

Q. Which class is responsible for the time (and why)?

> Displays are typically the component responsible for showing information to the users, including the time. 
> The Display class would handle updating the time on the screen for the driver to see.


Which class is responsible for each of the following pieces of information (and why)?

The number of available bays
>  Car Park class. Since it pertains to the car park's capacity and occupancy, the CarPark class is responsible for calculating and
> providing this information. 

The current temperature
>Car Park class. The car park can have a temperature sensor (like the TemperatureSensor class), but the car park itself would be the one that 
> requests and displays the temperature. The CarPark class gathers the temperature data through the TemperatureSensor class,
> which actively monitors and provides the temperature value

The time 
>  In order to update the displays appropriately, the CarPark class retrieves the current time, like  a system clock.


What is the difference between an attribute and a property? 
> An attribute is a variable that stores data or information about an object. A property is a special kind of method that behaves like an attribute. 
> It allows you to define a method that can be accessed as if it were a regular attribute. 
> The main difference is that properties allow for dynamic computation and additional logic, whereas attributes store static values that can be directly accessed or modified.

Why do you think we used a dictionary to hold the data we passed the display? List at least one advantage and one disadvantage of this approach.
> We used a dictionary because it's flexible and easy to add new data without changing the method, but the downside is that it can lead to mistakes
> if the keys or values aren't handled carefully, and sometimes a more structured approach might be better.

Test the car park register method
The car park register method should accept a Sensor or Display object. It should raise a TypeError if the object is neither a Sensor nor a Display. 
Before proceeding, think about where you would test this behaviour. Should you test it in the CarPark unit tests or the Sensor unit tests? Why?
> The CarPark class includes the register method. Since this behaviour is strongly linked to how the CarPark handles sensors and displays, 
> it is appropriate to test this functionality in the CarPark unit tests.