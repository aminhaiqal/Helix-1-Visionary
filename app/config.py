import os

class Config:
    MONGO_URI = 'mongodb+srv://<username>:<password>@<cluster-url>/<your_database_name>?retryWrites=true&w=majority'
    UPLOAD_FOLDER = 'uploads'
    ALLOWED_EXTENSIONS = {'pdf', 'jpg', 'jpeg', 'png', 'gif', 'bmp'}
    DATABASE_NAME = 'Helix-1-Visionary'
    