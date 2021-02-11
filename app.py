import json
import datetime
from flask import Flask, request, jsonify
app = Flask(__name__)


@app.route("/")
def read(key='time'):
    # read start_time and end_time from url
    start_time = request.args.get("start_time", "2021-01-28 08:30:00")
    end_time = request.args.get("end_time", "2021-01-28 10:30:00")
    print(start_time,end_time)
    # opening of json file
    with open('db.json', 'r') as r:
        data = json.load(r)
    
    runtime = downtime = totaltime = 0.00
    #traverse all elements of data
    for i in range(len(data)):
        # checking for given duration
        if(data[i][key] >= start_time and data[i][key] <= end_time):
            #if runtime <=1021 then add total time in runtime
            if(float(data[i]["runtime"])<=1021):
                runtime += int(data[i]["runtime"])
            #else time-1021 put in downtime
            else:
                runtime += 1021
                downtime+=int(data[i]["runtime"])-1021
            totaltime+=int(data[i]["runtime"])
    #find utilization
    utilization = (runtime*100)/totaltime
    #storing all values in dictionary dict1
    dict1 = {
                "runtime":str(datetime.timedelta(seconds = runtime)),
                "downtime":str(datetime.timedelta(seconds = downtime)),
                "utilization":utilization
             }
    
    return jsonify(dict1)