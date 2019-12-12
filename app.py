from flask import Flask, render_template, request, session, redirect, url_for, make_response, jsonify
import json, datetime, requests
app = Flask(__name__)


@app.route('/')
def index():
  return render_template('tables.html',date=datetime.date.today())

@app.route('/library_report')
def library_report():
    return render_template('library_report.html')


@app.route('/get_library_report')
def get_library_report():
    data =json.dumps( [{"case_name":"jks.L3_dybanuc_alu_host_vitis_sw_emu", "case_number":1, "Test_case_url":"Test case url address", "Test_Result":"PASS", "Unique_Error":"XXXXXXXXXXXXXXXXXXXXX"}])  
    data = {"data":json.loads(data)}
    return jsonify(data)

@app.route('/issues_get_data')
def update_issues():
    #issues_url="https://api.github.com/repos/pyecharts/pyecharts/issues" #test url address
    issues_url="https://api.github.com/repos/Xilinx/Vitis_Libraries/issues"
    #response = requests.get(issues_url)
    data={"data":json.loads(requests.get(issues_url).text)}
    return jsonify(data)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, threaded=True)