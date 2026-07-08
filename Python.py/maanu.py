import numpy as np
import matplotlib.pyplot as plt

x = np.arange(len(merged_df["products_Name"]))

plt.figure()
plt.bar(x - 0.2, merged_df["Myntra"], width=0.4, label="Myntra")
plt.bar(x + 0.2, merged_df["Meesho"], width=0.4, label="Meesho")

plt.xticks(x, merged_df["products_Name"], rotation=30)
plt.xlabel("Products")
plt.ylabel("Sales")
plt.title("Myntra vs Meesho Sales Comparison")
plt.legend()

plt.show()
