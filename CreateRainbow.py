import hashlib 
import hash
import sys
import csv

#Well! I should think about this 


class RainBow():
    def __init__(self, filename):
        self.filename = filename 
    
    #save it to the list
    def savelines(self):
        with open(self.filename, 'r') as file:
            lines = file.readlines()
        lines = [line.strip() for line in lines]
        return lines
    
    #hash that shit
    def hashit(self, choice, line):
        #use hash module
        thehash = hash.HashChoice(choice)
        #access the type
        hashed = thehash.type
        hashed.update(line.encode())
        #return in a readable form
        return hashed.hexdigest()
    #save that shit in dict
    
    def saveitdic(self, initial_list, hashed_list):
        Dictio = dict(zip(initial_list, hashed_list))
        return Dictio
    
    def savecsv(self, newname, data_dict):
        csv_file = newname[0] + ".csv"
        with open(csv_file, 'w', newline='') as csvfile:
            field_names = ['Initial_Value', 'Hashed_Value']
            writer = csv.DictWriter(csvfile, fieldnames=field_names)
            writer.writeheader()
            
            #converting your dictionary into a list of dictionaries
            for initial, hashed in data_dict.items():
                writer.writerow({'Initial_Value': initial, 'Hashed_Value': hashed})
#putting the values inside of a list 
def hashedlist(thelist, obj, input):
    hashed_list = []
    for line in thelist:
        hashe_value = obj.hashit(input, line)
        hashed_list.append(hashe_value)
    return hashed_list


def main():
    #if command line argument 
    if len(sys.argv) > 1:
        #to see hashing options
        if sys.argv[1] == 'print':
            print("Available hash algorithms:", hashlib.algorithms_guaranteed)
            sys.exit(0)
        else:
            filename = sys.argv[1]   
    else:
        #if no cmd argument 
        filename = input("Enter the file name: ") 
    try:
        # check if a hashing method is provided in the command-line argument
        if len(sys.argv) > 2:
            intake = sys.argv[2]
        else:
            #take the hashing method
            intake = input('Choose your hashing method (default sha256): ')
            if not intake:
                intake = 'sha256'
        
        # construct the that shit
        cons = RainBow(filename)
        
        # get lines from file
        the_list = cons.savelines()
        
        # get the hashed list
        hashed_list = hashedlist(the_list, cons, intake)
        
        # create dictionary from original and hashed lists
        the_dict = cons.saveitdic(the_list, hashed_list)
        
        # save dictionary to CSV
        newname = filename.split('.')
        cons.savecsv(newname, the_dict)
    
    except FileNotFoundError:
        print("File not found. Make sure that it is in your directory.")
    except Exception as e:
        print(f"An error occurred: {e}")
    
    
if __name__ == "__main__":
    main()