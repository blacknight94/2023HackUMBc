import requests
import re


user_input = input("Enter part of the URL (e.g., 'AAPL/sustainability'): ")



# Define the URL of the webpage you want to download
url = f'https://finance.yahoo.com/quote/{user_input}/sustainability'  # Replace with the URL of the webpage you want to download

# Set the User-Agent header to mimic Mozilla Firefox
headers = {'User-Agent': 'Mozilla/5.0'}

try:
	# Send an HTTP GET request to the URL with the specified User-Agent
  response = requests.get(url, headers=headers)

    	# Check if the request was successful (status code 200)
	if response.status_code == 200:
		# Get the HTML content of the page
		html_content = response.text

		# Define the target string
		target_string = '<div class="D(ib) Fz(23px) smartphone_Fz(22px) Fw(600)">'
		
		level = 0
		# Use regular expression to find and print the content between the target string and the next '<' for the first 3 instances
		for match in re.finditer(re.escape(target_string), html_content):
			start_index = match.end()
			end_index = html_content.find('<', start_index)

			if end_index != -1:
				content_between = html_content[start_index:end_index]
				if(level == 0):
					print("Environment Risk Score")
				elif(level == 1):
					print("Social Risk Score")
				else:
					print("Governance Risk Score")
				level;
				print(f"	Instance {match.start() // len(target_string) + 1}: {content_between}")
			else:
				print(f"Instance {match.start() // len(target_string) + 1}: Content not found after target string.")

			# Stop after the first 3 instances
			if match.start() // len(target_string) == 2:
				break
			
		print("Total ESG Risk score")
		target_string = '<div class="Fz(36px) Fw(600) D(ib) Mend(5px)">'
		for match in re.finditer(re.escape(target_string), html_content):
			start_index = match.end()
			end_index = html_content.find('<', start_index)
			if end_index != -1:
				content_between = html_content[start_index:end_index]
				print(f"	Instance {match.start() // len(target_string) + 1}: {content_between}")
			else:
				print(f"Instance {match.start() // len(target_string) + 1}: Content not found after target string.")


	else:
        	print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {str(e)}")






