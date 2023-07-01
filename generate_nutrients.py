import csv

nutrients = [
    "Calories",
    "SaturatedFatContent",
    "SodiumContent",
    "CarbohydrateContent",
    "FiberContent",
    "SugarContent",
    "ProteinContent",
]

filename = "nutrients.csv"

with open(filename, "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Nutrients"])  # Write the header row

    for nutrient in nutrients:
        writer.writerow([nutrient])

print("CSV file generated successfully.")
