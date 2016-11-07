from flask import Flask
import views.home_page
import views.integrations_page


app = Flask(__name__)
app.register_blueprint(views.home_page.page)
app.register_blueprint(views.integrations_page.page)


if __name__ == "__main__":
    app.run(debug=True)