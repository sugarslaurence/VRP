from Files import *
from pprint import pprint as pp

def graph_hopper_request_builder(vehicles, services, objectives, objective_types = 'min'):

    default_body = default

    # Add vehicles

    new_vehicle_template = default_body['vehicles'][0]
    no_head_vehicles = vehicles[1:]

    vehicles = []
    for x in no_head_vehicles:
        request_vehicle = {}
        request_vehicle['vehicle_quantity'] = x[0]
        request_vehicle['vehicle_type'] = x[1]
        request_vehicle['vehicle_lat'] = float(x[2])
        request_vehicle['vehicle_lon'] = float(x[3])
        request_vehicle['vehicle_location_id'] = x[4]
        vehicles.append(request_vehicle)

    vehicles_list = []
    for x in range(0, len(vehicles)):
        vehicle = new_vehicle_template.copy()
        vehicle['vehicle_id'] = str(x + 1)
        vehicle['start_address']['lat'] = vehicles[x]['vehicle_lat']
        vehicle['start_address']['lon'] = vehicles[x]['vehicle_lon']
        vehicle['start_address']['location_id'] = vehicles[x]['vehicle_location_id']
        vehicles_list.append(vehicle)

    default_body["vehicles"] = vehicles_list

    # Add services

    new_service_template = default_body['services'][0]
    services_list = []
    new_address_template = default_body['services'][0]['address']
    services_bound = len(services)

    for x in range(0, services_bound - 1):
        service = new_service_template.copy()
        address = new_address_template.copy()
        service['id'] = services[x + 1][0]
        service['name'] = services[x + 1][1]
        address['location_id'] = str(x + 1)
        address['lon'] = float(services[x + 1][3])
        address['lat'] = float(services[x + 1][2])
        service['address'] = address
        services_list.append(service)

    default_body['services'] = services_list


    # Determine Objective Function

    objective_list = []
    for x in objectives:
        objective_list.append(x[1])

    objective_type_list = []
    for x in objective_types:
        objective_type_list.append(x[1])

    list = []
    for x in objective_list:
        for y in objective_type_list:
            loop_list = []
            loop_list.append(x)
            loop_list.append(y)
            list.append(loop_list)



    new_objective_template = default_body['objectives'][0]

    list_of_objectives = []

    for x in range(0, len(list)):
        objective = new_objective_template.copy()
        objective['value'] = list[x][0]
        objective['type'] = list[x][1]
        list_of_objectives.append(objective)

    list_bodies = []

    for x in list_of_objectives:
        body = default_body.copy()
        body['objectives'] = x
        list_bodies.append(body)

    return list_bodies
