from dotenv import load_dotenv
load_dotenv()
import routes.generate_report

from flask import Flask
import routes.describe
import routes.recommend
import routes.generate_report
import routes.health


app = Flask(__name__)

app.register_blueprint(routes.describe.describe_bp)

app.register_blueprint(routes.recommend.recommend_bp)
app.register_blueprint(routes.generate_report.report_bp)
app.register_blueprint(routes.health.health_bp)

print(app.url_map)

@app.route("/")
def home():
    return "AI Service Running"

if __name__ == "__main__":
    app.run(debug=True)