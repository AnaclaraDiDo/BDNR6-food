import csv

input_filename = "data_part_3_10000.csv"
output_filename = "extraceted_nutrients_10000.csv"
columns = [
    "Calories",
    "SaturatedFatContent",
    "SodiumContent",
    "CarbohydrateContent",
    "FiberContent",
    "SugarContent",
    "ProteinContent",
    "RecipeId",
]

with open(input_filename, "r") as input_file, open(
    output_filename, "w", newline=""
) as output_file:
    reader = csv.DictReader(input_file)
    rows = list(reader)  # Read all rows into a list

    writer = csv.DictWriter(output_file, fieldnames=columns)
    writer.writeheader()

    for row in rows[:-1]:  # Exclude the last row
        output_row = {column: row[column] for column in columns}
        writer.writerow(output_row)

print("CSV file generated successfully.")
