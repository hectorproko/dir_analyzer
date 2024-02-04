import os
import tkinter as tk
import matplotlib.pyplot as plt
from tkinter import filedialog

root = tk.Tk()  # Create a temporary root window
root.withdraw()  # Hide the root window

#folder_path = filedialog.askdirectory()  # Prompt user to select a folder
folder_path = "C:/Users/Hecti/Downloads"

# Initialize variables to store file types and sizes
file_types = {}
total_size = 0

# Iterate through all files and folders in the directory
for root, _, files in os.walk(folder_path):
    for file in files:
        # Get file path and size
        file_path = os.path.join(root, file)
        file_size = os.path.getsize(file_path)

        # Extract file extension (if any)
        file_type = os.path.splitext(file)[1].lower()  # Convert to lowercase

        # Update file type dictionary
        if file_type in file_types:
            file_types[file_type] += file_size
        else:
            file_types[file_type] = file_size

        # Update total size
        total_size += file_size

# Calculate percentages for each file type
file_type_percentages = {
    file_type: (size / total_size) * 100 for file_type, size in file_types.items()
}

# Filter out file types with 0.00% contribution
filtered_percentages = {file_type: percent for file_type, percent in file_type_percentages.items() if percent > 0.00}

# Sort file types by percentage in descending order
file_types_sorted = sorted(filtered_percentages.items(), key=lambda item: item[1], reverse=True)

# Create bar chart data and labels
bar_chart_labels = [f"{file_type} ({percent:.2f}%)" for file_type, percent in file_types_sorted]
bar_chart_data = [percent for _, percent in file_types_sorted]

# Create horizontal bar chart
plt.figure(figsize=(10, 6))
plt.barh(bar_chart_labels, bar_chart_data, color=['skyblue', 'lightgreen', 'gold', 'lightcoral'])
plt.xlabel("Percentage of Total Size")
plt.ylabel("File Type")
plt.title("Horizontal Bar Chart of File Types by Size")
plt.tight_layout()
plt.show()

