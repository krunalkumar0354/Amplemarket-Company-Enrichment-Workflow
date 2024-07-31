import os
import json
import requests
from hubspot import HubSpot

def main(event):
  # Use inputs to get data from any action in your workflow and use it in your code instead of having to use the HubSpot API.
  amplemarket_api_key = os.getenv('Amplemarket')

  # Extract email from the event data
  domain = event.get('inputFields').get('domain')
  
  if not amplemarket_api_key:
    print("Amplemarket API key is missing.")
    return

  if not domain:
    print("Domain is missing from the input fields.")
    return
  
  url = "https://api.amplemarket.com/companies/find"
  querystring = {"domain": domain}
  headers = {"Authorization": f"Bearer {amplemarket_api_key}"}
  
  response = requests.get(url, headers=headers, params=querystring)
  # Check for successful response
  if response.status_code == 200:
    company_data = response.json()
    return {
    "outputFields": {
      'id': company_data.get('id'),
      'object': company_data.get('object'),
      'name': company_data.get('name'),
      'website': company_data.get('website'),
      'linkedin_url': company_data.get('linkedin_url'),
      'keywords': company_data.get('keywords'),
      'estimated_number_of_employees': company_data.get('estimated_number_of_employees'),
      'size': company_data.get('size'),
      'industry': company_data.get('industry'),
      'logo_url': company_data.get('logo_url'),
      'location': company_data.get('location'),
      'city': company_data.get('location_details')['city'],
      'state': company_data.get('location_details')['state'],
      'country': company_data.get('location_details')['country'],
      'overview': company_data.get('overview'),
      'followers': company_data.get('followers'),
      'founded_year': company_data.get('founded_year'),
      'traffic_rank': company_data.get('traffic_rank'),
      'sic_codes': company_data.get('sic_codes'),
      'naics_codes': company_data.get('naics_codes'),
      'type': company_data.get('type'),
      'total_funding': company_data.get('total_funding'),
      'latest_funding_stage': company_data.get('latest_funding_stage'),
      'latest_funding_date': company_data.get('latest_funding_date'),
      'is_b2b': company_data.get('is_b2b'),
      'is_b2c': company_data.get('is_b2c'),
      'technologies': ', '.join(company_data.get('technologies')),
      'department_headcount':company_data.get('department_headcount'),
      'job_function_headcount': company_data.get('job_function_headcount'),
      'estimated_revenue': company_data.get('estimated_revenue')
    }
    }
  else:
    print(f"Error: {response.status_code}, {response.json()}")
  # Return the output data that can be used in later actions in your workflow.