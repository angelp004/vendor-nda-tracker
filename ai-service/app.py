from dotenv import load_dotenv
load_dotenv()
from flask import Flask
import routes.describe

app = Flask(__name__)

app.register_blueprint(routes.describe.describe_bp)

print(app.url_map)

@app.route("/")
def home():
    return "AI Service Running"

if __name__ == "__main__":
    app.run(debug=True)