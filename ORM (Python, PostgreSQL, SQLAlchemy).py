import datetime
from typing import List
from typing import Optional
from sqlalchemy import Column, ForeignKey, Table
from sqlalchemy import String, Integer, Float, Date
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy import select
from sqlalchemy.sql import func
from sqlalchemy.sql.expression import cast
from sqlalchemy import case, literal
from prettytable import PrettyTable




#DB Connection: create_engine(DBMS_name+driver://<username>:<password>@<hostname>/<database_name>)
engine = create_engine("postgresql+psycopg2://adam:1809@localhost/postgres")


#Define Classes/Tables
class Base(DeclarativeBase):
   pass


association_table = Table(
   "association_table",
   Base.metadata,
   Column("loan", ForeignKey("loan.L_ID"), primary_key=True),
   Column("applicant", ForeignKey("applicant.App_ID"), primary_key=True)
)


class Applicant(Base):
   __tablename__ = "applicant"


   def __init__(self, id, name, ethnicity, race, sex, income):
       self.App_ID = id
       self.App_Name = name
       self.Ethnicity = ethnicity
       self.Race = race
       self.Sex = sex
       self.App_Income = income


   App_ID: Mapped[str] = mapped_column(String, primary_key=True)
   App_Name: Mapped[str] = mapped_column(String, nullable=False)
   Ethnicity: Mapped[str] = mapped_column(String, nullable=False)
   Race: Mapped[str] = mapped_column(String, nullable=False)
   Sex: Mapped[str] = mapped_column(String, nullable=False)
   App_Income: Mapped[str] = mapped_column(Integer, nullable=False)
   loans: Mapped[List["Loan"]] = relationship(
       back_populates="applicants", secondary=association_table
   )


   def __repr__(self) -> str:
       return f"Applicant(id={self.App_ID!r}, name={self.App_Name!r}, ethnicity={self.Ethnicity!r}, race={self.Race!r}, sex={self.Sex!r}, income={self.App_Income!r})"


class Institution(Base):
  __tablename__ = "institution"




  I_ID: Mapped[str] = mapped_column(String, primary_key=True)
  I_Name: Mapped[str] = mapped_column(String(30))
  I_Street_No: Mapped[str] = mapped_column(String(40))
  I_Street_name: Mapped[str] = mapped_column(String(40))
  I_City: Mapped[str] = mapped_column(String(40))
  I_State: Mapped[str] = mapped_column(String(2))
  I_Zip_Code: Mapped[str] = mapped_column(String(5))
  loans: Mapped[List["Loan"]] = relationship(
      back_populates="institution", cascade="all, delete-orphan"
  )


  def __repr__(self) -> str:  # represents the object as a string
      return f"Institution(I_ID={self.I_ID!r}, I_Name={self.I_Name!r}, I_Street_No={self.I_Street_No!r},I_Street_name={self.I_Street_name!r},I_City={self.I_City!r},I_State={self.I_State!r},I_Zip_Code={self.I_Zip_Code!r})"


class Property(Base):
   __tablename__ = "property"
  
   P_ID: Mapped[str] = mapped_column(String(50), primary_key=True)
   P_Type: Mapped[str] = mapped_column(String(50),nullable=False)
   P_Street_No: Mapped[str] = mapped_column(String(50),nullable=False)
   P_Street_Name: Mapped[str] = mapped_column(String(50),nullable=False)
   P_City: Mapped[str] = mapped_column(String(50),nullable=False)
   P_State: Mapped[str] = mapped_column(String(50),nullable=False)
   P_Zip_Code: Mapped[str] = mapped_column(String(50),nullable=False)
   No_Of_Bedrooms: Mapped[int] = mapped_column(Integer,nullable=False)
   Year_Built: Mapped[str] = mapped_column(String(50),nullable=False)
   P_Area: Mapped[str] = mapped_column(String(50),nullable=False)
   P_Value: Mapped[int] = mapped_column(Integer,nullable=False)
   loans: Mapped[List["Loan"]] = relationship(
       back_populates="property", cascade="all, delete-orphan"
   )


   def __repr__(self) -> str: #represents the object as a string
       return f"Property(P_ID={self.P_ID!r}, P_Type={self.P_Type!r}, P_Street_No={self.P_Street_No!r},P_Street_Name={self.P_Street_Name!r},P_City={self.P_City!r},P_State={self.P_State},P_Zip_Code={self.P_Zip_Code!r},No_Of_Bedrooms={self.No_Of_Bedrooms!r},Year_Built={self.Year_Built!r},P_Area={self.P_Area!r},P_Value={self.P_Value!r})"


