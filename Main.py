from Optimise import *
from Files import *
from pprint import pprint as pp

def graph_hopper_request_builder(vehicles):

    default_body = default
    new_vehicle_template = default_body['vehicles'][0]  # dict


    vehicles_list = []

    for x in range(0, vehicles):

        vehicle = new_vehicle_template.copy()
        vehicle['vehicle_id'] = str(x + 1)
        vehicles_list.append(vehicle)

    default_body["vehicles"] = vehicles_list
    print(pp(default_body))

    return default_body

graph_hopper_request_builder(5)

body = graph_hopper_request_builder(5)
id = start_optimiser(body)
result = get_results(id)
print(result)






