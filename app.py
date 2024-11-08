from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/calculator', methods=['POST'])
def calculator():
    num1 = float(request.form['num1'])
    num2 = float(request.form['num2'])
    operation = request.form['operation']

    if operation == "add":
        answer = num1 + num2
    elif operation == "subtract" :
        answer = num1 - num2
    elif operation == "mul":
        answer = num1 * num2
    elif operation == "div" :
        if num2 == 0:
            answer = "invalid input! Cannot divide by zero"
        else:
            answer = num1 / num2
    else:
        answer = "invalid input!"

    return jsonify({"answer" : answer})    

if __name__ == '__main__':
    app.run()