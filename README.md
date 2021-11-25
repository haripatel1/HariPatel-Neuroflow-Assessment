For this project, please create a small backend REST API which fulfills the requirements written
below.

Create a public git repo to host your project and submit a link to this repo when you are finished.
Feel free to develop however you normally would. Please use Python, but besides that you can
make use of whatever frameworks and 3rd party libraries you think make sense for this project.
If you have any questions feel free to reach out, but specific direction is up to you.
When you're finished, please send back the link to the git repo with your completed work. Make
sure to include instructions as to how to run and use the application.

Requirements:
Create a web REST application with a '/mood' endpoint, which when POSTed to persists the
submitted mood value.
Add the ability for users to login.
Create a '/mood' endpoint with a GET method, returning all values submitted by the logged-in
user.

Add to the body of the response for the ‘/mood’ endpoint the length of their current "streak".
A user is on a “streak” if that user has submitted at least 1 mood rating for each
consecutive day of that streak.
For example, if on March 1st, March 2nd, March 3rd, and March 5th the user entered
mood ratings, a 3-day streak will apply to the March 3rd rating and the streak will reset to
a 1-day streak for the March 5th rating.
