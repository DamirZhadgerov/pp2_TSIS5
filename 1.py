import re

# Provide the full path to the file
file_path = r'C:\Users\Damir\OneDrive\Рабочий стол\row.txt'

# Open and read the file with utf-8 encoding
with open(file_path, 'r', encoding='utf-8') as file:
    data = file.read()

# Define the pattern
pattern = 'ab*'

# Find matches
matches = re.findall(pattern, data)

# Print matches
for match in matches:
    print(match)
