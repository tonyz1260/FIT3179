# import pandas as pd
# from fuzzywuzzy import fuzz

# # Load the CSV file into a DataFrame
# csv_file = 'D:\\MONASH\\Y4\\FIT3179\\DataVis\\FIT3179\\Week10Homework\\data\\International - Copy.csv'
# df_csv = pd.read_csv(csv_file)

# # Extract the 'Service_Country' column
# service_countries = df_csv['Port_Country'].tolist()

# # Load the JSON file and extract country names from 'properties.NAME'
# import json
# json_file = 'D:\\MONASH\\Y4\\FIT3179\\DataVis\\FIT3179\\Week10Homework\js\\ne_110m.json'

# with open(json_file, 'r', encoding='utf-8') as json_data:
#     data = json.load(json_data)
# # for key in data.keys():
# #     print(key)
#     json_countries = [feature['properties']['NAME'] for feature in data['objects']['ne_110m_admin_0_countries']['geometries']]

# # Initialize a list to store unmatched countries
# unmatched_countries = set()

# # Iterate through service_countries and try to find a match in json_countries
# for service_country in service_countries:
#     match_found = False
#     for json_country in json_countries:
#         similarity_ratio = fuzz.ratio(service_country, json_country)
#         if similarity_ratio >= 99:  # Adjust the threshold as needed
#             match_found = True
#             break
#     if not match_found:
#         unmatched_countries.add(service_country)
#         unmatched_countries.add(json_country)

# # Print unmatched countries
# print("Unmatched Countries:")
# for country in unmatched_countries:
#     print(country)

# import pandas as pd

# # Load the CSV file
# df = pd.read_csv('D:\MONASH\Y4\FIT3179\DataVis\FIT3179\Week9Homework\data\International.csv')

# # Filter the DataFrame for Year 2022
# df_2022 = df[df['Year'] == 2022]

# # Group by 'Service_Country' and sum the 'All_Flights' column
# flights_count = df_2022.groupby('Service_Country')['All_Flights'].sum().reset_index()

# # Rename the 'All_Flights' column to represent the total count
# flights_count.rename(columns={'All_Flights': 'Total_Flights'}, inplace=True)

# # Override the original CSV with the filtered data
# flights_count.to_csv('D:\MONASH\Y4\FIT3179\DataVis\FIT3179\Week9Homework\data\International.csv', index=False)


# import pandas as pd

# # Read the CSV file into a DataFrame
# df = pd.read_csv('D:\\MONASH\\Y4\\FIT3179\\DataVis\\FIT3179\\Week10Homework\\data\\InternationalTotalFlights.csv')

# # Filter inbound and outbound data separately
# inbound_data = df[df['In_Out'] == 'I']
# outbound_data = df[df['In_Out'] == 'O']

# # Group by Australian City and Year for inbound flights and calculate the total flights
# inbound_grouped = inbound_data.groupby(['Australian_City', 'Year'])['All_Flights'].sum().reset_index()

# # Group by Australian City and Year for outbound flights and calculate the total flights
# outbound_grouped = outbound_data.groupby(['Australian_City', 'Year'])['All_Flights'].sum().reset_index()

# # Create a new DataFrame to store the results
# results_df = pd.DataFrame(columns=['Type', 'Australian_City', 'Total_Flights', 'Year'])

# # Add inbound results to the new DataFrame
# for index, row in inbound_grouped.iterrows():
#     results_df = results_df.append({'Type': 'Inbound', 'Australian_City': row['Australian_City'], 'Total_Flights': row['All_Flights'], 'Year': row['Year']}, ignore_index=True)

# # Add outbound results to the new DataFrame
# for index, row in outbound_grouped.iterrows():
#     results_df = results_df.append({'Type': 'Outbound', 'Australian_City': row['Australian_City'], 'Total_Flights': row['All_Flights'], 'Year': row['Year']}, ignore_index=True)

# # Save the results to a new CSV file
# results_df.to_csv('D:\\MONASH\\Y4\\FIT3179\\DataVis\\FIT3179\\Week10Homework\\data\\InternationalTotalFlights.csv', index=False)


import pandas as pd
import json
import requests

# # Read the CSV file into a Pandas DataFrame
# df = pd.read_csv('D:\\MONASH\\Y4\\FIT3179\\DataVis\\FIT3179\\Week10Homework\\data\\International - Copy.csv')

# # Filter the DataFrame for Year 2022
# df_2022 = df[df['Year'] == 2022]

# # Initialize an empty list to store the unique city pairs
# unique_city_pairs = []