class Agency(Base):
   __tablename__ = "agency"


   Agency_Code: Mapped[str] = mapped_column(String, primary_key=True)
   A_Name: Mapped[str] = mapped_column(String, nullable=False)
   Name_Acronym: Mapped[str] = mapped_column(String, nullable=False)


   loans: Mapped[List["Loan"]] = relationship(back_populates="agency")


   def __repr__(self) -> str:
       return f"Agency(Agency_Code={self.Agency_Code!r}, A_Name={self.A_Name!r}, Name_Acronym={self.Name_Acronym!r})"


class Loan(Base):
   __tablename__ = "loan"


   def __init__(self, id, type, amount, interest, purpose, status, denial, start, end):
       self.L_ID = id
       self.L_Type = type
       self.L_Purpose = purpose
       self.L_Amount = amount
       self.L_Interest = interest
       self.L_Status = status
       self.L_Denial_Reason = denial
       self.L_Start_Date = start
       self.L_End_Date = end


   L_ID: Mapped[str] = mapped_column(String, primary_key=True)
   L_Type: Mapped[str] = mapped_column(String, nullable=False)
   L_Purpose: Mapped[str] = mapped_column(String, nullable=False)
   L_Amount: Mapped[int] = mapped_column(Integer, nullable=False)
   L_Interest: Mapped[float] = mapped_column(Float, nullable=False)
   L_Status: Mapped[str] = mapped_column(String, nullable=False)
   L_Denial_Reason: Mapped[str] = mapped_column(String, nullable=False)
   L_Start_Date: Mapped[datetime.date] = mapped_column(Date, nullable=False)
   L_End_Date: Mapped[datetime.date] = mapped_column(Date, nullable=False)


   Agency_Code: Mapped[str] = mapped_column(String, ForeignKey("agency.Agency_Code"), nullable=True)
   agency: Mapped["Agency"] = relationship(back_populates="loans")


   I_ID: Mapped[str] = mapped_column(String, ForeignKey("institution.I_ID"), nullable=True)
   institution: Mapped["Institution"] = relationship(back_populates="loans")


   P_ID: Mapped[str] = mapped_column(String, ForeignKey("property.P_ID"), nullable=True)
   property: Mapped["Property"] = relationship(back_populates="loans")


   applicants: Mapped[List["Applicant"]] = relationship(back_populates="loans", secondary=association_table)


   def __repr__(self) -> str:
       return f"Loan(id={self.L_ID!r}, type={self.L_Type!r}, purpose={self.L_Purpose!r}, amount={self.L_Amount!r}, interest={self.L_Interest!r}, status={self.L_Status!r}, denial={self.L_Denial_Reason!r}, start={self.L_Start_Date!r}, end={self.L_End_Date!r})"


#Create Tables
Base.metadata.create_all(engine)


