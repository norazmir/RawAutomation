import pandas as pd
import json

# read csv file
read_demand = pd.read_csv(
    'C:/Users/norazmir.nordin/Desktop/out_clean_sdemand_2014_2018.csv')
print(read_demand.head())

# read json druid template
with open('C:/Users/norazmir.nordin/Desktop/Json_template.json') as access_json:
    read_content = json.load(access_json)


# header of sdemand columns
demand_list = read_demand.columns.to_list()
print(demand_list)

# inserting sdemand column headers
jDemandCol = read_content['spec']['dataSchema']['parser']['parseSpec']
jDemandCol.update(columns=demand_list)
print(jDemandCol)


# copy list of dimensions
dimension_list = demand_list.copy()

# updating dimensions
for idx, col in enumerate(dimension_list):
    if read_demand[col].dtype == 'float64':
        dimension_list[idx] = {'name': col, "type": 'float'}
    elif read_demand[col].dtype == 'int64':
        dimension_list[idx] = {'name': col, "type": 'long'}

# inserting dimensions
jdimSpec = read_content['spec']['dataSchema']['parser']['parseSpec']['dimensionsSpec']
print(jdimSpec)
jdimSpec.update(dimensions=dimension_list)
print(jdimSpec)

read_demand['DEMAND_DATE'] = pd.to_datetime(read_demand.DEMAND_DATE, dayfirst=True)
newDate = read_demand['DEMAND_DATE'].dt.strftime('%Y-%m-%d')

read_demand['Time_Date'].update(newDate)
print(read_demand['DEMAND_DATE'].head())

# - for writing file to json file
s = json.dumps(read_content)

# create new json file
with open("C:/Users/norazmir.nordin/Desktop/query_sdemand_2014_2018", "w") as f:
    f.write(s)
