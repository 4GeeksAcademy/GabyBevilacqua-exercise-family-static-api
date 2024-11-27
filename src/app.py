"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

# create the jackson family object
jackson_family = FamilyStructure("Bevilacqua")

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/members', methods=['GET'])
def get_members():
    # get all family members
    members = jackson_family.get_all_members()
    # si todos los familiares are fetch correctamente la respuesta 
    # es la lista de miembros y el numero 200 de success
    return jsonify(members), 200

@app.route('/member/<int:member_id>', methods=['GET'])
def get_member(member_id):
    # get one family member basado en un id
    member = jackson_family.get_member(member_id)
    # si el familiar are fetch correctamente la respuesta 
    # es el miembro al frontend y el numero 200 de success
    return jsonify(member), 200

@app.route('/member', methods=['POST'])
def add_member():
    # convierte al dictionary, the JSON request
    request_body = request.get_json()
    #get the new family member data and store in the family list
    jackson_family.add_member(request_body)
    return "Family member added succesfully", 200

@app.route('/member/<int:member_id>', methods=['DELETE'])
def delete_member(member_id):
    # elimina un miembro por el id
    deleted_member = jackson_family.delete_member(member_id)
    if deleted_member:
        return jsonify({"done": True, "deleted_member": deleted_member}), 200
    else:
        return jsonify({"done": False, "error": "Member not found"}), 404

# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)