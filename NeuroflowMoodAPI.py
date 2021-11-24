# import modules
import datetime
from flask import Flask, request

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
                        return "Please enter mood."
                    i['moods'].append(mood)
                    currtime = datetime.datetime.now().day
                    i['timestamp'].append(currtime)
                    return 'moods:' + str(i['moods']) + '   streak:' + str(streak(i['moods']))
                else:
                    return 'moods:' + str(i['moods']) + '   streak:' + str(streak(i['moods']))
            else:
                return "User not logged in."

    for i in userlist['users']:
        if nameInput not in i['username']:
            return "User does not exist."


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
            response.append({'Login successful.'})
        else:
            response.append({"Wrong username or password."})

    for message in response:
        if "Login successful." in str(message):
            return str(message)

    for message in response:
        if "Login successful." not in str(message):
            return str(message)

if __name__ == '__main__':
    app.run()
