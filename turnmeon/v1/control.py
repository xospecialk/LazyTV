from flask_restful import Resource
from flask_restful import reqparse
import paramiko


class Control(Resource):

    turn_on = 'echo on 0 | cec-client -s -d 1'
    turn_off = 'echo standby 0 | cec-client -s -d 1'

    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('action')

    def get(self):
        args = self.parser.parse_args()
        action = args.get('action')
        ssh = paramiko.SSHClient()
        ssh.load_system_host_keys()
        ssh.connect("192.168.0.10", username="root", password="openelec")
        if action == "on":
            ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(self.turn_on)
        else:
            ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(self.turn_off)


