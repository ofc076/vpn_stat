from vpn_flask import app as application

# For debugging; will not run if launched from Nginx
if __name__ == "__main__":
    application.run(port=8081, debug=True, host="0.0.0.0")