# # Iterate through each row in the DataFrame
# for index, row in df_2022.iterrows():
#     # Split the international cities by comma
#     international_cities = row['International_City'].split(', ')
#     for international_city in international_cities:
#         city_pair = (row['Australian_City'], international_city, row['Port_Country'])
#         if city_pair not in unique_city_pairs:
#             unique_city_pairs.append(city_pair)

# # Create a new DataFrame from the unique city pairs list
# result_df = pd.DataFrame(unique_city_pairs, columns=['Australian_City', 'International_City', 'Port_Country'])

# # Add the year column
# result_df['Year'] = 2022

# # Load the JSON data
# # with open('D:\\MONASH\\Y4\\FIT3179\\DataVis\\FIT3179\\Week10Homework\\js\\ne_110m.json', 'r', encoding='utf-8') as json_file:
# #     data = json.load(json_file)

# # # Extract LATITUDE and LONGITUDE from JSON data and merge with result_df
# # result_df['LATITUDE'] = result_df['International_City'].apply(lambda city: next((item['properties']['LATITUDE'] for item in data['objects']['ne_110m_populated_places']['geometries'] if item['properties']['NAME'] == city), None))
# # result_df['LONGITUDE'] = result_df['International_City'].apply(lambda city: next((item['properties']['LONGITUDE'] for item in data['objects']['ne_110m_populated_places']['geometries'] if item['properties']['NAME'] == city), None))

# def get_latitude_longitude(city_name, country_name):
#     if city_name == "PhUnited Kingdomet":
#         city_name = "Phuket"
#     if city_name == "Noumea":
#         country_name = "FR"
#     api_url = "https://api.api-ninjas.com/v1/geocoding?city=" + city_name + "&country=" + country_name
#     response = requests.get(api_url, headers={'X-Api-Key': 'sW/J27nTI29xb1E1++5vWQ==7zR6aNGudVQbp6lK'})
#     if response.status_code == 200:
#         data = response.json()
#         print(data)
#         return data[0].get('latitude'), data[0].get('longitude')
#     else:
#         print("Error:", response.status_code, response.text)
#         return None, None


# # Add columns for FROM_LATITUDE and FROM_LONGITUDE
# result_df['FROM_LATITUDE'], result_df['FROM_LONGITUDE'] = zip(*result_df.apply(lambda row: get_latitude_longitude(row['Australian_City'], 'Australia'), axis=1))

# # Add columns for TO_LATITUDE and TO_LONGITUDE
# result_df['TO_LATITUDE'], result_df['TO_LONGITUDE'] = zip(*result_df.apply(lambda row: get_latitude_longitude(row['International_City'], row['Port_Country']), axis=1))

# # Write the unique cities to a new CSV file
# result_df.to_csv('D:\\MONASH\\Y4\\FIT3179\\DataVis\\FIT3179\\Week10Homework\\data\\uniqueInternationalCity2022.csv', index=False)

# # # import requests

# # city = "Melbourne"
# # api_url = 'https://api.api-ninjas.com/v1/geocoding?city=' + city
# # response = requests.get(api_url, headers={'X-Api-Key': 'sW/J27nTI29xb1E1++5vWQ==7zR6aNGudVQbp6lK'})
# # if response.status_code == requests.codes.ok:
# #     print(response.text)
# # else:
# #     print("Error:", response.status_code, response.text)


# import pandas as pd

# # Read the CSV file
# df = pd.read_csv('D:\\MONASH\\Y4\\FIT3179\\DataVis\\FIT3179\\Week10Homework\\data\\International - Copy.csv')

# # Filter the data for the desired years (2003-2022)
# df_filtered = df[(df['Year'] >= 2003) & (df['Year'] <= 2022)]

# # Group by Australian City, International City, Port Country, and Year
# grouped = df_filtered.groupby(['Australian_City', 'International_City', 'Port_Country', 'Year']).size().reset_index()

# # Rename the columns
# grouped.columns = ['Australian City', 'International City', 'Port Country', 'Year', 'Count']

# # Save the result to a new CSV file
# grouped.to_csv('D:\\MONASH\\Y4\\FIT3179\\DataVis\\FIT3179\\Week10Homework\\data\\uniqueInternationalCity.csv', index=False, columns=['Australian_City', 'International_City', 'Port_Country', 'Year'])


# import pandas as pd
# import requests

# # Read the CSV file
# df = pd.read_csv('D:\\MONASH\\Y4\\FIT3179\\DataVis\\FIT3179\\Week10Homework\\data\\International - Copy.csv')

