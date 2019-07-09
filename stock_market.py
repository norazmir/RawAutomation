import pandas as pd
import json

# read csv file
read_demand = pd.read_csv('C:/Users/norazmir.nordin/Desktop/ActualVSPrediction.csv')
print(read_demand.head())

# read json druid template
with open('C:/Users/norazmir.nordin/Desktop/query_stock_market.json') as access_json:
    read_content = json.load(access_json)

print(read_content)

# header of sdemand columns
demand_list = read_demand.columns.to_list()
print(demand_list)

# inserting sdemand column headers
jDemandCol = read_content['spec']['dataSchema']['parser']['parseSpec']
jDemandCol.update(columns=demand_list)
print(jDemandCol)

dimension_list = demand_list.copy()  # copy list of dimensions

# updating dimensions
for idx, col in enumerate(dimension_list):
    if read_demand[col].dtype == 'float64':
        dimension_list[idx] = {'name': col, "type": 'float'}
    elif read_demand[col].dtype == 'int64':
        dimension_list[idx] = {'name': col, "type": 'long'}

# inserting dimensions
jdimSpec = read_content['spec']['dataSchema']['parser']['parseSpec']['dimensionsSpec']
jdimSpec.update(dimensions=dimension_list)
print(jdimSpec)

# - for writing file to json file
s = json.dumps(read_content)

# create new json file
with open("C:/Users/norazmir.nordin/Desktop/query_stock_market", "w") as f:
    f.write(s)