with Session(engine) as session:


   agency1 = Agency(Agency_Code='A1', A_Name='Office of the Comptroller of the Currency', Name_Acronym='OCC')
   agency2 = Agency(Agency_Code='A2', A_Name='Federal Reserve System', Name_Acronym='FRS')
   agency3 = Agency(Agency_Code='A3', A_Name='Federal Deposit Insurance Corporation', Name_Acronym='FDIC')
   agency4 = Agency(Agency_Code='A4', A_Name='National Credit Union Administration', Name_Acronym='NCUA')
   agency5 = Agency(Agency_Code='A5', A_Name='Department of Housing and Urban Development', Name_Acronym='HUD')
   agency6 = Agency(Agency_Code='A6', A_Name='Consumer Financial Protection Bureau', Name_Acronym='CFPB')
   session.add_all([agency1, agency2, agency3, agency4, agency5, agency6])


   a1 = Applicant('A101','Mary','Hispanic or Latino','White','Female',84400)
   a2 = Applicant('A102','EMMA','Not Hispanic or Latino','Black or African American','Female',60000)
   a3 = Applicant('A103','ELIZABETH','Hispanic or Latino','Asian','Female',59600)
   a4 = Applicant('A104','MINNIE','Not Hispanic or Latino','White','Female',146000)
   a5 = Applicant('A105','John','Hispanic or Latino','American Indian','Male',85000)
   a6 = Applicant('A106','William','Not Hispanic or Latino','Black or African American','Male',98000)
   a7 = Applicant('A107','James','Other','Asian','Male',69500)
   a8 = Applicant('A108','Henry','Hispanic or Latino','American Indian','Male',134000)
   a9 = Applicant('A109','ELIA','Other','American Indian','Other',60400)
   a10 = Applicant('A110','Mary','Hispanic or Latino','Asian','Other',77500)
   a11 = Applicant('A111','Robert','Hispanic or Latino','American Indian','Male',70000)
   a12 = Applicant('A112','CLARA','Hispanic or Latino','White','Female',55000)
   session.add_all([a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12])


   Chase = Institution(
      I_ID="I1",I_Name="JPMorgan Chase Bank",I_Street_No="1111",
      I_Street_name="Polaris Parkway",I_City="Columbus",I_State="OH",I_Zip_Code="43240"
   )
   US_Bank = Institution(
      I_ID="I2",I_Name="US BANK",I_Street_No="425",
      I_Street_name="WALNUT STREET",I_City="CINCINNATI",I_State="OH",I_Zip_Code="45202"
   )
   BANK_OF_AMERICA = Institution(
      I_ID="I3",I_Name="BANK OF AMERICA",I_Street_No="31303",
      I_Street_name="Agoura Rd",I_City="Westlake Village",I_State="CA",I_Zip_Code="91361"
   )
   wells_fargo = Institution(
      I_ID="I4",I_Name="WELLS FARGO BANK",I_Street_No="100",
      I_Street_name="N MAIN STREET MAC",I_City="N MAIN STREET MAC",I_State="NC",I_Zip_Code="27150",
   )
   citi = Institution(
      I_ID="I5",I_Name="CITIBANK",I_Street_No="1",
      I_Street_name="Court Square",I_City="Long Island City",I_State="NY",I_Zip_Code="11120",
   )
   goldman = Institution(
      I_ID="I6",I_Name="Goldman Sachs Bank",I_Street_No="200",
      I_Street_name="West Street",I_City="New York City",I_State="NY",I_Zip_Code="10282",
   )
   PNC = Institution(
      I_ID="I7",I_Name="PNC BANK",I_Street_No="249",
      I_Street_name="Fifth Ave",I_City="Pittsburgh",I_State="PA",I_Zip_Code="15222",
   )
   fifth_third = Institution(
      I_ID="I8",I_Name="Fifth Third Bank",I_Street_No="38",
      I_Street_name="Fountain Square",I_City="CINCINNATI",I_State="OH",I_Zip_Code="45263",
   )
   capital_one = Institution(
      I_ID="I9",I_Name="CAPITAL ONE",I_Street_No="7933",
      I_Street_name="Preston Road",I_City="Plano",I_State="TX",I_Zip_Code="75024",
   )
   TD = Institution(
      I_ID="I10",I_Name="TD BANK",I_Street_No="2035",
      I_Street_name="LIMESTONE ROAD",I_City="WILMINGTON",I_State="DE",I_Zip_Code="19808",
   )
   session.add_all([Chase, US_Bank, BANK_OF_AMERICA,wells_fargo,citi,goldman,PNC,fifth_third,capital_one,TD])


   p1=Property(P_ID='P1',P_Type= 'Apartment', P_Street_No='1131',P_Street_Name='Maple Street',P_City= 'Los Angeles',P_State= 'CA',P_Zip_Code= '90001',No_Of_Bedrooms= 2, Year_Built='2000',P_Area= '1200', P_Value=300000)
   p2=Property(P_ID='P2',P_Type= 'House', P_Street_No='31', P_Street_Name='Oak Avenue', P_City= 'New York', P_State='NY', P_Zip_Code= '10001',No_Of_Bedrooms=3, Year_Built='1985',P_Area=  '1800', P_Value=450000)
   p3=Property(P_ID='P3',P_Type= 'Condo',P_Street_No= '373', P_Street_Name='Pine Lane',P_City=  'Dallas', P_State='TX', P_Zip_Code='75201',No_Of_Bedrooms= 1,Year_Built= '2008', P_Area= '900',P_Value= 200000)
   p4=Property(P_ID='P4',P_Type= 'Townhouse',P_Street_No= '89',P_Street_Name= 'Cedar Road',P_City=  'Miami', P_State='FL',P_Zip_Code= '33101', No_Of_Bedrooms=2,Year_Built= '1990',P_Area=  '1500', P_Value=250000)
   p5=Property(P_ID='P5',P_Type= 'Apartment', P_Street_No= '11-1',P_Street_Name='Elm Street',P_City=  'Chicago',P_State= 'IL',P_Zip_Code= '60601', No_Of_Bedrooms=1,Year_Built= '2015',P_Area=  '800',P_Value= 180000)
   session.add_all([p1,p2,p3,p4,p5])


   l1 = Loan('L1', 'Conventional', 10000, 5.0, 'Refinancing', 'denied', 'Credit application incomplete', '2017-06-01', '2018-12-01')
   l2 = Loan('L2', 'FHA-insured', 300000, 1.0, 'Home purchase', 'denied', 'Credit application incomplete', '2017-01-01', '2018-12-01')
   l3 = Loan('L3', 'VA-guranteed', 58000, 6.0, 'Refinancing', 'approved', 'Employment history', '2017-03-01', '2018-12-01')
   l4 = Loan('L4', 'FHA-insured', 69000, 8.0, 'Home purchase', 'denied', 'Employment history', '2017-07-01', '2023-12-01')
   l5 = Loan('L5', 'VA-guranteed', 300000, 6.0, 'Home purchase', 'approved', 'Employment history', '2015-05-01', '2016-12-01')
   l6 = Loan('L6', 'Conventional', 400000, 8.0, 'Refinancing', 'approved', 'Credit application incomplete', '2017-06-01', '2018-12-01')
   l7 = Loan('L7', 'VA-guranteed', 10000, 5.0, 'Refinancing', 'approved', 'Credit application incomplete', '2014-06-01', '2015-12-01')
   l8 = Loan('L8', 'FHA-insured', 300000, 1.0, 'Home purchase', 'approved', 'Credit application incomplete', '2023-01-01', '2023-12-01')
   l9 = Loan('L9', 'VA-guranteed', 57000, 6.0, 'Refinancing', 'denied', 'other', '2020-03-01', '2021-12-01')
   l10 = Loan('L10', 'FHA-insured', 65000, 8.0, 'Home purchase', 'denied', 'Employment history', '2017-07-01', '2018-12-01')
   l11 = Loan('L11', 'FHA-insured', 300000, 6.0, 'Home purchase', 'approved', 'other', '2023-05-01', '2023-12-01')
   l12 = Loan('L12', 'Conventional', 400000, 8.0, 'Refinancing', 'approved', 'Credit application incomplete', '2017-06-01', '2018-12-01')
   l13 = Loan('L13', 'FHA-insured', 80000, 8.0, 'Home purchase', 'denied', 'Employment history', '2017-07-01', '2018-12-01')
   l14 = Loan('L14', 'FHA-insured', 60000, 8.0, 'Home purchase', 'approved', 'Employment history', '2017-07-01', '2018-12-01')
   l15 = Loan('L15', 'FHA-insured', 49000, 8.0, 'Home purchase', 'denied', 'Employment history', '2017-07-01', '2018-12-01')


   l1.applicants=[a1]
   l2.applicants=[a2]
   l3.applicants=[a2]
   l4.applicants=[a2]
   l5.applicants=[a3]
   l6.applicants=[a3]
   l7.applicants=[a4]
   l8.applicants=[a5]
   l9.applicants=[a6]
   l10.applicants=[a7]
   l11.applicants=[a8]
   l12.applicants=[a9]
   l1.agency = agency1
   l2.agency = agency5
   l3.agency = agency5
   l4.agency = agency2
   l5.agency = agency3
   l6.agency = agency1
   l7.agency = agency4
   l8.agency = agency2
   l9.agency = agency3
   l10.agency = agency5
   l11.agency = agency6
   l12.agency = agency1
   l13.agency = agency5
   l14.agency = agency5
   l15.agency = agency5
   l1.institution = Chase
   l6.institution = Chase
   l7.institution = Chase
   l12.institution = Chase
   l8.institution = US_Bank
   l9.institution = US_Bank
   l10.institution = US_Bank
   l15.institution = US_Bank
   l13.institution = US_Bank
   l2.institution = US_Bank
   l3.institution = US_Bank
   l4.institution = US_Bank
   l14.institution = US_Bank
   l11.institution = BANK_OF_AMERICA
   l5.institution = BANK_OF_AMERICA
   l1.property = p1
   l2.property = p2
   l3.property = p3
   l4.property = p4
   l5.property = p5
   l6.property = p5
   l7.property = p2
   l8.property = p1
   l9.property = p4
   l10.property = p3
   l11.property = p3
   l12.property = p1
   l13.property = p2
   l14.property = p3
   l15.property = p1
  
   session.add_all([l1, l2, l3, l4, l5, l6, l7, l8, l9, l10, l11, l12, l13, l14, l15])
   session.commit()