# # Filter the data for the desired years (2003-2022)
# df_filtered = df[(df['Year'] >= 2003) & (df['Year'] <= 2022)]

# # Group by Australian City, International City, Port Country, and Year
# grouped = df_filtered.groupby(['Australian_City', 'International_City', 'Port_Country', 'Year']).size().reset_index()

# # Rename the columns
# grouped.columns = ['Australian_City', 'International_City', 'Port_Country', 'Year', 'Count']

# # Save the result to a new CSV file
# grouped.to_csv('D:\\MONASH\\Y4\\FIT3179\\DataVis\\FIT3179\\Week10Homework\\data\\uniqueInternationalCityFirst.csv', index=False, columns=['Australian_City', 'International_City', 'Port_Country', 'Year'])


# # Read the first CSV file
# df_first_requirement = pd.read_csv('D:\\MONASH\\Y4\\FIT3179\\DataVis\\FIT3179\\Week10Homework\\data\\uniqueInternationalCityFirst.csv')

# print(df_first_requirement)

# # Create a dictionary to store latitude and longitude information
# city_coordinates = {}

# def get_coordinates(city, country):
#     if city == "PhUnited Kingdomet":
#         city = "Phuket"
#     if city == "Noumea":
#         country = "FR"
#     print(city, country)
#     if (city, country) in city_coordinates:
#         return city_coordinates[(city, country)]
#     else:
#         # Replace 'YOUR_API_ENDPOINT' with the actual API endpoint
#         api_url = "https://api.api-ninjas.com/v1/geocoding?city=" + city + "&country=" + country
#         response = requests.get(api_url, headers={'X-Api-Key': 'sW/J27nTI29xb1E1++5vWQ==7zR6aNGudVQbp6lK'})
#         if response.status_code != 200:
#             print("Error:", response.status_code, response.text)
#             return (None, None)
#         data = response.json()
#         try:
#             print(data)
#         except (UnicodeEncodeError, UnicodeDecodeError):
#             print("Unicode Error with " + city + ", " + country)
#         if len(data) == 0:
#             print(data)
#             return (None, None)
#         if 'latitude' in data[0] and 'longitude' in data[0]:
#             coordinates = (data[0]['latitude'], data[0]['longitude'])
#             city_coordinates[(city, country)] = coordinates
#             return coordinates
#         else:
#             return (None, None)

# # Function to fetch coordinates for Australian cities
# def get_from_coordinates(row):
#     return get_coordinates(row['Australian_City'], 'Australia')

# # Function to fetch coordinates for International cities
# def get_to_coordinates(row):
#     return get_coordinates(row['International_City'], row['Port_Country'])

# # Apply the functions to fetch coordinates
# df_first_requirement['FROM_LATITUDE'], df_first_requirement['FROM_LONGITUDE'] = zip(*df_first_requirement.apply(get_from_coordinates, axis=1))
# df_first_requirement['TO_LATITUDE'], df_first_requirement['TO_LONGITUDE'] = zip(*df_first_requirement.apply(get_to_coordinates, axis=1))


# # Save the result to a new CSV file
# df_first_requirement.to_csv('D:\\MONASH\\Y4\\FIT3179\\DataVis\\FIT3179\\Week10Homework\\data\\uniqueInternationalCity.csv', index=False, columns=['Australian_City', 'International_City', 'Port_Country', 'Year', 'FROM_LATITUDE', 'FROM_LONGITUDE', 'TO_LATITUDE', 'TO_LONGITUDE'])


import pandas as pd

# Read the CSV file into a pandas DataFrame
df = pd.read_csv('D:\\MONASH\\Y4\\FIT3179\\DataVis\\FIT3179\\Week10Homework\\data\\International - Copy.csv')

# Group the data by Year and Port_Country, and then sum the number of flights for each group
result = df.groupby(['Year', 'Port_Country'])['All_Flights'].sum().reset_index()

# Create a new DataFrame for the final output
output_df = pd.DataFrame(columns=['Country', 'Total_Flights', 'Year'])

# Loop through the unique years and populate the output DataFrame
unique_years = result['Year'].unique()

for year in unique_years:
    year_data = result[result['Year'] == year]
    for _, row in year_data.iterrows():
        output_df = output_df.append({'Country': row['Port_Country'], 'Total_Flights': row['All_Flights'], 'Year': year}, ignore_index=True)

# Write the output DataFrame to a new CSV file
output_df.to_csv('D:\\MONASH\\Y4\\FIT3179\\DataVis\\FIT3179\\Week10Homework\\data\\International.csv', index=False)

