import csv

def csv2text():
    # Open the CSV file
    with open('./data/minor_consultation.csv', 'r') as file:
        # Create a CSV reader object
        csv_reader = csv.reader(file)
        
        # Read the header row
        headers = next(csv_reader)
        
        # Find the indices of the columns named 'description' and 'dialogue'
        description_index = headers.index('description')
        dialogue_index = headers.index('dialogue')
        fileName = './data/minor_consultation.txt'
        # Open a text file for writing
        with open(fileName, 'w') as output_file:
            # Iterate over each row in the CSV file
            for row in csv_reader:
                # Concatenate data from the 'description' and 'dialogue' columns
                # concatenated_line = f"{row[description_index]} {row[dialogue_index]}\n"
                description = row[description_index]
                dialogue = row[dialogue_index]
                concatenated_line = f"When the health issue discussion was about {description} then the doctor and patient consultation discussion was {dialogue}\n"
                # Write the concatenated line to the text file
                output_file.write(concatenated_line)
    
    print("File written successfully - ", fileName)



