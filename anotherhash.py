import hashlib

#we made this
import hash 


def main():
    
    try:
        try:
            hash_type = input()
            string_obj = input()
        except: 
            print("Error: Invalid input. Please provide a valid hash type and string.")
            return False
        
        
        hashfunc = hash.HashChoice(hash_type)

        thetype = hashfunc.hash_type

        hashed = getattr(hashlib, thetype)()
        hashed.update(string_obj.encode())


        result = hashed.hexdigest()
        print(f"Hash Value: {result}")
        print(f"We used {hash_type}")
    except:
        print("An error occurred while executing the program.")

if __name__ == "__main__":
    main()