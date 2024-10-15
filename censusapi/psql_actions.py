import psycopg2

# Database connection parameters
db_params = {
    'dbname': 'census',
    'user': 'wc',
    'password': '2004',
    'host': 'localhost',
    'port': '5432'
}

# Connect to the PostgreSQL database
try:
    connection = psycopg2.connect(**db_params)
    cursor = connection.cursor()
    
    # Execute the SQL command
    cursor.execute(create_state_query)
    
    # Commit the changes
    connection.commit()
    
    print("Table created successfully")
except Exception as error:
    print(f"Error creating table: {error}")
finally:
    # Close the cursor and connection
    if cursor:
        cursor.close()
    if connection:
        connection.close()

#SQL Commands
create_state_query = '''
CREATE TABLE state (
    fips INTEGER UNIQUE
    name TEXT
    abbreviation VARCHAR(2) NOT NULL
    districts INTEGER[]
)
'''

create_district_query = '''
CREATE TABLE district (
    fips INTEGER UNIQUE
    district_num INTEGER UNIQUE
    congress INTEGER
    area FLOAT
    perimeter FLOAT
    current_party CHAR(1)
    d_votes INTEGER
    r_votes INTEGER
)
'''

create_district_geo_query = '''
CREATE TABLE district_geo (
    fips INTEGER UNIQUE
    district_num INTEGER UNIQUE
    congress INTEGER
    geom GEOMETRY(Geometry, 4326)
)
'''

create_district_results_query = '''
CREATE TABLE district_results (
    fips INTEGER UNIQUE
    district_num INTEGER UNIQUE
    congress INTEGER
    polsby-popper FLOAT
    schwartzberg FLOAT
    reock FLOAT
    eg FLOAT
)
'''

get_geojson_query = '''
SELECT * FROM district
    INNER JOIN district_geo ON district.fips = district_geo.fips 
        AND  district.district_num = district_geo.district_num
        AND district.congress = district_geo.congress
'''

compare_district_to_state = '''
SELECT * FROM district_results

'''

insert_state_query = '''
INSERT INTO your_app_state (name, abbreviation) VALUES (%s, %s) RETURNING id;
'''


insert_district_query = '''
INSERT INTO your_app_district (
    state_id, name, district, republican_votes, democratic_votes, area, perimeter, congress, party
) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);
'''