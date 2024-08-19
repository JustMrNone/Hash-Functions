import hashlib
import sys

class HashFile:
    def __init__(self, filename, hash_type):
        self.filename = filename
        self.buff_size = 65536  # Buffer size for reading file
        self.hash = hash_type  # Initialized with a hash object
            
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
        self.hash_type = hash_type.lower()  # Case insensitive check
        if self.hash_type in hashlib.algorithms_available:
            self.type = getattr(hashlib, self.hash_type)()  # Create the hash object
        else:
            print(f"Unsupported hash type: {hash_type}")
            sys.exit(1)
            
def main():
    if len(sys.argv) < 3:
        #When no Argv
        print("Available hash algorithms:", hashlib.algorithms_guaranteed)
    else:
        # Get the hash function based on the user's choice
        what_hash = HashChoice(sys.argv[2]).type
        
        # Initialize the HashFile object with the filename and hash function
        hash_file_obj = HashFile(sys.argv[1], what_hash)
    
        # Compute and print the hash
        hashed = hash_file_obj.hash_file()
        print(f'Hash: {hashed}')

if __name__ == "__main__":
    main()
