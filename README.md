# Currency conversor
Python | Currency conversor - Practice - 4/2023
This is a currency convertor that i made as a python practice in my study time.
The program converts 
  * Pesos Argentinos
  * Pesos Colombianos
  * Pesos Mexicanos
  
 Into US dolars using diferents tipe of exchance by country.

In this Python code, you can observe the following things:

* The code defines a multi-line string variable called menu, which serves as a menu prompt for a currency converter.
* It prompts the user to input an option by displaying the menu string and storing the input as an integer in the opcion variable.
* It checks the value of opcion using an if statement and executes different code blocks based on the chosen option.
 * If opcion is 1, it prompts the user to input the amount of pesos to convert to dollars, performs the conversion using a fixed exchange rate, rounds the result to 2 decimal places, and displays the converted amount and exchange rate.
* If opcion is 2, it performs a similar conversion using a different exchange rate specific to Colombian pesos.
* If opcion is 3, it performs a conversion using a different exchange rate specific to Mexican pesos.
* If the value of opcion does not match any of the specified cases, it prints a message indicating that an incorrect option was entered.

The code demonstrates the use of input/output functions (input() and print()) for user interaction, variable assignment and manipulation, conditional statements (if, elif, else), and string concatenation.
