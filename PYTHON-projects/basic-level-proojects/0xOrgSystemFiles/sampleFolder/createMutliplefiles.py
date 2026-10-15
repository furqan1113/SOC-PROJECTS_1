import os
import random
import string

# Create test folder
test_folder = "sampleFolder"
os.makedirs(test_folder, exist_ok=True)

# Function to generate random content for files
def generate_random_content(extension):
    if extension == '.txt':
        return ''.join(random.choices(string.ascii_letters + string.digits + " \n", k=100))
    elif extension == '.jpg':
        return f"Fake image content for {extension}."
    elif extension == '.pdf':
        return "%PDF-1.4\n% Fake PDF content"
    elif extension == '.md':
        return "# Markdown file\nSample content for markdown file."
    elif extension == '.py':
        return "print('Sample Python code')"
    else:
        return "Some generic content"

# Extensions to create
extensions = ['.txt', '.jpg', '.pdf', '.md', '.py', '.exe', '.zip', '.html', '.csv', '.log', '.json']

# Number of files to generate
num_files = 100

# Generate files
for _ in range(num_files):
    # Randomly select a file extension
    ext = random.choice(extensions)
    
    # Generate a random file name
    filename = ''.join(random.choices(string.ascii_letters + string.digits, k=10)) + ext
    
    # Generate random content based on the extension
    content = generate_random_content(ext)
    
    # Write the content to the file
    with open(os.path.join(test_folder, filename), "w") as file:
        file.write(content)

print(f"Generated {num_files} test files in: {os.path.abspath(test_folder)}")
