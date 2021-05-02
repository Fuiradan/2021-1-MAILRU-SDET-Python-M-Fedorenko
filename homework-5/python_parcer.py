#pattern = re.compile(r'(?P<ipaddress>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) (?P<identity>.+) (?P<remoteuser>.+) [(?P<dateandtime>\d{2}\/\w{3}\/\d{4}:\d{2}:\d{2}:\d{2} (\+|\-)\d{4})\] "(?:(.*))(?P<method>GET|POST|HEAD|OPTIONS|PUT|PATCH|DELETE|TRACE|CONNECT) (?P<url>.+) ([A-Z]+\/[1-2]\.\d)" (?P<statuscode>\d{3}) (?P<bytessent>.+) "(?P<refferer>()|(.+))" "(?P<useragent>()|(.+))" "(?P<CanonicalName>()|(.+))"'
import os
import re
import json
import argparse

JSON_ARG = False
client_error_pattern = r'4\d\d'
server_error_pattern = r'5\d\d'
LOG_PATH = None
OUTPUT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), './python_output.txt'))
JSON_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), './json_output.json'))
json_dict = []

def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('logfile', help='Path to logfile')
    parser.add_argument('--json', action='store_true', help='Create a JSON file with results')
    return parser

def parce_line(log_string):
    pattern = re.compile(r'(?P<ipaddress>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) (?P<identity>.+) (?P<remoteuser>.+)'\
            r' \[(?P<dateandtime>\d{2}\/\w{3}\/\d{4}:\d{2}:\d{2}:\d{2} ' \
            r'(\+|\-)\d{4})\] "(?:(.*))(?P<method>GET|POST|HEAD|OPTIONS|PUT|PATCH|DELETE|TRACE|CONNECT) '\
            r'(?P<url>.+)(\?*) ([A-Z]+\/[1-2]\.\d)" (?P<statuscode>\d{3}) '\
            r'(?P<bytessent>(-)|(\d+))')
    data = re.search(pattern, log_string)
    datadict = data.groupdict()
    return datadict

def parse_data_for_json(data):
    tmp_dict = dict()
    splitted_string = data.strip().split('\n')
    for i in splitted_string:
        another_split = i.split(': ')
        tmp_dict[another_split[0]] = another_split[1]
    return tmp_dict



def create_json(json_dict):
    json_res = json.dumps(json_dict, indent=2)
    with open(JSON_PATH , 'a') as jf:
        jf.write(json_res)
        jf.close()

def get_results_to_file(header_str, str_template, data, quantity=None):
    if JSON_ARG: 
        tmp_dict = dict()  
    with open(OUTPUT_PATH, 'a') as out:
        out.write(header_str)
        if JSON_ARG:
            tmp_dict['info'] = header_str.strip()
            tmp_dict['data'] = []
        if quantity != None:
            for i in range(quantity):
                string = str_template.format(data[i])
                out.write(string)
                if JSON_ARG:
                    parsed_data = parse_data_for_json(string)
                    tmp_dict['data'].append(parsed_data)
        else:
            for i in range(len(data)):
                string = str_template.format(data[i])
                out.write(string)
                if JSON_ARG:
                    parsed_data = parse_data_for_json(string)
                    tmp_dict['data'].append(parsed_data)
        out.close()
    if JSON_ARG:
        json_dict.append(tmp_dict)

def read_file_line(file_name):
    with open(file_name, 'r') as f:
        while True:
            line = f.readline()
            if not line:
                break
            yield line.rstrip()
        f.close()

def init_outputfile(filepath):
    if JSON_ARG:
        f = open(JSON_PATH, 'w')
        f.close()
    f = open(filepath, 'w')
    f.close()

def create_reqs_with_client_error():
    log_lines = read_file_line(LOG_PATH)
    reqs_list = []
    for line in log_lines:
        data = parce_line(line)
        statuscode = re.match(client_error_pattern, data['statuscode'])
        if statuscode != None:
            request = data['url']
            bytes = data['bytessent']
            ip = data['ipaddress']
            statuscode = statuscode.string
            reqs_list.append([request, statuscode, bytes, ip])
        else:
            pass
    return reqs_list

def create_dict_with_cliets():
    log_lines = read_file_line(LOG_PATH)
    top_clients = dict()
    for line in log_lines:
        data = parce_line(line)
        statuscode = re.match(server_error_pattern, data['statuscode'])
        if statuscode != None:
            ip = data['ipaddress']
            if ip in top_clients:
                top_clients[ip] += 1
            else:
                top_clients[ip] = 1
    return top_clients 

def create_dict_with_req_types():
    log_lines = read_file_line(LOG_PATH)
    number_of_types = dict()   
    for line in log_lines:
        data = parce_line(line)
        m_type = data['method']
        if m_type in number_of_types:
            number_of_types[m_type] += 1
        else:
            number_of_types[m_type] = 1
    return number_of_types

def create_dict_with_requests():
    log_lines = read_file_line(LOG_PATH)
    number_of_requests = dict()
    for line in log_lines:
        data = parce_line(line)
        url = data['url']
        if url in number_of_requests:
            number_of_requests[url] += 1
        else:
            number_of_requests[url] = 1
    return number_of_requests

def sort_reqs_by_size(req_list):
    return sorted(req_list, key= lambda x: x[2], reverse=True)

def sort_dict(data):
    return sorted(data.items(), key=lambda x: x[1], reverse=True)

def top_requests():
    reqs = create_dict_with_requests()
    sort_res = sort_dict(reqs)
    header = "\nTop 10 of requests\n"
    template = 'Url: {0[0]}\nRequests: {0[1]}\n'
    get_results_to_file(header, template, sort_res, 10)

def count_requests():
    res = create_dict_with_requests()
    header = 'Total number of requests\n'
    template = 'Requests: {}\n'
    data = [len(res)]
    get_results_to_file(header, template, data)

def biggest_reqs_with_client_errors():
    reqs = create_reqs_with_client_error()
    sorted_reqs = sort_reqs_by_size(reqs)
    header = '\nTop 5 largest requests with client error\n'
    template = 'Url: {0[0]}\nStatuscode: {0[1]}\nSize: {0[2]}\nIp: {0[3]}\n'
    get_results_to_file(header, template, sorted_reqs, 5)

def count_reqs_by_method():
    reqs = create_dict_with_req_types()
    sorted_data = sort_dict(reqs)
    header = '\nTotal number of requests by method\n'
    template = 'Method: {0[0]}\nRequests: {0[1]}\n'
    get_results_to_file(header, template, sorted_data)


def top_clients_with_server_error():
    clients = create_dict_with_cliets()
    sorted_clients = sort_dict(clients)
    header = '\nTop 5 users by the number of requests that ended with a server error\n'
    template = 'IP: {0[0]}\nRequests: {0[1]}\n'
    get_results_to_file(header, template, sorted_clients, 5)


if __name__ == '__main__':
    parser = create_parser()
    namespace = parser.parse_args()
    JSON_ARG = namespace.json
    LOG_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), namespace.logfile))
    init_outputfile(OUTPUT_PATH)
    count_requests()
    top_requests()
    count_reqs_by_method()
    biggest_reqs_with_client_errors()
    top_clients_with_server_error()
    if JSON_ARG:
        create_json(json_dict) 