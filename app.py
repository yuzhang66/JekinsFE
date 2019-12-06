from flask import Flask, render_template, request, session, redirect, url_for, make_response, jsonify
import json
app = Flask(__name__)

@app.route('/')
def index():
  return render_template('tables.html')

@app.route('/library_report')
def library_report():
    return render_template('library_report.html')

@app.route('/get_library_report')
def get_library_report():
    data ={"data":json.loads( '{"case_name": "jks.L3_dybanuc_alu_host_vitis_sw_emu", "case_number": 1, "Test_case_url":"Test case url address" , "Test Result":"pass", "Unique_Error":"XXXXXXXXXXXXXXXXXXXXX", }' ) } 
    return jsonify(data)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, threaded=True)