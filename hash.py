import hashlib
import sys

class HashFile:
    def __init__(self, filename, hash_type):
        self.filename = filename
        self.buff_size = 65536  # Buffer size for reading file
        
        if hash_type == None:
            self.hash = hashlib.sha256()
        else:
            self.hash = hash_type 
    def hash_file(self):
        try:
            with open(self.filename, "rb") as f:
                while True:
                    data = f.read(self.buff_size)
                    if not data:
                        break
                    self.hash.update(data)
            #make it readable 
            return self.hash.hexdigest()
        except FileNotFoundError:
            print(f"File '{self.filename}' not found.")
            sys.exit(1)            

class HashChoice:
    def __init__(self, hash_type):
        self.hash_type = hash_type.lower()  
        if self.hash_type in hashlib.algorithms_available:
            
            self.type = getattr(hashlib, self.hash_type)()  # Create the hash object
        else:
            print(f"Unsupported hash type: {hash_type}")
            sys.exit(1)
            
def main():
    if len(sys.argv) < 2:
        #When no Argv
        print("Available hash algorithms:", hashlib.algorithms_guaranteed)
        
    
    elif len(sys.argv) < 3:
        hash_default = HashFile(sys.argv[1], None)
        print(f"Hash Value: {hash_default.hash_file()}")
        print("Hash Type: default(sha256)")
            
    else:
        # Get the hash function based on the user's choice
        what_hash = HashChoice(sys.argv[2]).type
        
        # Initialize the HashFile object with the filename and hash function
        hash_file_obj = HashFile(sys.argv[1], what_hash)
    
        # Compute and print the hash
        hashed = hash_file_obj.hash_file()
        print(f'Hash Value: {hashed}')
        print(f'Hash Type: {sys.argv[2]}' )
       

if __name__ == "__main__":
    main()





















#psudocode: I just do not want to delete these so I will leave them here 

''' CreateRainbow

1 - .read(file)

2 - for line in file: append line to the list

3 - choice of hashing = input()

4 - if the input is None: default = sha256 

5 - hash each item in the list with the chosen hashing algorithm

6 - dictionary = {input value : the hash value}

7 - print("enter 1 to print to console leave empty to save the csv") ??

8 - if 1 print the dictionary

9 - else save the dictionary to a csv file

10 - sys.exit(1)'

11 - add command line accessibility 

Reverse.py

1 - take the rainbow table
2 - take the hash values
3 - compare with the hash values in the table
4 - if the hashvalue exists get the corresonding value
5 - create a dictionary of found values 
5 - if the hash value is not in the database 
6 - print("value not found")

'''