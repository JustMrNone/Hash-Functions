import hashlib 
import hash
import sys
import csv
#I should think about this 


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
        thehash = hash.HashChoice(choice)
        hashh = thehash.hash_type
        hashed = getattr(hashlib, hashh)()
        hashed.update(line.encode())
        
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

def main():
    try:
        filename = input()
        while not filename:
            filename = input("Please enter a filename: ")
            
    except Exception as e:
        print(e)
        sys.exit(1)
        
    intake = input('choose your hashing method(default sha256): ')
    if not intake:
        intake = 'sha256'
        
    #construct that shit    
    cons = RainBow(filename)
    
    the_list = cons.savelines()
    
    hashed_list = []
    for line in the_list:
        hashe_value = cons.hashit(intake, line)
        hashed_list.append(hashe_value)
    
    #print(hashed_list)
    
    the_dict = cons.saveitdic(the_list, hashed_list)
    

    #debug that shit
    
    #print(the_dict)
    newname = filename.split('.')
    cons.savecsv(newname, the_dict)

        
if __name__ == "__main__":
    main()