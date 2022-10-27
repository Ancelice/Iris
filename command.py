import os
from iris_client import IrisClient, AsyncIrisClient

# Iris credentials
base_url = "https://api.iris.dioptra.io"
username = "mg22019@shibaura-it.ac.jp"
password = "Hiro@114"
#username = os.environ.get("IRIS_USERNAME")
#password = os.environ.get("IRIS_PASSWORD")
if not username or not password:
    raise ValueError("IRIS_USERNAME and IRIS_PASSWORD environment variables must be set")

# Check out https://github.com/dioptra-io/iris-client for more info on IrisClient
with IrisClient(base_url, username, password) as iris:
    measurements = iris.all("/measurements/public", params={"tag": "collection:exhaustive"})

#####

# We select the measurement we want to query (newest measurement)
measurement = measurements[0]

#####

# Get temporary access token to the database for this measurement
with IrisClient(base_url, username, password) as iris:
    me = iris.get("/users/me/services", params={"measurement_uuid": measurement["uuid"]}).json()
    credentials = dict(
        base_url=me["clickhouse"]["base_url"],
        database="iris",
        username=me["clickhouse"]["username"],
        password=me["clickhouse"]["password"]
    )

#####

def format_uuid(uuid):
    return uuid.replace("-", "_")

def get_tables(measurement, data_type="results"):
    """
    Get the table of each agent in the measurement.
    """
    return [
        f"{data_type}__{format_uuid(measurement['uuid'])}__{format_uuid(agent['agent_uuid'])}" 
        for agent in measurement["agents"]
    ]

#####

# Get reply table names for this measurement
tables = get_tables(measurement)

#####

data = []
i = 0

from pych_client import ClickHouseClient

# Check out https://github.com/dioptra-io/pych-client for more info on ClickHouseClient
with ClickHouseClient(**credentials) as client:
    for row in client.iter_json(
        f"SHOW tables"
    ):
        print(row)