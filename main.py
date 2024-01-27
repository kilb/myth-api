from app import create_app

app = create_app("/var/mythapi/tsniffer/data")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, workers=8, dev=True)