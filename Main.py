import requests
from URLs import *
from ApiKeys import *
import json
import time

default = {
    "objectives": [{
            "type": "min",
            "value": "vehicles"
        },
        {
            "type": "min",
            "value": "transport_time"
        }
    ],
    "vehicles": [{
            "vehicle_id": "vehicle1",
            "start_address": {
                "location_id": "home_location_tower_bridge",
                "lon": -0.075338,
                "lat": 51.505597
            },
            "type_id": "vehicle_type_1"
        },
        {
            "vehicle_id": "vehicle2",
            "start_address": {
                "location_id": "home_location_tower_bridge",
                "lon": -0.075338,
                "lat": 51.505597
            },
            "type_id": "vehicle_type_1"
        }, {
            "vehicle_id": "vehicle3",
            "start_address": {
                "location_id": "home_location_tower_bridge",
                "lon": -0.075338,
                "lat": 51.505597
            },
            "type_id": "vehicle_type_1"
        }, {
            "vehicle_id": "vehicle4",
            "start_address": {
                "location_id": "home_location_tower_bridge",
                "lon": -0.075338,
                "lat": 51.505597
            },
            "type_id": "vehicle_type_1"
        }
    ],
    "vehicle_types": [{
        "type_id": "vehicle_type_1",
        "profile": "car",
        "capacity": [3]
    }],
    "services": [{
            "id": "1",
            "name": "chelsea_bridge",
            "address": {
                "location_id": "loc_1",
                "lon": -0.149832,
                "lat": 51.484484
            },
            "size": [1]
        },
        {
            "id": "2",
            "name": "southwark_bridge",
            "address": {
                "location_id": "loc_2",
                "lon": -0.094011,
                "lat": 51.508902
            },
            "size": [1]
        },
        {
            "id": "3",
            "name": "victoria_park",
            "address": {
                "location_id": "loc_3",
                "lon": -0.038972,
                "lat": 51.536561
            },
            "size": [1]
        },
        {
            "id": "4",
            "name": "hyde_park",
            "address": {
                "location_id": "loc_4",
                "lon": -0.165730,
                "lat": 51.507268
            },
            "size": [1]
        },
        {
            "id": "5",
            "name": "clapham_common",
            "address": {
                "location_id": "loc_5",
                "lon": -0.149261,
                "lat": 51.458452
            },
            "size": [1]
        },
        {
            "id": "6",
            "name": "battersea_park",
            "address": {
                "location_id": "loc_6",
                "lon": -0.156498,
                "lat": 51.479107
            },
            "size": [1]
        },
        {
            "id": "7",
            "name": "",
            "address": {
                "location_id": "borough",
                "lon": -0.091522,
                "lat": 51.503470
            },
            "size": [1]
        },
        {
            "id": "8",
            "name": "westfield_shopping",
            "address": {
                "location_id": "loc_11",
                "lon": -0.221122,
                "lat": 51.507531
            },
            "size": [1]
        }
    ]
}
four_cars_eight_services = {
    "objectives": [{
            "type": "min",
            "value": "transport_time"
        },
    ],
    "vehicles": [{
            "vehicle_id": "vehicle1",
            "start_address": {
                "location_id": "home_location_tower_bridge",
                "lon": -0.075338,
                "lat": 51.505597
            },
            "type_id": "vehicle_type_1"
        },
        {
            "vehicle_id": "vehicle2",
            "start_address": {
                "location_id": "home_location_tower_bridge",
                "lon": -0.075338,
                "lat": 51.505597
            },
            "type_id": "vehicle_type_1"
        }, {
            "vehicle_id": "vehicle3",
            "start_address": {
                "location_id": "home_location_tower_bridge",
                "lon": -0.075338,
                "lat": 51.505597
            },
            "type_id": "vehicle_type_1"
        }, {
            "vehicle_id": "vehicle4",
            "start_address": {
                "location_id": "home_location_tower_bridge",
                "lon": -0.075338,
                "lat": 51.505597
            },
            "type_id": "vehicle_type_1"
        }
    ],
    "vehicle_types": [{
        "type_id": "vehicle_type_1",
        "profile": "car",
        "capacity": [3]
    }],
    "services": [{
            "id": "1",
            "name": "chelsea_bridge",
            "address": {
                "location_id": "loc_1",
                "lon": -0.149832,
                "lat": 51.484484
            },
            "size": [1]
        },
        {
            "id": "2",
            "name": "southwark_bridge",
            "address": {
                "location_id": "loc_2",
                "lon": -0.094011,
                "lat": 51.508902
            },
            "size": [1]
        },
        {
            "id": "3",
            "name": "victoria_park",
            "address": {
                "location_id": "loc_3",
                "lon": -0.038972,
                "lat": 51.536561
            },
            "size": [1]
        },
        {
            "id": "4",
            "name": "hyde_park",
            "address": {
                "location_id": "loc_4",
                "lon": -0.165730,
                "lat": 51.507268
            },
            "size": [1]
        },
        {
            "id": "5",
            "name": "clapham_common",
            "address": {
                "location_id": "loc_5",
                "lon": -0.149261,
                "lat": 51.458452
            },
            "size": [1]
        },
        {
            "id": "6",
            "name": "battersea_park",
            "address": {
                "location_id": "loc_6",
                "lon": -0.156498,
                "lat": 51.479107
            },
            "size": [1]
        },
        {
            "id": "7",
            "name": "",
            "address": {
                "location_id": "borough",
                "lon": -0.091522,
                "lat": 51.503470
            },
            "size": [1]
        },
        {
            "id": "8",
            "name": "westfield_shopping",
            "address": {
                "location_id": "loc_11",
                "lon": -0.221122,
                "lat": 51.507531
            },
            "size": [1]
        }
    ]
}

def start_optimiser(objective_function = 'transport_time'):

    # Objective: vehicles, transport_time, completion_time

    url = GRAPH_HOPPER_OPTIMISE_API
    key = graph_hopper_test
    url_key = "{0}key={1}".format(url, key)
    req_body = four_cars_eight_services
    content_type = {'Content-Type': 'application/json'}
    req_body['objectives'][0]['value'] = objective_function

    req = requests.post(url=url_key, data=json.dumps(req_body), headers=content_type)
    res = req.json()
    print(res)
    job_id = res['job_id']

    return job_id


def get_results(job_id):

    url = GRAPH_HOPPER_OPTIMISE_RETRIEVE_RESULTS
    key = graph_hopper_test
    url_id_key = "{0}{1}?key={2}".format(url, job_id, key)

    req = requests.get(url_id_key)
    res = req.json()

    return res


job = start_optimiser('vehicles')
time.sleep(3)
result = get_results(job)
kpis = schedule_kpis(result)
print(kpis)


