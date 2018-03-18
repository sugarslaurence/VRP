from Compiler import *
from Import import *
from Optimise import *

services = read_services()
vehicles = read_vehicles()

request = graph_hopper_request_builder(vehicles, services)
id = start_optimiser(request)
print(id)
result = get_results(id)
#kpis = schedule_kpis(result)

print(result)
#print(kpis)

