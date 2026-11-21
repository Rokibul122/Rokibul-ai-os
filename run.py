from app import create_app

app = create_app()

if name == "main":
app.run(
host=app.config["HOST"],
port=app.config["PORT"],
debug=app.config["DEBUG"]
)
