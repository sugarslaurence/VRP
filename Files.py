default = {
    "objectives": [{
        "type": "min",
        "value": "transport_time"
    }],
    "vehicles": [{
        "vehicle_id": "1",
        "start_address": {
            "location_id": "home_location_tower_bridge",
            "lon": -0.075338,
            "lat": 51.505597
        },
        "type_id": "vehicle_type_1"
    }],
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
    }]
}
new_vehicle = {
    'vehicle_id': 'vehicleX',
    'start_address': {'location_id': 'home_location_tower_bridge', 'lon': -0.075338, 'lat': 51.505597},
    'type_id': 'vehicle_type_1'}