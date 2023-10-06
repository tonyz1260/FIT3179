# import pandas as pd
# from fuzzywuzzy import fuzz

# # Load the CSV file into a DataFrame
# csv_file = 'D:\MONASH\Y4\FIT3179\DataVis\FIT3179\Week9Homework\data\International.csv'
# df_csv = pd.read_csv(csv_file)

# # Extract the 'Service_Country' column
# service_countries = df_csv['Service_Country'].tolist()

# # Load the JSON file and extract country names from 'properties.NAME'
# import json
# json_file = 'D:\MONASH\Y4\FIT3179\DataVis\FIT3179\Week9Homework\js\\ne_110m.json'

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


import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv('D:\\MONASH\\Y4\\FIT3179\\DataVis\\FIT3179\\Week10Homework\\data\\InternationalTotalFlights.csv')

# Filter inbound and outbound data separately
inbound_data = df[df['In_Out'] == 'I']
outbound_data = df[df['In_Out'] == 'O']

# Group by Australian City and Year for inbound flights and calculate the total flights
inbound_grouped = inbound_data.groupby(['Australian_City', 'Year'])['All_Flights'].sum().reset_index()

# Group by Australian City and Year for outbound flights and calculate the total flights
outbound_grouped = outbound_data.groupby(['Australian_City', 'Year'])['All_Flights'].sum().reset_index()

# Create a new DataFrame to store the results
results_df = pd.DataFrame(columns=['Type', 'Australian_City', 'Total_Flights', 'Year'])

# Add inbound results to the new DataFrame
for index, row in inbound_grouped.iterrows():
    results_df = results_df.append({'Type': 'Inbound', 'Australian_City': row['Australian_City'], 'Total_Flights': row['All_Flights'], 'Year': row['Year']}, ignore_index=True)

# Add outbound results to the new DataFrame
for index, row in outbound_grouped.iterrows():
    results_df = results_df.append({'Type': 'Outbound', 'Australian_City': row['Australian_City'], 'Total_Flights': row['All_Flights'], 'Year': row['Year']}, ignore_index=True)

# Save the results to a new CSV file
results_df.to_csv('D:\\MONASH\\Y4\\FIT3179\\DataVis\\FIT3179\\Week10Homework\\data\\InternationalTotalFlights.csv', index=False)