import json
import re

# read the links_map
with open('links_map.json') as f:
    link_map = json.load(f)

# Function to replace only href links in the HTML file
def replace_href_links(file_path, replacements):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Regular expression to match only the href attributes containing the image file name
    pattern = re.compile(r'(href)="(Energy%20System%20Sector%20-%20Overview(?:%20[0-9a-zA-Z-]+)?/)([^"]+)"')

    # Function to replace the found matches based on the dictionary
    def replace_match(match):
        file_name = match.group(3)  # Extract the file name like 'lorenz_thumb.png'
        # Remove the file extension to match with the dictionary key
        base_name = file_name.split('.')[0]
        # Check if the base name is in the dictionary and replace it
        if base_name in replacements:
            new_link = replacements[base_name]
            # Replace the entire href value with the new link from the dictionary
            return f'{match.group(1)}="{new_link}"'
        return match.group(0)  # No replacement if not in the dictionary

    # Use sub function to replace all the matches for href attributes
    new_content = re.sub(pattern, replace_match, content)

    # Save the modified content back to the HTML file (or a new file if desired)
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(new_content)


# Replace the image links in your HTML file
replace_href_links('index.html', link_map)



# insert style_insertion
with open('style_insertion.txt', 'r', encoding='utf-8') as file:
    insertion = file.read()

to_be_replaced = """
body {
	margin: 0;
	padding: 0;
}
@media only screen {
	body {
		margin: 2em auto;
		max-width: 900px;
		color: rgb(55, 53, 47);
	}
}
"""

def add_css_to_html(html_file, to_be_replaced, insertion):
    # Read the contents of the HTML file
    with open(html_file, 'r', encoding='utf-8') as file:
        content = file.read()

    # Insert the CSS code before the closing </head> tag
    updated_content = content.replace(to_be_replaced, insertion)

    # Write the updated content back to the HTML file
    with open(html_file, 'w', encoding='utf-8') as file:
        file.write(updated_content)

add_css_to_html('index.html', to_be_replaced, insertion)