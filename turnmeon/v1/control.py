from flask_restful import Resource
from flask_restful import reqparse
import paramiko


class Control(Resource):

    def __init__(self):
        self.parser = reqparse.RequestParser()

    def get(self):
        ssh = paramiko.SSHClient()
        ssh.load_system_host_keys()
        ssh.connect("192.168.0.10", username="root", password="openelec")
        ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command('echo on 0 | cec-client -s -d 1')


