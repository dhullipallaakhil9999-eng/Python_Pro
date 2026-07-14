import pandas as pd

# Excel file path
file_path = input("Enter Excel file path: ")

# Read Excel file
df = pd.read_excel(file_path)

# Ask how many columns to add
num_cols = int(input("How many new columns do you want to add? "))

new_columns = []

# Get column names from user
for i in range(num_cols):
    col_name = input(f"Enter name for column {i+1}: ")
    new_columns.append(col_name)

    # Create column if it doesn't exist
    if col_name not in df.columns:
        df[col_name] = ""

# Take input for each row
for index, row in df.iterrows():

    print("\n" + "=" * 40)
    print(f"Row {index + 1}")
    print("=" * 40)

    # Display current row data
    for column in df.columns:
        if column not in new_columns:
            print(f"{column}: {row[column]}")

    print()

    # Get values for new columns
    for col in new_columns:
        value = input(f"Enter value for '{col}': ")
        df.at[index, col] = value

# Save back to same Excel file
df.to_excel(file_path, index=False)

print("\nExcel updated successfully!")
