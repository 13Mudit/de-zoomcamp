import time

import pandas as pd
from sqlalchemy import create_engine


engine = create_engine('postgresql://root:root@pgdatabase:5432/ny_taxi')

# data_url = "https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/yellow_tripdata_2021-01.csv.gz"
# table_name = "yellow_taxi_data"
# data_url = "https://d37ci6vzurychx.cloudfront.net/misc/taxi+_zone_lookup.csv"
# table_name = "zones"
data_url = "https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2019-01.csv.gz"
table_name = "green_taxi_data_2019"

df_iter = pd.read_csv(data_url, compression='gzip', iterator=True, chunksize=100000)
# df_iter = pd.read_csv(data_url, iterator=True, chunksize=100000)


df = next(df_iter)

print(pd.io.sql.get_schema(df, name=table_name, con=engine))


# df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
# df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)
df.lpep_pickup_datetime = pd.to_datetime(df.lpep_pickup_datetime)
df.lpep_dropoff_datetime = pd.to_datetime(df.lpep_dropoff_datetime)


df.head(n=0).to_sql(name=table_name, con=engine, if_exists="replace")

df.to_sql(name=table_name, con=engine, if_exists="append")

while True:
	try:
		t_start = time.time()

		df = next(df_iter)
		
		# df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
		# df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)
		df.lpep_pickup_datetime = pd.to_datetime(df.lpep_pickup_datetime)
		df.lpep_dropoff_datetime = pd.to_datetime(df.lpep_dropoff_datetime)

		df.to_sql(name=table_name, con=engine, if_exists="append")

	except StopIteration:
		break

	finally:
		print(f"Inserted a chunk, took {time.time()-t_start:.3f} seconds")


print("data inserted successfully!!")