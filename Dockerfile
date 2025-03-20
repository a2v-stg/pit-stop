# Using the official Python 3.9 image
FROM python:3.9


# Set the working directory
WORKDIR /app

# Creating static directory 
RUN mkdir -p /app/static

# Copying requirements and install dependencies
COPY requirements.txt .

RUN pip install pyap
RUN pip install numpy==1.26.4
RUN pip install -r requirements.txt
RUN pip uninstall -y keras 
RUN pip install tf-keras
RUN python -m spacy download en_core_web_sm

# Copying the application code
COPY . .

# Exposing the application port
EXPOSE 8082

# Run the application
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]

