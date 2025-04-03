# Use an official Python runtime as a parent image
FROM python:3.9

# Copy the current directory contents into the container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Define the command to run the application
CMD ["python", "main.py"]

# #FROM python:3.8-slim-buster
# FROM public.ecr.aws/sam/build-python3.8:1.121.0-20240730174605
# #WORKDIR /python-docker

# COPY requirements.txt requirements.txt
# RUN pip3 install -r requirements.txt

# COPY . .

# # Set the entrypoint correctly
# ENTRYPOINT python main.py
# #CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]