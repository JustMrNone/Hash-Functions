import hashlib
import sys
#we made this
import hash 


def main():
    
    try:
        try:
            hash_type = input("Choose Your Hash Function (default=sha256): ")
            if not hash_type:
                hash_type = 'sha256'
            if hash_type == 'show algorithms':
                print(hashlib.algorithms_available)
                sys.exit()
                
            string_obj = input("enter your string: ").strip()
            
        except AttributeError:
            print(f"Error: Unsupported hash type '{hash_type}'.")
        
        hashfunc = hash.HashChoice(hash_type)

        thetype = hashfunc.hash_type

        hashed = getattr(hashlib, thetype)()
        hashed.update(string_obj.encode())


        result = hashed.hexdigest()
        print(f"Hash Value: {result}")
        print(f"We used {hash_type}")
        
        
    except Exception as e:
        print(f"An error occurred: {e}")
        
        
if __name__ == "__main__":
    main()