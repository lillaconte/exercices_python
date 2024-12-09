from app.app import app, version

if __name__ == "__main__":
    print(f"Version:{version}")
    app.run()