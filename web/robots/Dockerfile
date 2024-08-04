FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the application code to the working directory
COPY . /app

# Install specific versions of Flask and Werkzeug
RUN pip install --no-cache-dir Flask==2.0.3 Werkzeug==2.0.3

# Install other dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port that the application will run on
EXPOSE 5000

# Set environment variables for Flask
ENV FLASK_APP=app.py

# Run the Flask application
CMD ["flask", "run", "--host=0.0.0.0"]
