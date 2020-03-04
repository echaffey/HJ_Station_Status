from flask import Flask, render_template, url_for
from pythonping import ping


app = Flask(__name__)

def read_file(path):
    with open(path, 'r') as f:
        x = f.read().splitlines()
    return x

@app.route('/')
@app.route('/home')
def home(methods=['GET', 'POST']):
    # data = ping('10.1.124.1', count=1)
    status = []
    id_names = []
    ip_addr = []
    for line in read_file('pi_routes.txt'):
        temp = line.split(':')
        data = ping(temp[1], count=1)
        status.append(data.success())
        id_names.append(temp[0])
        ip_addr.append(temp[1])

    return render_template('/home.html', status=status, id_names=id_names, ip_addr=ip_addr)

@app.route('/table')
def table():
    status = []
    id_names = []
    ip_addr = []
    for line in read_file('pi_routes.txt'):
        temp = line.split(':')
        data = ping(temp[1], count=1)
        status.append(data.success())
        id_names.append(temp[0])
        ip_addr.append(temp[1])

    return render_template('/table.html', status=status, id_names=id_names, ip_addr=ip_addr)
if __name__ == '__main__':
    app.run(debug=True)