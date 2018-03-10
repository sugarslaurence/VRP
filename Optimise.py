import requests
from URLs import *
from ApiKeys import *
import json
import time
from Files import *


def start_optimiser(objective_function = 'transport_time'):

    # Objective: vehicles, transport_time, completion_time

    url = GRAPH_HOPPER_OPTIMISE_API
    key = graph_hopper_test
    url_key = "{0}key={1}".format(url, key)
    req_body = default
    content_type = {'Content-Type': 'application/json'}
    req_body['objectives'][0]['value'] = objective_function

    req = requests.post(url=url_key, data=json.dumps(req_body), headers=content_type)
    res = req.json()
    print(res)
    job_id = res['job_id']
    time.sleep(3)

    return job_id


def get_results(job_id):

    url = GRAPH_HOPPER_OPTIMISE_RETRIEVE_RESULTS
    key = graph_hopper_test
    url_id_key = "{0}{1}?key={2}".format(url, job_id, key)

    req = requests.get(url_id_key)
    res = req.json()

    return res