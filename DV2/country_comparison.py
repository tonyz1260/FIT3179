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


# import pandas as pd
# import json
# import requests

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


# import pandas as pd

# # Read the CSV file into a pandas DataFrame
# df = pd.read_csv('D:\\MONASH\\Y4\\FIT3179\\DataVis\\FIT3179\\Week10Homework\\data\\International - Copy.csv')

# # Group the data by Year and Port_Country, and then sum the number of flights for each group
# result = df.groupby(['Year', 'Port_Country'])['All_Flights'].sum().reset_index()

# # Create a new DataFrame for the final output
# output_df = pd.DataFrame(columns=['Country', 'Total_Flights', 'Year'])

# # Loop through the unique years and populate the output DataFrame
# unique_years = result['Year'].unique()

# for year in unique_years:
#     year_data = result[result['Year'] == year]
#     for _, row in year_data.iterrows():
#         output_df = output_df.append({'Country': row['Port_Country'], 'Total_Flights': row['All_Flights'], 'Year': year}, ignore_index=True)

# # Write the output DataFrame to a new CSV file
# output_df.to_csv('D:\\MONASH\\Y4\\FIT3179\\DataVis\\FIT3179\\Week10Homework\\data\\International.csv', index=False)


# import pandas as pd

# # Read the CSV file into a pandas DataFrame
# df = pd.read_csv('D:\\MONASH\\Y4\\FIT3179\\DataVis\\FIT3179\\DV2\\data\\International - Copy.csv')

# # Group the data by Year, Australian City, and Service Region and calculate the total flights
# grouped = df.groupby(['Year', 'Australian_City', 'Service_Region'])['All_Flights'].sum().reset_index()

# # Calculate the total flights for each year
# total_flights_by_year = df.groupby('Year')['All_Flights'].sum().reset_index()
# total_flights_by_year.rename(columns={'All_Flights': 'Total_All_Flights'}, inplace=True)

# # Merge the grouped data with total flights by year
# result = pd.merge(grouped, total_flights_by_year, on='Year')

# # Calculate the percentage of flights for each row
# result['Percentage'] = (result['All_Flights'] / result['Total_All_Flights']) * 100

# # # Rename columns
# # result.rename(columns={'Australian_City': 'First Column', 'Service_Region': 'Second Column',
# #                       'All_Flights': 'Third Column', 'Year': 'Fourth Column',
# #                       'Percentage': 'Last Column'}, inplace=True)

# # Save the result to a new CSV file
# result.to_csv('D:\\MONASH\\Y4\\FIT3179\\DataVis\\FIT3179\\DV2\\data\\InternationalFlightRatio.csv', index=False)


# import pandas as pd

# # Load the first CSV file into a DataFrame
# df1 = pd.read_csv('D:\\MONASH\\Y4\\FIT3179\\DataVis\\FIT3179\\DV2\\data\\InternationalTotalFlights.csv')

# # Load the second CSV file into a DataFrame
# df2 = pd.read_csv('D:\\MONASH\\Y4\\FIT3179\\DataVis\\FIT3179\\DV2\\data\\au.csv')

# # Merge the two DataFrames based on the 'Australian_City' and 'city' columns
# merged_df = pd.merge(df1, df2[['city', 'admin_name']], left_on='Australian_City', right_on='city', how='left')

# # Drop the 'city' column from the merged DataFrame (if needed)
# merged_df.drop(columns=['city'], inplace=True)

# # Save the merged DataFrame back to the first CSV file
# merged_df.to_csv('D:\\MONASH\\Y4\\FIT3179\\DataVis\\FIT3179\\DV2\\data\\InternationalTotalFlights.csv', index=False)

# print("Merged file saved successfully!")


# import pandas as pd

# # Load the merged CSV file into a DataFrame
# merged_df = pd.read_csv('D:\\MONASH\\Y4\\FIT3179\\DataVis\\FIT3179\\DV2\\data\\InternationalTotalFlights.csv')

# # Group the DataFrame by 'admin_name' and 'Year' and calculate the sum of 'Total_Flights'
# grouped_df = merged_df.groupby(['admin_name', 'Year'])['Total_Flights'].sum().reset_index()

# # Merge the grouped DataFrame with the original merged DataFrame
# merged_df = pd.merge(merged_df, grouped_df, on=['admin_name', 'Year'], how='left', suffixes=('', '_yearly_total'))

# # Rename the newly added column to 'Total_Flights_Yearly'
# merged_df.rename(columns={'Total_Flights_yearly_total': 'Total_Flights_Yearly'}, inplace=True)

