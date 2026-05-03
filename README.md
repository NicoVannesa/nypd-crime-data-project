# The nypd-crime-data-project

## Data Source Description

Dataset name: NYPD Complaint Data Historic
Dataset source: https://data.cityofnewyork.us/browse
Link to the data: NYPD Complaint Data Historic | NYC Open Data
GitHub Link: https://github.com/NicoVannesa/nypd-crime-data-project

The following project is based on the NYPD Complaint Data Historic dataset from NYC Open Data.
The main target of this project is to analyze crime complaint data and understand different patterns based on location, type of crime, time and many other factors.

The projects include business requirements, functional requirements, and data requirements. It also has systems designed diagrams which include the information architecture diagram, the data architecture diagram, and a dimensional model using a star schema.

The dimensional model contains a fact table and multiple dimension tables that allow for more efficient data organization and analysis.

## Data Source

https://data.cityofnewyork.us/Public-Safety/NYPD-Complaint-Data-Historic/qgea-i56i/about_data

## Files Included
- Data Dictionary (Excel form, make sure to download the raw form of it to access it.)
- Information Architecture Diagram
- Data Architecture Diagram
- Dimensional Model Diagram

## Explanation of the research:

This dataset was selected to be studied because it has valid felony and violation crimes reported directly to the NYC Police Department (NYPD) from the year of 2006 to the year of 2016. In the entire dataset, it was clear that each complaint record actually stands for one crime complaint and it also includes details such as the type of offense, when and at what time it occurred, where it happened, and many other relevant pieces of information regarding the crime/case.

## Business Requirements

Establishing the high-crime zones in NYC would be important to facilitate public safety and resource deployment.
Determine the most common/frequent types of crimes so that law enforcement agencies can adopt a crime prevention strategy accordingly.
Trends associated with criminal activities should be studied to make decisions and policies.

## Functional Requirements

The system should allow users to filter the crime data by borough, data and type of crime/offense.
The system should display the numbers (#) of crime complaints for different categories.
The system should show crime trends over time using charts and/or tables.
The system should allow users to search for specific crimes and/or locations.
The system should show how often certain crimes occur in different areas.

## Data Requirements

Data Source: NYPD Complaint Data Historic | NYC Open Data

The data that I have decided to use to complete this project is from the NYC Open Data website and it’s called the NYPD Complaint Data Historic. This data contains information on records of crime complaints in New York City. To do this research, I used one of the links that was provided to me which was the NYC Open Data website and in the NYPD Complaint Data was 3 files: 2 xlsx and 1 pdf. The data was downloaded in Excel format and any other informations that was given from the link was in PDF form.
I think that this dataset meets the necessary requirements for this project because it actually contains millions of rows (we are looking at 9.49 M) and it has 35 columns which is way more than this project’s requirements. I believe that the dataset that I chose is not aggregated because each row represents only a single crime complaint, and the dataset doesn’t come from restricted sources like Bitcoin or the stock market. 

This chosen dataset includes information about different types of crimes, the date and time that they occurred, and the location of where they happened. We can also see that there are detailed informations such as borough, offense type, and other related attributes. Unfortunately, there might be some missing values or approximate locations due to limitations and privacy protections reasons.

To better understand this dataset, a data dictionary is created and it defines the columns, including their names, descriptions and what data type they are. In the data dictionary are included different types of data such as text, numeric values, and date/time fields.

## Information Architecture

<img width="1092" height="431" alt="information_architecture_diagram drawio" src="https://github.com/user-attachments/assets/37090044-dafe-4f65-afcf-7ef90e6cd745" />

In the Information Architecture diagram above, we can see how the user starts to interact with the system and how the data moves around between different parts of the system. Everything begins when the user uses the dashboard to either search or filter the data, based on some given factors like the type of crime, the location, or the date of the crime. Once the request is being made, it’s sent to the data processing system.

Then the data processing system handles the request that was made by filtering and preparing the data. After that, it connects to the database, where the NYPD complaint data is being stored and retrieves the information that is needed. After the data is retrieved, it’s being processed so it can be used for visualization.

The processed data is then being sent to the visualization and to the reporting section. The data is usually being displayed as charts or tables. Ultimately, the results are shown back to the user, allowing them to view and analyze all the requested information.

This system includes different user roles with defined permissions. The end users have the opportunity to view, filter, and analyze data through the dashboards, while the administrators are responsible for managing the data updates and maintaining the system’s integrity.

Usually, the data access is read-only for the users, ensuring that the data consistency and preventing any unauthorized modifications. Any updates to the data, occur through backend processing workflows.

The system boundaries also include the user interface, the data processing system and the data storage layer, which all work together to process and deliver all the information efficiently.

# Data Dictionary

<img width="1920" height="936" alt="nypd_data_dictionary - Excel 5_3_2026 6_42_43 PM" src="https://github.com/user-attachments/assets/fed715dc-073c-45dc-964b-71417f725c8c" />

The purpose of developing this data dictionary is to give an understanding of the data structures that exist within the chosen dataset in this study. This is achieved by providing all the essential details such as the name of the column, its description, data types, and any constraints associated with it. This will help understand what each field represents and how data can be used for analysis. 
All the information that I used to build the data dictionary was based on the PDF document that was provided to me by the NYC Open Data and my own understanding of what the data is about.

# Data Architecture

<img width="1263" height="569" alt="data_architecture_diagram drawio png - draw io - Google Chrome 5_3_2026 6_37_32 PM" src="https://github.com/user-attachments/assets/6a8a93c8-0026-416b-886e-7b3573516f71" />

For this project, the data architecture follows a structured pipeline to make certain of the data’s processing and analysis. Everything begins with the data source which is the NYC Open Data platform in this case, which contains the NYPD Complaint dataset.

The data is loaded into a temporary storage where in there the raw data is stored before it’s being processed. That will allow for any data validation and cleaning without modifying the original dataset.

After that, there is the ETL process (Extract, Transform, Load), which is to clean, filter, and transform the data into a structured format. Then the processed data is being stored in a data warehouse, which serves as the central optimized repository for querying and analysis. At the end, the data is being accessed by visualization and reporting tools for the dashboards and insights.

## Dimensional Modeling

<img width="602" height="644" alt="dimensional_model drawio" src="https://github.com/user-attachments/assets/82adbd02-1cbc-4bb1-a581-13ec2021c472" />

This dimensional model was designed using the star schema structure method, which consists of one central fact table and several dimension tables. The fact table (the center one) represents what is the main data in the system, which in this particular case is the crime complaints. For every record in the fact table, its being corresponding to a single complaint and it’s connected to multiple dimensions with foreign keys. 

As for the rest of the tables, meaning the dimension tables, they provide additional details about each complaint, including date, location, crime type, premises and suspect information. The tables are very helpful in organizing the data into meaningful categories, making it easier to analyze.

Next, we have the relationships between the fact table and the dimension tables. The fact table and the dimension tables follow a one-to-many relationship. Each record in a dimension table can be associated with multiple records in the fact table. A good example would be, let’s say, one date, one crime type, one culprit can correspond to many crime complaints.

The star structure improves the data organization and allows for more efficient analysis, because it helps separate descriptive attributes from the main transactional data.

(CONTINUATION COMING SOON!)
