-- NYPD Crime Complaint Data Warehouse

DROP TABLE IF EXISTS Fact_Crime_Complaints;
DROP TABLE IF EXISTS Dim_Suspect;
DROP TABLE IF EXISTS Dim_Premises;
DROP TABLE IF EXISTS Dim_Crime;
DROP TABLE IF EXISTS Dim_Location;
DROP TABLE IF EXISTS Dim_Date;

CREATE TABLE Dim_Date (
    Date_ID INT IDENTITY(1,1) PRIMARY KEY,
    Complaint_Date DATE,
    Year INT,
    Quarter INT,
    Month INT,
    Day INT
);

CREATE TABLE Dim_Location (
    Location_ID INT IDENTITY(1,1) PRIMARY KEY,
    Borough VARCHAR(100),
    Precinct INT,
    Latitude DECIMAL(10,6),
    Longitude DECIMAL(10,6)
);

CREATE TABLE Dim_Crime (
    Crime_ID INT IDENTITY(1,1) PRIMARY KEY,
    Offense_Description VARCHAR(255),
    Law_Category VARCHAR(50),
    Is_Felony INT
);

CREATE TABLE Dim_Premises (
    Premises_ID INT IDENTITY(1,1) PRIMARY KEY,
    Premises_Description VARCHAR(255)
);

CREATE TABLE Dim_Suspect (
    Suspect_ID INT IDENTITY(1,1) PRIMARY KEY,
    Suspect_Age_Group VARCHAR(50),
    Suspect_Race VARCHAR(100),
    Suspect_Sex VARCHAR(20)
);

CREATE TABLE Fact_Crime_Complaints (
    Fact_ID INT IDENTITY(1,1) PRIMARY KEY,
    Complaint_Number VARCHAR(50),
    Date_ID INT,
    Location_ID INT,
    Crime_ID INT,
    Premises_ID INT,
    Suspect_ID INT,
    Complaint_Time VARCHAR(20),

    FOREIGN KEY (Date_ID) REFERENCES Dim_Date(Date_ID),
    FOREIGN KEY (Location_ID) REFERENCES Dim_Location(Location_ID),
    FOREIGN KEY (Crime_ID) REFERENCES Dim_Crime(Crime_ID),
    FOREIGN KEY (Premises_ID) REFERENCES Dim_Premises(Premises_ID),
    FOREIGN KEY (Suspect_ID) REFERENCES Dim_Suspect(Suspect_ID)
);
