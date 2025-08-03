from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "Home"

@app.route("/get-user/<user_id>")
def get_user(user_id):
    user_data = {
        "user_id" : user_id,
        "name" : "Ola Nordmann",
        "email" : "olanor@gmail.com"
    }
    
    extra = request.args.get("extra")
    if extra:
        user_data["extra"] = extra
        
    return jsonify(user_data), 200

@app.route("/create-user", methods = ["POST"])
def create_user():
    # if request.method == "POST":
    data = request.get_json()
    
    return jsonify(data), 201
    

if __name__ == "__main__":
    port = 5000  # The port your Flask app listens to inside container
    
    # The host port your Docker maps to, usually 5000, but can be changed in docker-compose.yml
    docker_host_port = os.environ.get("DOCKER_HOST_PORT", port)
    
    print(f" * Running on http://localhost:{docker_host_port} (Press CTRL+C to quit)")
    
    
    app.run(host="0.0.0.0", port=port, debug=True)