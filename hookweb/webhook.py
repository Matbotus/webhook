from flask import Flask, request
import logging
from datetime import datetime

app = Flask(__name__)

# Set up logging
logging.basicConfig(filename='detailed_visitor_logs.txt', level=logging.INFO)

@app.route('/')
def log_data():
    # Get visitor's IP address
    visitor_ip = request.remote_addr

    # Get user agent (browser, OS details)
    user_agent = request.headers.get('User-Agent')

    # Get the referrer URL
    referrer = request.referrer if request.referrer else "No referrer"

    # Get all request headers
    headers = dict(request.headers)

    # Get the request method (GET, POST, etc.)
    method = request.method

    # Get any query parameters
    query_params = request.args.to_dict()

    # Get the host (server) information
    host = request.host

    # Get cookies sent with the request
    cookies = request.cookies

    # Get the specific path requested
    path = request.path

    # Get the current timestamp
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # Log the data
    log_entry = (
        f"Time: {timestamp}, IP: {visitor_ip}, User-Agent: {user_agent}, "
        f"Referrer: {referrer}, Method: {method}, Path: {path}, "
        f"Query Params: {query_params}, Host: {host}, Cookies: {cookies}, "
        f"Headers: {headers}"
    )
    
    logging.info(log_entry)

    return "Detailed Data Logged"

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)
