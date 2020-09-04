from app import app


@app.route('/')
def home():
	return "I will look at Blueprints, I looked at it for a second"

if __name__ == '__main__':
   app.run(debug=True, host='0.0.0.0')
