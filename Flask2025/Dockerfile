# Use a slim Python base image for a smaller image size
FROM python:3.13.4

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire application code into the container
COPY . .

# Expose the port on which the Flask application will run (default is 5000)
EXPOSE 5000

# Command to run the Flask application using Gunicorn (recommended for production)
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app:app"]