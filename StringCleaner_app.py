# StringCleaner.py
# Author: K. Nicole Thompson
#
# This is a microservice for Emi's "Note-ify" note taking app.
# By using a combination of microservices, the app allows the user to 
# create a note, edit, delete, search, and analyze notes. The app also 
# allows the user to add tags to notes.
#
# This microservice is the string cleaner, given a string that 
# represents the category or tag, it cleans the string.
# The string cleaner returns a list if there are words in the string, 
# or the empty string. The input is a string of words separated by 
# commas. The string can also be the empty string or just one word.
# Example inputs:
# "Cream",
# "Creams, life, favourite",
# "Creams", 
# ""
from flask import Flask, request, jsonify
app = Flask(__name__)

def string_cleaner(string):
    """
    Cleans a string of words separated by commas, removes whitespace,
    and returns a list of cleaned words.
    """
    if not string:
        return []
    words = [word.strip() for word in string.split(",")]
    return [word for word in words if word]

@app.route("/clean", methods=["POST"])
def clean_string():
    if not request.is_json:
        return jsonify({"error": "Request must be JSON"}), 415

    data = request.get_json()
    if "string" not in data:
        return jsonify({"error": "Missing 'string' field in JSON"}), 400

    input_string = data["string"]
    cleaned = string_cleaner(input_string)
    return jsonify({"cleaned": cleaned})

if __name__ == "__main__":
    app.run(debug=True)