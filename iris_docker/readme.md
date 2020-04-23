
### 1- Create pipenv 

- Go to your project path
- pipenv install streamlit, pandas, seaborn
- pipenv shell
- cat Pipfile

### 2- Create requirements.txt

- pipenv lock -r > requirements.txt

### 3- Create file with a name "Dockerfile"

- check content as given

### 4- Create Docker Image

- sudo docker build -t irisapp:latest .

- to check if docker image is there 

sudo docker images

