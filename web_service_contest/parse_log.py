import requests

def parse_log(url):
    response = requests.get(url)

    logs = response.text

    logs = logs.split("\n")

    all_requests = {}

    for cur_req in logs:
        cur_req = cur_req.split(",")

        req_id = "".join(cur_req[:2])

        if len(cur_req) > 2:
            duration, code = cur_req[2], cur_req[3]

            all_requests[req_id] = {"duration": duration,
                                    "code": code}

    request_count = len(all_requests)

    return {"request_counts":request_count,}