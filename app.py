# imports...
from flask import Flask

# (E302) make sure there are TWO blank lines before any top-level def/class

def create_app():
    app = Flask(__name__)

    @app.route("/")
    def home():
        return "Hello, CI/CD!"

    return app


# (E305) ensure TWO blank lines after a function/class *before* the next top-level block

if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=5000)
