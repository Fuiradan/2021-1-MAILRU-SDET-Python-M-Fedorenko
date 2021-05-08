import re
import os

client_error_pattern = r'4\d\d'
server_error_pattern = r'5\d\d'

class LogParcer():
    def __init__(self):
        self.path_to_logfile = os.path.abspath(os.path.join(os.path.dirname(__file__), 'access.log'))

    def parce_line(self, log_string):
        pattern = re.compile(r'(?P<ipaddress>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) (?P<identity>.+) (?P<remoteuser>.+)'\
                r' \[(?P<dateandtime>\d{2}\/\w{3}\/\d{4}:\d{2}:\d{2}:\d{2} ' \
                r'(\+|\-)\d{4})\] "(?:(.*))(?P<method>GET|POST|HEAD|OPTIONS|PUT|PATCH|DELETE|TRACE|CONNECT) '\
                r'(?P<url>.+)(\?*) ([A-Z]+\/[1-2]\.\d)" (?P<statuscode>\d{3}) '\
                r'(?P<bytessent>(-)|(\d+))')
        data = re.search(pattern, log_string)
        datadict = data.groupdict()
        return datadict
    
    def read_file_line(self, file_name):
        with open(file_name, 'r') as f:
            while True:
                line = f.readline()
                if not line:
                    break
                yield line.rstrip()
            f.close()
    
    def create_reqs_with_client_error(self):
        log_lines = self.read_file_line(self.path_to_logfile)
        reqs_list = []
        for line in log_lines:
            data = self.parce_line(line)
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

    def create_dict_with_cliets(self):
        log_lines = self.read_file_line(self.path_to_logfile)
        top_clients = dict()
        for line in log_lines:
            data = self.parce_line(line)
            statuscode = re.match(server_error_pattern, data['statuscode'])
            if statuscode != None:
                ip = data['ipaddress']
                if ip in top_clients:
                    top_clients[ip] += 1
                else:
                    top_clients[ip] = 1
        return top_clients 

    def create_dict_with_req_types(self):
        log_lines = self.read_file_line(self.path_to_logfile)
        number_of_types = dict()   
        for line in log_lines:
            data = self.parce_line(line)
            m_type = data['method']
            if m_type in number_of_types:
                number_of_types[m_type] += 1
            else:
                number_of_types[m_type] = 1
        return number_of_types

    def create_dict_with_requests(self):
        log_lines = self.read_file_line(self.path_to_logfile)
        number_of_requests = dict()
        for line in log_lines:
            data = self.parce_line(line)
            url = data['url']
            if url in number_of_requests:
                number_of_requests[url] += 1
            else:
                number_of_requests[url] = 1
        return number_of_requests

    def sort_reqs_by_size(self, req_list):
        return sorted(req_list, key= lambda x: x[2], reverse=True)

    def sort_dict(self, data):
        return sorted(data.items(), key=lambda x: x[1], reverse=True)

    def top_requests(self):
        reqs = self.create_dict_with_requests()
        sort_res = self.sort_dict(reqs)
        return sort_res[:10]

    def count_requests(self):
        res = self.create_dict_with_requests()
        data = [len(res)]
        return data

    def biggest_reqs_with_client_errors(self):
        reqs = self.create_reqs_with_client_error()
        sorted_reqs = self.sort_reqs_by_size(reqs)
        return sorted_reqs[:5]

    def count_reqs_by_method(self):
        reqs = self.create_dict_with_req_types()
        sorted_data = self.sort_dict(reqs)
        return sorted_data

    def top_clients_with_server_error(self):
        clients = self.create_dict_with_cliets()
        sorted_clients = self.sort_dict(clients)
        return sorted_clients[:5]
