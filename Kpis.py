def schedule_kpis(schedule, resources="optional"):

    kpis = []

    # Solution Review

    solution = schedule['solution']

    distance = {}
    scheduled_distance = solution['distance']
    distance['total_distance'] = scheduled_distance
    kpis.append(distance)

    scheduled_time = solution['time']
    kpis[-1]['total_drive_time'] = scheduled_time

    scheduled_vehicles = solution['no_vehicles']
    kpis[-1]['used_vehicles'] = scheduled_vehicles

    scheduled_unassigned = solution['no_unassigned']
    kpis[-1]['unassigned_services'] = scheduled_unassigned

    routes = 0
    for route in solution['routes']:
        routes += 1
    scheduled_routes = routes
    kpis[-1]['scheduled_routes'] = scheduled_routes

    scheduled_cost = solution['costs']
    kpis[-1]['cost'] = scheduled_cost

    job_id = schedule['job_id']
    kpis[-1]['job_id'] = job_id

    return kpis

    # Resource Review

    vehicles = 0
    for vehicle in resources['vehicles']:
        vehicles += 1
    available_vehicles = vehicles


    # Plan vs Actual

    unused_vehicles = available_vehicles - scheduled_vehicles
    print(unused_vehicles)

    return "done"

def schedule_metadata(schedule):

    processing_time = schedule['processing_time']

    return "done"


