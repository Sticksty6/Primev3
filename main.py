from bitarray import bitarray

class manipulateArray:

    def __init__(self, length):
        #Defines an array of bits of desired length
        self.bits = bitarray(length)
        self.bits.setall(0)

    def set_bit(self, position):
        #Sets bit at desired position to 1
        self.bits[position]=1

    def display_bit(self, position):
        #Display bit status at desired position
        print(self.bits[position])

    def flip_bit(self, checking_rounds, length, counter, arrayX):
        #Sieves through bitarray and calls set_bit to flip desired bit to a 1
        value =5
        current_round =1
        frequency = 0
        starting_value = 0
        previous_even_start = 1
        while current_round <= checking_rounds:
            if current_round%2 ==1:
                starting_value = int(((value*value)-1)/3)
                frequency = value*2
                while starting_value <= length:
                    self.set_bit(starting_value-1)
                    starting_value+=frequency
                arrayX[current_round-1]=starting_value-frequency
                counter+=1
                current_round+=1
            else:
                starting_value = int((value*2)+previous_even_start)
                previous_even_start = starting_value
                frequency = value *2
                while starting_value <= length:
                    self.set_bit(starting_value-1)
                    starting_value += frequency
                if(current_round%4 == 0):
                    value+=4
                else:
                    value+=2
                arrayX[current_round-1]=starting_value-frequency
                counter+=1
                current_round+=1
        print(counter)

    def save_to_file(self, filename):
        #Saves binary list to a file
        with open(filename,'wb') as filename:
            self.bits.tofile(filename)

    def getPrime(self, output_file, length):
        #Iterates through array of bits to turn the bit position into the desired prime number
        with open(output_file,'w') as outfile:
            prime=0
            for i in range(length):
                if(self.bits[i]==0):
                    if(i%2 == 0):
                        prime=3*(i+1)+2
                        outfile.write(f"{prime}\n")
                    else:
                        prime=3*(i+1)+1
                        outfile.write(f"{prime}\n")

#Initializations
length = 667408
checks = 940
counter = 0
arrayX = [0] * (checks)
ordinal_list=manipulateArray(length)
ordinal_list.flip_bit(checks,length,counter,arrayX)
#Save the binary data
ordinal_list.save_to_file('ordinal_output.txt')
#Converts binary data to decimal value of prime number
ordinal_list.getPrime('prime_output.txt',length)
#A file containing the last value checked during checking rounds
with open('arrayX_output.txt','w') as outfile:
    for i in range(checks):
        outfile.write(f"{arrayX[i]}\n")