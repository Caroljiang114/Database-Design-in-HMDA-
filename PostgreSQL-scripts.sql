CREATE TABLE Applicant (
    App_ID varchar(80) PRIMARY KEY,
    App_Name varchar(80) not null ,
    Ethnicity varchar(80) CHECK (Ethnicity IN ('Hispanic or Latino','Not Hispanic or Latino','Other')),
    Race varchar(80) CHECK (Race IN ('White','Black or African American','Asian','American Indian')),
    Sex varchar(80) CHECK(Sex IN ('Male','Female', 'Other')),
    App_Income integer not null
);
CREATE TABLE Property (
    P_ID varchar(80) PRIMARY KEY,
    P_type varchar(80) not null ,
    P_Street_No varchar(80)  not null,
    P_Street_Name varchar(80) not null ,
    P_City varchar(80) not null ,
    P_State varchar(80) not null ,
    P_Zip_Code varchar(5) not null ,
    No_Of_Bedrooms integer not null ,
    P_Area numeric(80) not null ,
    Year_Built varchar(80) not null ,
    P_Value numeric(80) not null CHECK (P_Value > 0)
);
CREATE TABLE Institution (
 I_ID  varchar(80)  PRIMARY KEY,
I_Name  varchar(80)  not null,
I_Street_No varchar(80)  not null,
I_Street_name  varchar(80)  not null,
I_City varchar(80)  not null,
I_State varchar(2)  not null,
I_Zip_Code varchar(5)  not null
);
CREATE TABLE Agency (
  Agency_Code varchar(80)  PRIMARY KEY,
  A_Name  varchar(80)  not null,
Name_Acronym  varchar(80)  not null
);
CREATE TABLE loan (
	L_ID varchar(80) PRIMARY KEY,
	L_Type varchar(80) not null CHECK (L_Type IN ('FHA-insured', 'Conventional', 'VA-guranteed')),
	L_Amount integer not null CHECK (L_Amount > 0),
	L_Interest real not null CHECK (L_Interest > 0),
	L_Purpose varchar(80) not null CHECK (L_Purpose IN ('Refinancing','Home purchase', 'Home improvement')),
	L_Status varchar(80) not null CHECK (L_Status IN ('approved', 'denied', 'withdrawn', 'originated')),
	L_Denial_Reason varchar(80) not null CHECK (L_Denial_Reason IN ('Debt-to-income ratio', 'Credit history', 'Collateral', 'Credit application incomplete', 'Employment history','other', '')),
	L_Start_Date date not null,
L_End_Date date not null,
	Agency_Code varchar(80) not null REFERENCES Agency(Agency_Code),
	I_ID varchar(80) not null REFERENCES Institution(I_ID),
	P_ID varchar(80) not null REFERENCES property(P_ID)
);
CREATE TABLE apply (
    App_ID varchar(80) not null REFERENCES applicant(App_ID),
    L_ID varchar(80) not null REFERENCES loan(L_ID)
);

insert into Applicant (App_ID, App_Name, Ethnicity, Race,Sex, App_Income)values
('A100','Mary','Hispanic or Latino','White','Female',84400),
('A102','EMMA','Not Hispanic or Latino','Black or African American','Female',121000),
('A103','ELIZABETH','Hispanic or Latino','Asian','Female',59600),
('A104','MMINNIE','Not Hispanic or Latino','White','Female',146000),
('A105','John','Hispanic or Latino','American Indian','Male',85000),
('A106','William','Not Hispanic or Latino','Black or African American','Male',98000),
('A107','James','Other','Asian','Male',69500),
('A108','Henry','Hispanic or Latino','American Indian','Male',134000),
('A109','ELIA','Other','American Indian','Other',60400),
('A110','Mary','Hispanic or Latino','Asian','Other',77500),
('A111','Robert','Hispanic or Latino','American Indian','Male',70000),
('A112','CLARA','Hispanic or Latino','White','Female',55000);

 INSERT INTO property (P_ID, P_type,P_Street_No, P_Street_Name, P_City, P_State, P_Zip_Code, No_Of_Bedrooms, Year_Built, P_Area, P_Value)
