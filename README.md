# ormae

-- Language: Python

-- Database: MongoDB

-- RateLimit: https://pypi.org/project/ratelimit/

As per my understanding from the problem statement, I had implemented the same by keeping the following major points in mind:

- Fetched the REST API data from: https://jsonplaceholder.typicode.com/comments/
- To match the caps/rate-limit, I had used RateLimit python package.
- For each comment recieved in the response, we check in the DB if comment is already present or not. (**Assuming the "id" to be unique for each comment**)
- If comment is not present, we insert that comment, else wee update all the fields of that comment.
- Added a sleep of 0.1s after each database call to double sure not to hit API call limit.
- I had used Docker to containerize the application

Steps to run:

- The docker command to the ssignment is as follows:
 ```docker run -itd --name ormae kapilbk1996/ormae:assignment1```
