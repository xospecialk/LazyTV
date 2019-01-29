from flask import Flask
import paramiko

app = Flask(__name__)

@app.route('/v1/control/tv/on')
def tv_on():
    turn_on = 'echo on 0 | cec-client -s -d 1'
    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    ssh.connect("192.168.0.10", username="root", password="openelec")
    ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(turn_on)
    return "success"
    
@app.route('/v1/control/tv/off')
def tv_off():
    turn_off = 'echo standby 0 | cec-client -s -d 1'
    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    ssh.connect("192.168.0.10", username="root", password="openelec")
    ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(turn_off)
    return "success"

if __name__ == "__main__":
    app.run(host='0.0.0.0')