VALUES
('P1', 'Apartment', '1131','Maple Street', 'Los Angeles', 'CA', '90001', 2, '2000', 1200, 300000),
('P2', 'House', '31', 'Oak Avenue', 'New York', 'NY', '10001', 3, '1985', 1800, 450000),
('P3', 'Condo', '373', 'Pine Lane', 'Dallas', 'TX', '75201', 1, '2008', 900, 200000),
('P4', 'Townhouse', '89', 'Cedar Road', 'Miami', 'FL', '33101', 2, '1990', 1500, 250000),
('P5', 'Apartment',  '11-1','Elm Street', 'Chicago', 'IL', '60601', 1, '2015', 800, 180000),
('P6', 'House', '995', 'Birch Boulevard', 'Cleveland', 'OH', '44101', 4, '1970', 2200, 500000),
('P7', 'Condo',  '23','Aspen Court', 'Denver', 'CO', '80201', 2, '2010', 1000, 230000),
('P8', 'Townhouse',  '987','Spruce Drive', 'Atlanta', 'GA', '30301', 3, '1988', 1600, 280000),
('P9', 'Apartment', '123-6', 'Sycamore Lane', 'Charlotte', 'NC', '28201', 1, '2020', 950, 210000),
('P10', 'House',  '765','Cypress Circle', 'Detroit', 'MI', '48201', 3, '2005', 2000, 480000),
('P11', 'Condo',  '298','Redwood Road', 'Seattle', 'WA', '98101', 2, '2012', 1100, 260000),
('P12', 'Townhouse',  '79','Fir Avenue', 'Philadelphia', 'PA', '19101', 2, '1995', 1400, 320000),
('P13', 'Apartment',  '19','Cherry Street', 'Boston', 'MA', '02101', 1, '2018', 900, 190000),
('P14', 'House',  '91','Willow Lane', 'Phoenix', 'AZ', '85001', 4,'1980', 2400, 550000),
('P15', 'Condo',  '786','Juniper Court', 'Chicago', 'IL', '60602', 2,'2007', 1200, 270000),
('P16', 'Townhouse', '45', 'Magnolia Avenue', 'Dallas', 'TX', '75202', 3, '2000', 1700, 310000),
('P17', 'Apartment',  '2871','Chestnut Lane', 'Los Angeles', 'CA', '90002', 1, '2019', 1000, 220000),
('P18', 'House',  '3','Palm Road', 'New York', 'NY', '10002', 5, '1975', 2600, 600000),
('P19', 'Condo',  '81','Poplar Drive', 'Miami', 'FL', '33102', 2, '2011', 1300, 290000),
('P20', 'Townhouse',  '651','Olive Street', 'Dallas', 'TX', '75203', 3, '1998', 1800, 340000);
	 	
INSERT INTO Agency
VALUES
('A1','Office of the Comptroller of the Currency','OCC'),
('A2','Federal Reserve System','FRS'),
('A3','Federal Deposit Insurance Corporation','FDIC'),
('A4','National Credit Union Administration','NCUA'),
('A5','Department of Housing and Urban Development','HUD'),
('A6','Consumer Financial Protection Bureau','CFPB');
INSERT INTO Institution
VALUES
('I1','JPMorgan Chase Bank','1111','Polaris Parkway','Columbus','OH','43240'),
('I2','US BANK','425','WALNUT STREET','CINCINNATI','OH','45202'),
('I3','BANK OF AMERICA','31303','Agoura Rd','Westlake Village','CA','91361'),
('I4','WELLS FARGO BANK','100','N MAIN STREET MAC','WINSTON-SALEM','NC','27150'),
('I5','CITIBANK','1','Court Square','Long Island City','NY','11120'),
('I6','Goldman Sachs Bank','200','West Street','New York','NY','10282'),
('I7','PNC BANK','249','Fifth Ave','Pittsburgh','PA','15222'),
('I8','Fifth Third Bank','38','Fountain Square','Cincinnati','OH','45263'),
('I9','CAPITAL ONE','7933','Preston Road','Plano','TX','75024'),
('I10','TD BANK','2035',' LIMESTONE ROAD','WILMINGTON','DE','19808');

