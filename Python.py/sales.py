# Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load Excel file
file_path = "mytra and meesho data sets (1).xlsx"

# Read both sheets
myntra_df = pd.read_excel(file_path, sheet_name='myntra')
meesho_df = pd.read_excel(file_path, sheet_name='meesho')

# Display first few rows
print("Myntra Data:\n", myntra_df.head())
print("\nMeesho Data:\n", meesho_df.head())


# ==============================
# DATA PROCESSING
# ==============================

# Merge both datasets on product name
merged_df = pd.merge(
    myntra_df,
    meesho_df,
    on="products_Name",
    how="inner"
)

# Rename columns for clarity
merged_df.rename(columns={
    "myntra_sales": "Myntra",
    "meesho_sales": "Meesho"
}, inplace=True)

print("\nMerged Data:\n", merged_df)


# ==============================
# NUMPY ANALYSIS
# ==============================

# Convert sales into numpy arrays
myntra_sales = np.array(merged_df["Myntra"])
meesho_sales = np.array(merged_df["Meesho"])

# Calculate statistics
print("\n--- NumPy Analysis ---")
print("Myntra Total Sales:", np.sum(myntra_sales))
print("Meesho Total Sales:", np.sum(meesho_sales))

print("Myntra Average Sales:", np.mean(myntra_sales))
print("Meesho Average Sales:", np.mean(meesho_sales))


# ==============================
# MATPLOTLIB VISUALIZATION
# ==============================

# Bar chart comparison
x = np.arange(len(merged_df["products_Name"]))

plt.figure()
plt.bar(x - 0.2, merged_df["Myntra"], width=0.4, label="Myntra")
plt.bar(x + 0.2, merged_df["Meesho"], width=0.4, label="Meesho")

plt.xticks(x, merged_df["products_Name"], rotation=30)
plt.xlabel("Product Categories")
plt.ylabel("Sales")
plt.title("Myntra vs Meesho Sales Comparison")
plt.legend()

plt.tight_layout()
plt.show()


# ==============================
# PIE CHART (TOTAL SHARE)
# ==============================

total_sales = [
    np.sum(myntra_sales),
    np.sum(meesho_sales)
]

labels = ["Myntra", "Meesho"]

plt.figure()
plt.pie(total_sales, labels=labels, autopct='%1.1f%%')
plt.title("Market Share Comparison")
plt.show()
