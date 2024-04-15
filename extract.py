import requests

# Function to extract text after 'uri=' and remove text after space
def extract_text(line):
    # Find the index of 'uri=' in the line
    index = line.find('uri=')
    # If 'uri=' is found
    if index != -1:
        # Extract text after 'uri='
        extracted_text = line[index + 4:].strip()
        # Find the index of the first space in the extracted text
        space_index = extracted_text.find(' ')
        # If a space is found
        if space_index != -1:
            # Extract text before the first space
            extracted_text = extracted_text[:space_index].strip()
        return extracted_text
    return None

# Get URL input from user
url = input("Enter the URL of the text file: ")

# Fetch the content of the text file from the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Split the content into lines
    lines = response.text.split('\n')
    # Iterate through each line
    for line in lines:
        # Extract text after 'uri=' and remove text after space
        extracted_text = extract_text(line)
        # Print the extracted text if it's not None
        if extracted_text:
            print(extracted_text)
else:
    print("Failed to fetch the content. Please make sure the URL is correct.")
