from app import app

@app.route('/')
def home():
	return "Welcome to this Landing Page"

if __name__ == '__main__':
   app.run(debug=True, host='0.0.0.0')
