import os, sys, hashlib, hash, csv

#probably will complete later 


class Reverse:
    def __init__(self, filename, dictname):
        self.filename = filename
        self.dictname = dictname
    #read your hash values
    def read_lines(self):
        with open(self.filename, 'r') as file:
            lines = file.readlines()
        lines = [line.strip() for line in lines]
        return lines
    
    #read your created dictionary containing key value pairs
    def read_dict(self):
        try:
            with open(self.dictname, 'r') as file:
                lines = csv.reader(file)
                dictionary = {rows[0]: rows[1] for rows in lines}
            return dictionary
        except Exception as e:
            print("Error: CSV file is not formatted correctly.")
            print(f"Details: {e}")
            sys.exit(1)
        
    #find that shit 
    def compare_and_save(self, list_to_compare, output_filename):
        dictionary = self.read_dict()
        found = False
        #write to csv
        with open(output_filename, 'w', newline='') as file:
            writer = csv.writer(file)
            for item in list_to_compare:
                matched = False
                for key, value in dictionary.items():
                    if item == value:
                        writer.writerow([key+' --> ', value])
                        matched = True
                        found = True
                        break
                if not matched:
                    writer.writerow(["Nothing found! --> ", item])
        
        if not found:
            with open(output_filename, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["Nothing found"])

def cmdargment():
    """Handle command-line arguments or prompt for user input."""
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        filename = input("Enter File Name (.txt): ")
    
    if len(sys.argv) > 2:
        csvname = sys.argv[2]
    else:
        csvname = input("Enter CSV Name (.csv): ")
    
    # check if the files exist
    if not os.path.isfile(filename):
        print(f"Error: Text File '{filename}' not found.")
        sys.exit(1)
    
    if not os.path.isfile(csvname):
        print(f"Error: CSV file '{csvname}' not found.")
        sys.exit(1)
    
    return filename, csvname


def main():
    filename, csvname = cmdargment()
    # construct the object 
    rev = Reverse(filename, csvname)
    # read the lines
    line_redear = rev.read_lines()
    # extract the name
    thename = filename.split('.')
    # finilize the process
    rev.compare_and_save(line_redear, thename[0]+'.csv')

# only run main function if run directly
if __name__ == "__main__":
    main()