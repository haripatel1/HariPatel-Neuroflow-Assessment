Step 1: User must download Postman Application.

Step 2: User must run NeuroflowMoodAPI.py file with PyCharm.

Step 3: User must login to Postman plus using valid username and password from NeuroflowMoodAPI.py file (as shown below).

<img width="550" alt="goodlogin" src="https://user-images.githubusercontent.com/94997951/143364894-4737dc40-8393-4244-8595-87f03a70695d.png">

If invalid username or password is used, user must try logging in again (as shown below).

<img width="550" alt="badlogin" src="https://user-images.githubusercontent.com/94997951/143365048-b53acb6f-773c-484b-ba83-9c94619dfe53.png">

Step 4: User can POST mood in the format shown below.

<img width="550" alt="onemoodgood" src="https://user-images.githubusercontent.com/94997951/143365208-d09094c1-bdbf-46e2-8bf4-c6eec773ea7b.png">

User cannot POST or GET mood before logging in (as shown below).

<img width="550" alt="notloggedin" src="https://user-images.githubusercontent.com/94997951/143365342-825700c5-b833-4766-81b2-9a78f0ab34fa.png">

Username must exist in NeuroflowMoodAPI.py file to POST or GET mood, otherwise user cannot POST or GET mood (as shown below).

<img width="550" alt="userDNE" src="https://user-images.githubusercontent.com/94997951/143365488-81354643-662c-43c0-9639-d16f0043262f.png">

Step 5: User must POST atleast one time everyday to continue streak (as shown below).

<img width="550" alt="twomoodsonedaygood" src="https://user-images.githubusercontent.com/94997951/143365657-1afe3ef0-81dc-4309-9b3e-bdfb6ea5f1a4.png">

If User goes one day without a POST, streak will reset to 1 (as shown below).

<img width="550" alt="streakreset" src="https://user-images.githubusercontent.com/94997951/143365731-ae155ebf-0e68-43ca-b26b-3826080a2b08.png">

Step 6: User can GET POSTed moods by sending GET request (as shown below).

<img width="550" alt="getmoodsandstreak" src="https://user-images.githubusercontent.com/94997951/143365852-dc626fe6-f2e7-483a-8c7d-9877af6d562d.png">


