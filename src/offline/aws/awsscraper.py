# scrapes AWS resource type and action mapping from AWS docs

import json
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.opera.options import Options
from selenium.webdriver.firefox.options import Options

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')

# takes in a URL to a IAM service's actions, resources, and condition keys list and scrapes the tables
def get_tables(url):
	# browser = webdriver.Chrome(options = options)
	# browser = webdriver.Opera(options = options, executable_path = './operadriver')
	browser = webdriver.Firefox(options = options, executable_path = './geckodriver')
	
	browser.get(url)
	time.sleep(5)
	wait = WebDriverWait(browser, 10)

	try:
		# wait for all the JSON elements to load before scraping.
		wait.until(EC.presence_of_element_located((By.TAG_NAME, 'awsdocs-view')))	
	except TimeoutError:
		pass

	else:
		# get IAM service name and tables
		namespace = browser.find_elements_by_xpath("//div[@id='main-col-body']/p/code")[0].text
		tables = browser.find_elements_by_tag_name('table')
		
		if len(tables) > 0:
			# first table is the list of actions
			actions = tables[0].find_elements(By.TAG_NAME, 'tr') 
			
			# second table is the list of resource types
			if len(tables) > 1:
				resources = tables[1].find_elements(By.TAG_NAME, 'tr')
		
		namespace_json = dict()
		
		if len(tables) > 0:
			previous_name = ''
			
			# store resource type -> actions mapping
			for action in actions:
				fields = list(action.find_elements_by_tag_name('td'))

				if len(fields) == 3:
					resource_type = str(fields[0].text.replace('*', ''))
					
					if resource_type in namespace_json:
						namespace_json[resource_type].append(previous_name)
					else:
						namespace_json[resource_type] = [previous_name]
				
				elif len(fields) > 3:
					resource_type = str(fields[3].text.replace('*', ''))
					action_name = fields[0].text.replace(' [permission only]', '')
					action_name = action_name.lower()
					
					if resource_type in namespace_json:
						namespace_json[resource_type].append(action_name)
					else:
						namespace_json[resource_type] = [action_name]
						
					previous_name = action_name

		# save the constraints
		actions_json[namespace] = namespace_json
		namespace_json = dict()
			
		#if there is a resource type, scrape it and its ARN format
		if len(tables) > 1:
			for resource in resources:
				fields = list(resource.find_elements_by_tag_name('td'))
				
				if len(fields) > 1:
					namespace_json[fields[0].text] = fields[1].text

		# save the constraints
		resources_json[namespace] = namespace_json
	
	finally:
		browser.close()

# browser = webdriver.Chrome(options = options)
# browser = webdriver.Opera(options = options, executable_path = './operadriver')
browser = webdriver.Firefox(options = options, executable_path = './geckodriver')

# open the general page listing the actions, resource types, and condition keys for all IAM services.
aws_reference = 'https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_actions-resources-contextkeys.html'
browser.get(aws_reference)
wait = WebDriverWait(browser, 10)

try:
	# wait until page has fully loaded all the JSON elements
	wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'highlights'))) 
except:
	pass

actions_json = {}
resources_json = {}

# get list of all services
rows = browser.find_elements_by_xpath("//div[@id='main-col-body']/div[@class='highlights']/ul/li")

# iterate through services and scrape their tables
for row in rows:
	a_path = row.find_elements_by_tag_name('a')[0]
	url = a_path.get_attribute('href')
	get_tables(url)
	print('{}...done'.format(url))

browser.quit()

# dump constraints to files
file = open('actions.json', 'w')
file.write(json.dumps(actions_json, indent=4))
file.close()

file = open('resources.json', 'w')
file.write(json.dumps(resources_json, indent=4))
file.close()