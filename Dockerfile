# Install Python 3
FROM python:3

# Include the following files in the app
COPY entrypoint.py /

# Install some needed python libraries used in 'entrypoint.py'
RUN pip install sh

# Make the app available at port 3306 of your computer
EXPOSE 3306

# Execute the terminal command 'python entrypoint.py' which uses python to start running the file 'entrypoint.py'
ENTRYPOINT "python" "entrypoint.py"
