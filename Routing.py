import requests
from ApiKeys import *
from pprint import pprint as pp
from URLs import *

class graph_hopper:

    # Distance API: Time, Distance, Path

    def graph_hopper_routing(self, shipFrom, shipTo, vehicle = "car", locale = "de"):

        base_url = GRAPH_HOPPER_ROUTING_API
        key = graph_hopper_test
        url = "{0}{1}&point={2}&vehicle={3}&locale={4}&key={5}".format(base_url, shipFrom, shipTo, vehicle,locale, key)
        req = requests.get(url)
        res = req.json()
        distance = res['paths'][0]['distance'] / 1000
        time = round(res['paths'][0]['time'] * 0.001, 1)
        ascend = res['paths'][0]['ascend']
        descend = res['paths'][0]['descend']

        def net_ascend_descend(ascend, descend):    # Returns whether the journey net ascends or descends
            if ascend - descend < 0:
                return "Descend: {0}".format(round(descend - ascend, 1))
            else:
                return "Ascend: {0}".format(round(ascend - descend, 1))

        dict = {}
        dict['distance'] = distance
        dict['time'] = time
        dict['ascend'] = ascend
        dict['descend'] = descend
        dict['net_ascend_descend'] = net_ascend_descend(ascend, descend)

        return dict


class routing:

    def driver_route(schedule):
        pass