# # Calculate the total flight count for Australia per year
# australia_total_per_year = merged_df.groupby('Year')['Total_Flights'].sum().reset_index()
# australia_total_per_year.rename(columns={'Total_Flights': 'Australia_Total_Flights_Yearly'}, inplace=True)

# # Merge the Australia total flight count DataFrame with the original merged DataFrame
# merged_df = pd.merge(merged_df, australia_total_per_year, on='Year', how='left')



# # Save the updated DataFrame back to the merged CSV file
# merged_df.to_csv('D:\\MONASH\\Y4\\FIT3179\\DataVis\\FIT3179\\DV2\\data\\InternationalTotalFlights.csv', index=False)

# print("Updated merged file saved successfully!")


# import pandas as pd

# # Read the CSV file into a DataFrame
# df = pd.read_csv('D:\\MONASH\\Y4\\FIT3179\\DataVis\\FIT3179\\DV2\\data\\Arrivals-international_students.csv', thousands=',')

# # # Calculate the percentages
# # for col in df.columns[1:]:
# #     df[col] = (df[col] / df[col].sum()) * 100

# # # Rename the 'Student_visa' column for clarity
# # df = df.rename(columns={'Student_visa': 'Visa_Category'})

# df.to_csv('D:\\MONASH\\Y4\\FIT3179\\DataVis\\FIT3179\\DV2\\data\\Arrivals-international_students.csv', index=False)

# # Melt the DataFrame to convert it to long format
# df_long = pd.melt(df, id_vars=['Visa_Category'], var_name='Time_Period', value_name='Percentage')

# # Sort the DataFrame by 'Student_visa' for clarity
# df_long = df_long.sort_values(by='Visa_Category')

# df_long.to_csv('D:\\MONASH\\Y4\\FIT3179\\DataVis\\FIT3179\\DV2\\data\\Arrivals-international_students.csv', index=False)

# # Print the result
# print(df_long)


# import pandas as pd

# # Read the first CSV file
# df = pd.read_csv('D:\\MONASH\\Y4\\FIT3179\\DataVis\\FIT3179\\DV2\\data\\International - Copy.csv')

# # # Read the second CSV file
# # df2 = pd.read_csv('D:\\MONASH\\Y4\\FIT3179\\DataVis\\FIT3179\\DV2\\data\\uniqueInternationalCity.csv')

# # # Group and sum the 'All_Flights' column in the first DataFrame based on 'Year', 'Australian_City', and 'International_City'
# # flight_counts = df1.groupby(['Year', 'Australian_City', 'International_City'])['All_Flights'].sum().reset_index()

# # # Merge the second DataFrame with the flight_counts DataFrame based on 'Year', 'Australian_City', and 'International_City'
# # merged_df = pd.merge(df2, flight_counts, on=['Year', 'Australian_City', 'International_City'], how='left')

# # # Fill NaN values in the 'All_Flights' column with 0 (if there were no flights for a specific combination)
# # merged_df['All_Flights'] = merged_df['All_Flights'].fillna(0)

# # print(merged_df)

# # # Write the merged DataFrame with the new 'Flight_Count' column to a new CSV file
# # merged_df.to_csv('D:\\MONASH\\Y4\\FIT3179\\DataVis\\FIT3179\\DV2\\data\\uniqueInternationalCity2.csv', index=False)


# # Group the data by 'Year' and 'Service_Region', and calculate the sum of 'All_Flights'
# result = df.groupby(['Year', 'Service_Region'])['All_Flights'].sum().reset_index()

# result.to_csv('D:\\MONASH\\Y4\\FIT3179\\DataVis\\FIT3179\\DV2\\data\\ServiceRegionFlights.csv', index=False)

# # Print the result
# print(result)


# import pandas as pd

# # Step 2: Read the CSV file into a pandas DataFrame
# df = pd.read_csv('D:\\MONASH\\Y4\\FIT3179\\DataVis\\FIT3179\\DV2\\data\\International - Copy.csv')

# # Step 3: Group the data by Year and In_Out and count the flights
# flight_counts = df.groupby(['Year', 'In_Out'])['All_Flights'].count().reset_index()

# # Step 4: Pivot the data to have separate columns for inbound and outbound flights
# flight_counts_pivot = flight_counts.pivot(index='Year', columns='In_Out', values='All_Flights')

# # Step 5: Fill missing values with 0
# flight_counts_pivot = flight_counts_pivot.fillna(0)

# # Step 6: Reset the index to have 'Year' as a regular column
# flight_counts_pivot = flight_counts_pivot.reset_index()

# # Step 7: Rename 'I' to 'Inbound' and 'O' to 'Outbound'
# flight_counts_pivot = flight_counts_pivot.rename(columns={'I': 'Inbound', 'O': 'Outbound'})

