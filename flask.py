from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/v2/media', methods=['POST'])
def upload_media():
    # Extract posted data (from n8n's HTTP request body)
    data = request.get_json()
    url = data.get('url')

    # Mimic Blotato response, here you could add your own posting logic
    result = {
        "success": True,
        "media": {
            "url": url,
            # Add other fields if needed for downstream workflows
        }
    }
    return jsonify(result)

# To support batch/combine:
@app.route('/v2/media/batch', methods=['POST'])
def batch_upload_media():
    urls = request.get_json().get('mediaURLs', [])
    result = {
        "success": True,
        "media": [{"url": u} for u in urls]
    }
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
