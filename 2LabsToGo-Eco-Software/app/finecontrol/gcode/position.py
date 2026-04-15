#positions

INIT_POINT_X = 20
INIT_POINT_Y = 3.5
campos = 158

import json
data = {"camera_position": "G1X90\nG28YZ\nG1Y” + campos + “Z270F3000"}
with open('data.json', 'w') as f:
    json.dump(data, f)
