import numpy as np
import matplotlib.pyplot as mp
from scipy.interpolate import griddata
import matplotlib
matplotlib.use('Agg')

file_name = "templates/heatmap.html" 
image_path = "./static/images/heatmap.png"

def writepage(x):
    fo = open(file_name,"w+")
    fo.write('<html><head><style>')
    fo.write('.container { display: flex; flex-direction: column; align-items: center; text-align: center; }')
    fo.write('h1 { color: black; font-style: italic; }')
    fo.write('</style>')
    fo.write('<link rel="icon" type="image/png" href="/static/images/images.png" />') 
    fo.write('</head><body>')
    fo.write('<div class="container">')
    fo.write('<h1>Heatmap</h1>')
    fo.write('<img src="' + x + '">')
    fo.write('</div>')
    fo.write('<script type="text/javascript">')
    fo.write('setTimeout(function() {location.reload();}, 1000);')
    fo.write('</script>')
    fo.write('</body></html>')
    fo.close()


def generate_heat_map(data, coordinates):
    mp.close('all')
    
    x_known = parse_x_coordinates(coordinates)
    y_known = parse_y_coordinates(coordinates)
    temperature_known = parse_temperature(data)

    x, y = np.meshgrid(np.linspace(-1.95, 1.95, 1000), np.linspace(-3.3, 3.3, 1697))
    temperature_interpolated = griddata((x_known, y_known), temperature_known, (x, y), method='linear')

    mp.figure("imshow", figsize=(5, 6), facecolor="lightgray")
    mp.title("Heatmap", fontsize=18)

    mp.imshow(temperature_interpolated, cmap="jet", origin="lower")
    mp.colorbar(label="Temperature")
    mp.savefig(image_path)   
    writepage(image_path)

def parse_x_coordinates(coordinates):
    return [coord[0] for coord in coordinates]

def parse_y_coordinates(coordinates):
    return [coord[1] for coord in coordinates]

def parse_temperature(data):
    n = []
    i = 0
    while 2*i + 1 < len(data):
        x = data[2*i + 1]
        x = x[:-2]
        x = float(x)
        n.append(x)
        i += 1
    return n