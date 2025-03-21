import os
import logging
import requests
from dotenv import load_dotenv
from flask import Flask, jsonify, request
from flask_cors import CORS

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

load_dotenv()

app = Flask(__name__)
CORS(app)

def json_response(data, status=200):
    """Standardized JSON response format"""
    return jsonify({
        "status": "success" if 200 <= status < 300 else "error",
        "data": data
    }), status

def fetch_call_details(call_id):
    """Fetch call details from VAPI API with error handling"""
    url = f"https://api.vapi.ai/call/{call_id}"
    headers = {
        "Authorization": f"Bearer {os.getenv('VAPI_API_KEY')}"
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()  # Raises HTTPError for 4xx/5xx responses
        data = response.json()
        
        if not data.get("success"):
            logger.error(f"API Error: {data.get('error', 'Unknown error')}")
            raise ValueError(data.get("error", "API returned unsuccessful response"))
            
        return data
    except requests.exceptions.RequestException as e:
        logger.error(f"Request failed: {str(e)}")
        raise
    except ValueError as e:
        logger.error(f"Invalid response format: {str(e)}")
        raise

@app.route("/call-details", methods=["GET"])
def get_call_details():
    """Get call details with improved error handling"""
    call_id = request.args.get("call_id")
    if not call_id:
        logger.warning("Call ID is missing from the request")
        return json_response({"error": "Call ID is required"}, 400)
    
    try:
        response = fetch_call_details(call_id)
        summary = response.get("summary")
        analysis = response.get("analysis")
        
        if summary is None or analysis is None:
            logger.warning(f"Summary or analysis missing for call ID: {call_id}")
            return json_response({"error": "Summary or analysis missing"}, 500)
        
        return json_response({"analysis": analysis, "summary": summary}, 200)
    except Exception as e:
        logger.exception(f"Error fetching call details for call ID: {call_id}")
        return json_response({"error": str(e)}, 500)
    
if __name__ == "__main__":
    app.run(debug=True)
