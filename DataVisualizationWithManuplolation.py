import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Generate some random data
np.random.seed(0)
data = {
    'Year': np.arange(2010, 2020),
    'Revenue': np.random.randint(100, 1000, 10),
    'Profit': np.random.randint(50, 500, 10)
}
df = pd.DataFrame(data)

# Plotting a bar chart
plt.figure(figsize=(8, 6))
plt.bar(df['Year'], df['Revenue'], color='skyblue', label='Revenue')
plt.xlabel('Year')
plt.ylabel('Amount ($)')
plt.title('Revenue Over Years')
plt.legend()
plt.grid(True)
plt.xticks(df['Year'])  # Show all years on x-axis
plt.tight_layout()
plt.show()

# Plotting a line chart
plt.figure(figsize=(8, 6))
plt.plot(df['Year'], df['Profit'], marker='o', color='orange', label='Profit')
plt.xlabel('Year')
plt.ylabel('Amount ($)')
plt.title('Profit Over Years')
plt.legend()
plt.grid(True)
plt.xticks(df['Year'])  # Show all years on x-axis
plt.tight_layout()
plt.show()
