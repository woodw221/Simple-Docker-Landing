from app import app

@app.route('/')
def home():
	return "Welcome to this Landing Page"
