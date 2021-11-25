# import modules
import datetime
from flask import Flask, jsonify, request

# instantiates Flask class
app = Flask(__name__)

# dictionary that stores valid usernames and passwords, login statuses, and timestamps(days)
userlist = {
    "users": [{"username": "hari", "password": "patel", "moods": [], 'loginStatus': False, 'timestamp': []},
               {"username": "neuroflow", "password": "assessment", "moods": [], 'loginStatus': False, 'timestamp': []},
               {"username": "newuser", "password": "newpasswd", "moods": [], 'loginStatus': False, 'timestamp': []}]

}

# function to calculate current streak; i.e. days in a row that mood was posted
def streak(moods):
    i = len(moods) - 1
    streak = 1
    if i >= 1:
        for j in userlist['users']:
            if nameInput == j['username']:
                if len(j['timestamp']) >= 2:
                    for n in range(1, (len(j['timestamp']))):
                        first = j['timestamp'][n-1]
                        second = j['timestamp'][n]

                        if (first + 1) == second:
                            streak += 1
                        elif (second - first) > 1:
                            streak = 1
                        else:
                            continue
    return streak


# login endpoint; allows users to post username and password
@app.route('/login', methods=['POST'])
def login():
    userInput = request.get_json()
    nameInput = userInput['username']
    passwdInput = userInput['password']
    response = []
    for i in userlist['users']:
        if nameInput == i['username'] and i['password'] == passwdInput:
            i['loginStatus'] = True
            response.append({'Login successful.'}), 200
        else:
            response.append({"Wrong username or password."}), 403

    for message in response:
        if "Login successful." in str(message):
            return jsonify({'success': str(message)})

    for message in response:
        if "Login successful." not in str(message):
            return jsonify({'notice': str(message)})


# mood endpoint; allows users to post mood
@app.route('/mood', methods=['GET', 'POST'])
def mood():
    userInput = request.get_json()
    global nameInput
    nameInput = userInput['username']

    for i in userlist['users']:
        if nameInput == i['username']:
            if i['loginStatus'] == True:
                if request.method == 'POST':
                    mood = userInput['mood']
                    if len(mood) == 0 or mood.isspace():
                        return jsonify({'notice': "Please enter mood."})
                    i['moods'].append(mood)
                    currtime = datetime.datetime.now().minute
                    i['timestamp'].append(currtime)
                    return jsonify({'moods': str(i['moods']), 'streak': str(streak(i['moods']))}), 201
                else:
                    return jsonify({'moods': str(i['moods']), 'streak': str(streak(i['moods']))}), 201
            else:
                return jsonify({'notice':"User not logged in."}), 403

    for i in userlist['users']:
        if nameInput not in i['username']:
            return jsonify({'notice': "User does not exist."}), 404



if __name__ == '__main__':
    app.run()
