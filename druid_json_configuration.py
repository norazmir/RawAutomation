import pandas as pd
import json

# read csv file
read_demand = pd.read_csv(
    'C:/../[raw file]')
print(read_demand.head())

# read json druid template
with open('C:/../Json_template.json') as access_json:
    read_content = json.load(access_json)


# header of columns values
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

read_demand[column_header] = pd.to_datetime(read_demand.column_header, dayfirst=True)
newDate = read_demand[column_header].dt.strftime('%Y-%m-%d')

read_demand[column_header].update(newDate)
print(read_demand[column_header].head())

# - for writing file to json file
s = json.dumps(read_content)

# create new json file
with open("C:/../[output at raw json file]", "w") as f:
    f.write(s)
