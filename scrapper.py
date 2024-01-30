import requests
from bs4 import BeautifulSoup

# Function to fetch the HTML content of a webpage
def get_html(url):
    response = requests.get(url)
    return response.text

# Function to extract and write the text content from a specific div with attributes to a file
def extract_div_text_to_file(url, attributes, output_file):
    html_content = get_html(url)
    soup = BeautifulSoup(html_content, 'html.parser')

    # Find the specific div with the specified attributes
    target_div = soup.find('div', attributes)

    if target_div:
        # Extract text content and write it to the specified output file
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(target_div.get_text())
        print(f"Text content written to '{output_file}'.")
    else:
        print(f"Div with attributes {attributes} not found on the page.")

# Replace 'your_url_here' with the URL of the webpage you want to scrape
url_to_scrape = 'https://www.stclaircollege.ca/programs/ace-academic-career-entrance'

# Define the attributes of the div you want to extract
div_attributes = {'data-history-node-id': '10853', 'role': 'article', 'about': '/programs/ace-academic-career-entrance',
                  'class': 'node node--type-program-full-time node--view-mode-full tab-content', 'id': 'courseTabContent'}

# Replace 'output.txt' with the desired output file name
output_file = 'output.txt'

# Call the function with the URL, div attributes, and output file
extract_div_text_to_file(url_to_scrape, div_attributes, output_file)