# # Step 8: Convert the data to a long format using melt
# flight_counts_long = pd.melt(flight_counts_pivot, id_vars=['Year'], value_vars=['Inbound', 'Outbound'], var_name='Flight_Type', value_name='Total_Flights')


# # Step 8: Save the result to a new CSV file
# flight_counts_long.to_csv('D:\\MONASH\\Y4\\FIT3179\\DataVis\\FIT3179\\DV2\\data\\InboundOutboundYear.csv', index=False)


# import pandas as pd

# # Replace 'your_file.csv' with the path to your CSV file
# input_file = 'D:\\MONASH\\Y4\\FIT3179\\DataVis\\FIT3179\\DV2\\data\\Short-term-visitor-arrivals-state-of-stay.csv'

# # Read the CSV file into a Pandas DataFrame
# df = pd.read_csv(input_file)

# # Melt the DataFrame to convert it to long format
# df_long = pd.melt(df, id_vars=['State'], var_name='MonthYear', value_name='Value')

# # Remove commas from the "Value" column
# df_long['Value'] = df_long['Value'].str.replace(',', '', regex=True)

# # Remove the "(no.)" suffix and replace it with a hyphen in the "MonthYear" column
# df_long['MonthYear'] = df_long['MonthYear'].str.replace(r'\s+\(no.\)', '', regex=True)


# # Save the long-format DataFrame to a new CSV file
# output_file = 'D:\\MONASH\\Y4\\FIT3179\\DataVis\\FIT3179\\DV2\\data\\Short-term-visitor-arrivals-state-of-stay-LONG.csv'
# df_long.to_csv(output_file, index=False)

# print(f"CSV file '{input_file}' has been converted to long format and saved as '{output_file}'.")


# # Load the CSV file
# df = pd.read_csv('D:\\MONASH\\Y4\\FIT3179\\DataVis\\FIT3179\\DV2\\data\\TotalArrivalsDepartures.csv')

# # Convert the 'MonthYear' column to a string format
# df['MonthYear'] = pd.to_datetime(df['MonthYear'], format='%b-%y').dt.strftime('%Y-%m')

# # Reshape the DataFrame from wide to long format
# df_long = pd.melt(df, id_vars=['MonthYear'], var_name='Type', value_name='Value')

# # Print or save the resulting DataFrame as needed
# print(df_long)

# # To save the long format DataFrame to a new CSV file
# df_long.to_csv('D:\\MONASH\\Y4\\FIT3179\\DataVis\\FIT3179\\DV2\\data\\TotalArrivalsDepartures-LONG.csv', index=False)


# import pandas as pd

# # Read the CSV file into a DataFrame
# df = pd.read_csv('D:\\MONASH\\Y4\\FIT3179\\DataVis\\FIT3179\\DV2\\data\\AustraliaArrivalTop10Country.csv')

# # Melt the DataFrame to convert it to long form
# df_long = pd.melt(df, id_vars=['Country of residence'], var_name='Period', value_name='Value')

# # Remove commas from the 'Value' column and convert it to numeric
# df_long['Value'] = df_long['Value'].str.replace(',', '').astype(float)

# # Print the resulting DataFrame
# print(df_long)

# df_long.to_csv("D:\\MONASH\\Y4\\FIT3179\\DataVis\\FIT3179\\DV2\\data\\AustraliaArrivalTop10Country-LONG.csv", index=False)


# import pandas as pd

# # Read the CSV file into a DataFrame
# df = pd.read_csv('D:\\MONASH\\Y4\\FIT3179\\DataVis\\FIT3179\\DV2\\data\\AustraliaArrivalMonth.csv')

# # Melt the DataFrame to convert it to long form
# df_long = pd.melt(df, id_vars=['Month'], var_name='Period', value_name='Value')


# # Print the resulting DataFrame
# print(df_long)

# df_long.to_csv("D:\\MONASH\\Y4\\FIT3179\\DataVis\\FIT3179\\DV2\\data\\AustraliaArrivalMonth-LONG.csv", index=False)

import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv('D:\\MONASH\\Y4\\FIT3179\\DataVis\\FIT3179\\DV2\\data\\AustraliaTravellerReason.csv')

# Melt the DataFrame to convert it to long form
df_long = pd.melt(df, id_vars=['MonthYear'], var_name='Reason', value_name='Value')


# Print the resulting DataFrame
print(df_long)

df_long.to_csv("D:\\MONASH\\Y4\\FIT3179\\DataVis\\FIT3179\\DV2\\data\\AustraliaTravellerReason-LONG.csv", index=False)
