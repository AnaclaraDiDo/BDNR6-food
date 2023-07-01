import pandas as pd

# Read the original CSV file
df = pd.read_csv("data_part_3_10000.csv")

# Create a new DataFrame to store the extracted ingredients
new_df = pd.DataFrame(columns=["RecipeId", "Ingredient"])

# Iterate over each row in the original DataFrame
for index, row in df.iterrows():
    recipe_id = row["RecipeId"]
    ingredients = row["RecipeIngredientParts"].strip("c()").replace('"', "").split(", ")

    # Create a DataFrame with the current recipe's ingredients
    recipe_df = pd.DataFrame(
        {"RecipeId": [recipe_id] * len(ingredients), "Ingredient": ingredients}
    )

    # Concatenate the recipe DataFrame with the new_df
    new_df = pd.concat([new_df, recipe_df], ignore_index=True)

# Save the new DataFrame to a new CSV file
new_df.to_csv("extracted_ingredients_10000.csv", index=False)