INSERT INTO loan VALUES
('L1', 'Conventional', 10000, 5.0, 'Refinancing', 'denied', 'Credit application incomplete', '2017-06-01', '2018-12-01', 'A1', 'I1', 'P1'),
('L2', 'FHA-insured', 300000, 1.0, 'Home purchase', 'denied', 'Credit application incomplete', '2017-01-01', '2018-12-01', 'A5', 'I2', 'P2'),
('L3', 'VA-guranteed', 58000, 6.0, 'Refinancing', 'approved', 'Employment history', '2017-03-01', '2018-12-01', 'A5', 'I2', 'P2'),
('L4', 'FHA-insured', 69000, 8.0, 'Home purchase', 'denied', 'Employment history', '2017-07-01', '2023-12-01', 'A2', 'I2', 'P3'),
('L5', 'VA-guranteed', 300000, 6.0, 'Home purchase', 'approved', 'Employment history', '2015-05-01', '2016-12-01', 'A3', 'I3', 'P4'),
('L6', 'Conventional', 400000, 8.0, 'Refinancing', 'approved', 'Credit application incomplete', '2017-06-01', '2018-12-01', 'A1', 'I1', 'P5'),
('L7', 'VA-guranteed', 10000, 5.0, 'Refinancing', 'approved', 'Credit application incomplete', '2014-06-01', '2015-12-01', 'A4', 'I1', 'P1'),
('L8', 'FHA-insured', 300000, 1.0, 'Home purchase', 'approved', 'Credit application incomplete', '2023-01-01', '2023-12-01', 'A2', 'I2', 'P2'),
('L9', 'VA-guranteed', 57000, 6.0, 'Refinancing', 'denied', 'other', '2020-03-01', '2021-12-01', 'A3', 'I2', 'P2'),
('L10', 'FHA-insured', 65000, 8.0, 'Home purchase', 'denied', 'Employment history', '2017-07-01', '2018-12-01', 'A5', 'I2', 'P3'),
('L11', 'FHA-insured', 300000, 6.0, 'Home purchase', 'approved', 'other', '2023-05-01', '2023-12-01', 'A6', 'I3', 'P4'),
('L12', 'Conventional', 400000, 8.0, 'Refinancing', 'approved', 'Credit application incomplete', '2017-06-01', '2018-12-01', 'A1', 'I1', 'P10'),
('L13', 'FHA-insured', 80000, 8.0, 'Home purchase', 'denied', 'Employment history', '2017-07-01', '2018-12-01', 'A5', 'I2', 'P3'),
('L14', 'FHA-insured', 60000, 8.0, 'Home purchase', 'approved', 'Employment history', '2017-07-01', '2018-12-01', 'A5', 'I2', 'P3'),
('L15', 'FHA-insured', 49000, 8.0, 'Home purchase', 'denied', 'Employment history', '2017-07-01', '2018-12-01', 'A5', 'I2', 'P3')
;

INSERT INTO apply VALUES 
('A100', 'L1'),
('A102', 'L2'),
('A102', 'L3'),
('A102', 'L4'),
('A103', 'L5'),
('A103', 'L6'),
('A104', 'L7'),
('A105', 'L8'),
('A106', 'L9'),
('A107', 'L10'),
('A108', 'L11'),
('A109', 'L12');


SELECT 
    I.I_Name AS Institution_Name,
    A.A_Name AS Agency_Name,DATE_PART('YEAR', L.L_Start_Date) AS Year,
TO_CHAR(L.L_Start_Date, 'Month') AS Month,COUNT(*) AS Total_Applications,
    SUM(CASE WHEN L.L_Status = 'denied' THEN 1 ELSE 0 END) AS Denial_Count,
    ROUND(SUM(CASE WHEN L.L_Status = 'denied' THEN 1 ELSE 0 END) * 100.0 / NULLIF(COUNT(*), 0), 2) AS Denial_Percentage,
    L.L_Denial_Reason AS Denial_Reason
FROM 
    loan L, Institution I, Agency A
WHERE 
    L.I_ID = I.I_ID 
    AND L.Agency_Code = A.Agency_Code 
    AND DATE_PART('YEAR', L.L_Start_Date) = 2017
GROUP BY 
    I.I_Name, A.A_Name, DATE_PART('YEAR', L.L_Start_Date), TO_CHAR(L.L_Start_Date, 'Month'),L.L_Denial_Reason
ORDER BY 
    Year,Month, Institution_Name, Agency_Name;

WITH App AS (SELECT App.App_ID, App.App_Income, avg(App.App_Income) OVER () as average FROM applicant App)
SELECT App.App_ID, App.App_Income, COUNT(*) as number_of_loans, AVG(L.L_Interest) as average_interest_rate, AVG(L.L_Amount) as average_loan_amount, App.average as average_income
FROM App, apply A, loan L
WHERE App.App_Income <= App.average and App.App_ID = A.App_ID and A.L_ID = L.L_ID
GROUP BY App.App_ID, App.App_Income, App.average
ORDER BY App.App_Income DESC;

SELECT
	Sex,
	Race,
	AVG(App_Income) AS AvgIncome,
	AVG(AvgLoans) AS AvgLoans
FROM (
	SELECT
    	Applicant.Sex,
    	Applicant.Race,
    	Applicant.App_Income,
    	COUNT(Loan.L_ID) AS AvgLoans
	FROM
    	Applicant, Apply, Loan
	WHERE
    	Applicant.App_ID = Apply.App_ID
    	AND Apply.L_ID = Loan.L_ID
	GROUP BY
    	Applicant.Sex, Applicant.Race, Applicant.App_Income
) AS Subquery
GROUP BY
	Sex, Race
ORDER BY
	AvgIncome DESC;


select A.a_name,count(*) as num_of_loans ,avg(P.p_value) as avg_of_properties
from property P, agency A, loan L
where A.agency_code=L.agency_code and
	  L.p_id=P.p_id and
	  P.p_value>=300000
group by A.agency_code, A.A_Name
having count(*)>=1
order by avg(P.p_value)
