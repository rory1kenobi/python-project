from flask import Flask, render_template
from controllers.country_controller import country_blueprint
# from controllers.sight_controller import sight_blueprint
# from controllers.visit_controller import visit_blueprint
from controllers.bucket_list_controller import bucket_list_blueprint

app = Flask(__name__)

app.register_blueprint(country_blueprint)
# app.register_blueprint(sight_blueprint)
# app.register_blueprint(visit_blueprint)
app.register_blueprint(bucket_list_blueprint)


@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)