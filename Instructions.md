Step 1: User must download Postman Application.

Step 2: User must run NeuroflowMoodAPI.py file with PyCharm.

Step 3: User must login to Postman plus using valid username and password from NeuroflowMoodAPI.py file (as shown below).

<img width="550" alt="goodloginnew" src="https://user-images.githubusercontent.com/94997951/143376658-207b1efb-8547-4d76-a448-231184fc378c.png">

If invalid username or password is used, user must try logging in again (as shown below).

<img width="550" alt="badloginnew" src="https://user-images.githubusercontent.com/94997951/143376674-68bd408d-2e9d-42e5-994e-00bc20071abb.png">

Step 4: User can POST mood in the format shown below (json).

<img width="550" alt="onemoodgoodnew" src="https://user-images.githubusercontent.com/94997951/143376690-a4009157-b79d-4e23-901d-f171260de26a.png">

User cannot POST or GET mood before logging in (as shown below).

<img width="550" alt="notloggedinnew" src="https://user-images.githubusercontent.com/94997951/143376717-da5e4d0b-7084-4b68-8e33-7de40890b3d4.png">

Username must exist in NeuroflowMoodAPI.py file to POST or GET mood, otherwise user cannot POST or GET mood (as shown below).

<img width="550" alt="userDNEnew" src="https://user-images.githubusercontent.com/94997951/143376735-de34b18d-ad2e-407a-ac7a-3602017d0ed0.png">

Step 5: User must POST atleast one time everyday to continue streak (as shown below).

<img width="550" alt="twomoodsgoodnew" src="https://user-images.githubusercontent.com/94997951/143376767-6d8e7cd8-5e4b-4377-839a-32f49d4fc4e7.png">

If User goes one day without a POST, streak will reset to 1 (as shown below).

<img width="550" alt="streakresetnew" src="https://user-images.githubusercontent.com/94997951/143376823-9152a98a-8d28-42fe-a685-84bb2dca676f.png">

Step 6: User can GET POSTed moods by sending GET request (as shown below).

<img width="550" alt="GETnew" src="https://user-images.githubusercontent.com/94997951/143377023-f330ed8d-8dd5-459e-aa84-07d12f0c2860.png">

