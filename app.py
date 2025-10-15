from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/v2/media', methods=['POST'])
def upload_media():
    data = request.get_json()
    url = data.get('url')
    result = {"success": True, "media": {"url": url}}
    return jsonify(result)

@app.route('/v2/media/batch', methods=['POST'])
def batch_upload_media():
    urls = request.get_json().get('mediaURLs', [])
    result = {"success": True, "media": [{"url": u} for u in urls]}
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True, port=8000)