#Query #1 - Sunayana
#This query will show how many loan applications have been denied by which institution and agency and what was the #percentage and reason of denial for each month of the year ‘2017’.
session = Session(engine) 
query = (
    session.query(
        Institution.I_Name.label('Institution_Name'),
        Agency.A_Name.label('Agency_Name'),
        func.date_part('year', Loan.L_Start_Date).label('Year'),
        func.to_char(Loan.L_Start_Date, 'Month').label('Month'),
        func.count().label('Total_Applications'),
        func.sum(case((Loan.L_Status == 'denied', 1), 
else_=0)).label('Denial_Count'),func.round(
            (func.sum(case((Loan.L_Status == 'denied', 1), else_=0)) * 100.0) /func.nullif(func.count(), 0) ,2)
        .label('Denial_Percentage'),     func.array_agg(Loan.L_Denial_Reason.distinct()).label('Denial_Reasons')
    )
    .join(Institution, Loan.I_ID == Institution.I_ID)
    .join(Agency, Loan.Agency_Code == Agency.Agency_Code)
    .filter(func.date_part('year', Loan.L_Start_Date) == 2017)
    .group_by(
        Institution.I_ID,
        Agency.Agency_Code,
        func.date_part('year', Loan.L_Start_Date),
        func.to_char(Loan.L_Start_Date, 'Month')
    )
    .order_by('Year', 'Month', 'Institution_Name','A_Name')
)
results = query.all()
print("## Output ##")
table = PrettyTable()
table.field_names = ["Institution","Agency", "Year", "Month", "Total 
Applications", "Denial Count", "Denial Percentage", "Denial Reasons"]
for result in results:
    table.add_row([result.Institution_Name,result.Agency_Name, result.Year, result.Month, result.Total_Applications, result.Denial_Count, result.Denial_Percentage, result.Denial_Reasons])
print(table)
  

#Query #2 - Adam
#It finds the average income, total number of loans, average interest rate, and average loan amount per applicant #with an income at or below the average. Order by applicant income descending.        

subquery = (
   select(cast(func.avg(Applicant.App_Income).label("average_income"), Float))
   .cte("sub")
)
query = (
       select(Applicant.App_ID, Applicant.App_Name, Applicant.App_Income, func.count(), cast(func.avg(Loan.L_Amount), Float), func.avg(Loan.L_Interest), subquery.c.average_income)
       .join(Applicant.loans)
       .add_cte(subquery)
       .group_by(Applicant.App_ID, Applicant.App_Name, Applicant.App_Income, subquery.c.average_income)
       .where(Applicant.App_Income < subquery.c.average_income)
       )
result = session.execute(query)
for item in result:
   print(item)

#Query #3 - Fiore
#Query to select FHA-Insured loans that are approved and have applicants with an income greater than 70,000.
result = (
   session.query(Agency.A_Name,
                 Loan.L_ID,
                 Loan.L_Type,
                 Applicant.App_ID,
                 Applicant.App_Name,
                 Applicant.App_Income)
   .join(Loan, Agency.Agency_Code == Loan.Agency_Code)
   .join(association_table, Loan.L_ID == association_table.c.loan)
   .join(Applicant, Applicant.App_ID == association_table.c.applicant)
   .filter(Loan.L_Status == 'approved',
           Loan.L_Type == 'FHA-insured',
           Applicant.App_Income > 70000)
   .all()
)
for row in result:
   print(row)


#QUERY #4 - Chongchong 
#List the count of loans and the average property values supervised by each agency, considering only properties valued over 300,000 and agencies with more than one loan. Sort the results in ascending order based on the average property values.

result = (((((((session.query(Agency.A_Name,
                     func.count().label('num_of_loans'),
                     func.avg(Property.P_Value).label('avg_of_properties'))
        .join(Loan, Agency.Agency_Code == Loan.Agency_Code))
        .join(Property, Loan.P_ID == Property.P_ID))
        .filter(Property.P_Value >= 300000))
        .group_by(Agency.Agency_Code, Agency.A_Name))
        .having(func.count() >= 1))
        .order_by(func.avg(Property.P_Value)))
        .all())


for item in result:
   print(item)










