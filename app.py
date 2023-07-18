from flask import Flask,render_template,jsonify,redirect,request
import serial_post
import heat_map

app = Flask(__name__)

sensor_coordinates = [(-1,2.8),(-1.95,-3.3),(-0.95,1.3),(-1.95,3.3),(1.95,0),(0.95,2.3),(-0.5,2.3),(1.95,3.3),(1.95,-3.3)]

@app.route('/sensor1')
def get_sensor1_data():
    data_list = serial_post.refresh()
    return jsonify({"temperature" : data_list[1]})

@app.route("/temperature")
def show_Temperature():
    if(serial_post.ReadyToRead()==True):
        serial_post.refresh()
    return render_template("serial.html")

@app.route("/heatmap")
def heatmap():
    if(serial_post.ReadyToRead()==True):
        data_list = serial_post.refresh()
        heat_map.generate_heat_map(data_list,sensor_coordinates)
    return render_template("heatmap.html")

@app.errorhandler(Exception)
def handle_error(error):
    return redirect(request.url)

if __name__ == '__main__':
    serial_post.init()
    app.run(host='0.0.0.0', port=5200, debug=True)
        