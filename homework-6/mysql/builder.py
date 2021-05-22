from mysql.models import TopRequests, TotalRequests, ClientErrorRequests, RequestsByMethod, ServerErrorUsers
from parcer.app import LogParcer

class MySQL_Builder:
    parcer = LogParcer()

    def __init__(self, client):
        self.client = client

    def write_TopRequests(self):
        parced_data = self.parcer.top_requests()
        for data in parced_data:
            record = TopRequests(
                url = data[0], 
                quantity = data[1]
            )
            self.client.session.add(record)
        records = self.client.session.query(TopRequests).all()
        return parced_data, records

    def write_TotalRequests(self):
        parced_data = self.parcer.count_requests()
        record = TotalRequests(
                quantity = parced_data[0]
            )
        self.client.session.add(record)
        records = self.client.session.query(TotalRequests).all()
        return parced_data, records

    def write_ClientErrorRequests(self):
        parced_data = self.parcer.biggest_reqs_with_client_errors()
        for data in parced_data:
            record = ClientErrorRequests(
                url = data[0], 
                statuscode = data[1],
                size = data[2],
                ip = data[3]
            )
            self.client.session.add(record)
        records = self.client.session.query(ClientErrorRequests).all()
        return parced_data, records       

    def write_RequestsByMethod(self):
        parced_data = self.parcer.count_reqs_by_method()
        for data in parced_data:
            record = RequestsByMethod(
                method = data[0], 
                quantity = data[1]
            )
            self.client.session.add(record)
        records = self.client.session.query(RequestsByMethod).all()
        return parced_data, records

    def write_ServerErrorUsers(self):
        parced_data = self.parcer.top_clients_with_server_error()
        for data in parced_data:
            record = ServerErrorUsers(
                ip = data[0], 
                quantity = data[1]
            )
            self.client.session.add(record)
        records = self.client.session.query(ServerErrorUsers).all()
        return parced_data, records