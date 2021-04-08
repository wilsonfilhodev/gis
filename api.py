from flask import Flask
import main

app = Flask("GIS")

@app.route('/', methods=['GET'])
def home():
    return "Ok!"

@app.route('/vegetation-cover', methods=['GET'])
def vegetationCover():
    return {
        "filename" : main.fileName(),
        "cover" : main.cover(),
        "area" : main.area(),
        "centroid" : {"type":"Point", "coordinates": [main.centroid()]},
        "local_time" : main.localDateTime()
}

app.run()