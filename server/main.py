from typing import Dict
from flask import Flask, request, Response, render_template
from os import path

DATABASE_PATH = "database"
class CircularBuffer:

    def __init__(self, cam_id, max_lines = 10) -> None:
        # check if file already exist if not create it
        self.max_lines = max_lines
        self.filename = f"{DATABASE_PATH}/{cam_id}.csv"
        if not path.exists(self.filename):
            with open(self.filename, 'w') as f: pass

    def add_data(self, data):
        with open(self.filename, "r") as inp:
            lines = inp.readlines()
            if len(lines) >= self.max_lines:
                lines = lines[:-1]
        lines.insert(0,data)
        with open(self.filename, "w") as out:
            out.writelines(lines)        


circular_buffers: Dict[str,CircularBuffer] = {}

app = Flask(__name__)

#implement read of existing files
@app.route('/datastream', methods=['POST'])
def my_form():
    data = list(request.form.values())
    header = ' '.join(request.form.keys())
    cam_id = data[0]
    values = ''.join(data[1:]) + '\n'

    if not cam_id in circular_buffers.keys():
        circular_buffers[cam_id] = CircularBuffer(cam_id)

    circular_buffers[cam_id].add_data(values)

    return Response(status = 204)

@app.route('/login', methods=['POST'])
def login():
    return str(list(request.form.values()))

@app.route('/')
def home():                         #aggiungere metodo di visualizzazione dei dati inseriti
    return render_template("login.html")
#mix fra dati della fotocamera e dati di home

if __name__ == '__main__':
   app.run(debug = True)

