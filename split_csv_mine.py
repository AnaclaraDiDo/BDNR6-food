import csv

# Open the input file
with open("DATASET_DE_RECETAS/recipes.csv", "r") as input_file:
    # Create a CSV reader object
    reader = csv.reader(input_file)
    # Initialize a counter variable
    count = 0
    # Iterate over the rows in the input file
    with open("data_part_1.csv", "w") as output_file:
        # Create a CSV writer object
        writer = csv.writer(output_file)
        for row in reader:
            writer.writerow(row)
            count += 1

            # If the counter is equal to 1000, reset the counter
            if count == 100:
                break
                # count = 0
