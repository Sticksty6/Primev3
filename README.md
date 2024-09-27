This program is created using methods described in "RSA Cracked" by German Navarro.<br/>
## ----**Requirements**----<br/>
This program requires the 'bitarray' library. Once a user has created a python environment, bitarray
can be installed using<br/>
'>pip install bitarray'
# ----**Current State (09/26/2024)**----<br/>
Primev3 is set to generate a list of prime numbers from 5 to 2002225.
The length, 667408, is the number of numbers less than 2002225 that are not multiples of 2 or 3.
The remaining numbers are all 1 less than or 1 more than multiples of 6.<br/>
__init__<br/>
An array is created containing a number of bits equal to the specified bits, initialized to 0.<br/>
**flip_bit**<br/>
The program iterates through this list using checking rounds. Each time the value of the 'check'
increases, the 'check' lands on the ordinal location of a non-prime number. The value of that bit is changed to 1
using the **set_bit** function
and the program continues. The 'arrayX_output.txt' file shows the last number checked during each checking round.<br/>
**getPrime**<br/>
Next, the program iterates through the list one last time. If a bit is 0,
it takes the location of that value and converts it to its prime value. The conversion is different whether it is
an even or an odd position.<br/>
# ----**Example**----<br/>
**Numerical value(Ordinal Value)** <br/>
5(1), 7(2), 11(3), 13(4), 17(5), 19(6), 23(7), 25(8), 29(9), 31(10), 35(11), 37(12), 41(13), 43(14), 47(15), 49(16), 53(17), 55(18), 59(19), 61(20), 65(21), 67(22), 71(23), 73(24), 77(25)<br/>
The first checking round starts at the position 8, and flips the bit to 1. As seen, 25 is the first
non-prime number from that list. The check will next increase by 10 and land on 55 at position 18, another non-prime number.
The second checking round starts at the position 11, which relates to the number 35, and flips the bit to 1. The next number
the second round lands on is the position 21, which is the number 65.<br/>
# ----**Plans (09/26/2024)**----<br/>
1.Allow the user to choose their desired target number, instead of 2002225.<br/>
2.Improve time consumption of program<br/>
3.Implement methods described by German Navarro to allow the user to save their ordinal location,
restart the checking rounds, and generate primes from their last location to their target number.
This will save memory and allow for larger primes to be discovered.
