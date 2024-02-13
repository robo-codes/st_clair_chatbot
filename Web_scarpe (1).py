import requests
from bs4 import BeautifulSoup

# Function to fetch the HTML content of a webpage
def get_html(url):
    response = requests.get(url)
    return response.text

# Function to extract and append the text content from specific divs with attributes to a file
def extract_and_append_text_to_file(url, div_attributes, additional_classes, output_file):
    html_content = get_html(url)
    soup = BeautifulSoup(html_content, 'html.parser')

    # Find the specific div with the specified attributes
    target_div = soup.find('div', div_attributes)

    if target_div:
        # Initialize text content with class values
        text_content = '\n'.join([soup.find(class_=class_name).get_text() for class_name in additional_classes])

        # Append text content from the main div
        text_content += '\n\n' + target_div.get_text()

        # Write the combined text content to the specified output file
        with open(output_file, 'a', encoding='utf-8') as file:
            file.write(text_content)
        print(f"Text content written to '{output_file}'.")
    else:
        print(f"Div with attributes {div_attributes} not found on the page.")


url_to_scrape = 'https://www.stclaircollege.ca/programs/ace-cep' #Replace the url with the one you want to scrape(course)


# Define the attributes of the main div you want to extract
div_attributes = {'data-history-node-id': '10898', 'about': '/programs/ace-cep'} # Change the id and about by clicking on inspect

# Define additional classes whose text content you want to extract
additional_classes = ['breadcrumb-item active', 'progInfo--details']

# Replace 'output.txt' with the desired output file name
output_file = 'output.txt'

# Call the function with the URL, div attributes, additional classes, and output file
extract_and_append_text_to_file(url_to_scrape, div_attributes, additional_classes, output_file)
