"""Alternative server startup on port 5001 to avoid conflicts"""
from app import create_app

if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("STARTING FLASK SERVER ON PORT 5001")
    print("=" * 60)
    app = create_app()
    print("\n" + "=" * 60)
    print("SERVER IS NOW RUNNING")
    print("Listening on: http://0.0.0.0:5001")
    print("Test: http://localhost:5001/api/health")
    print("=" * 60 + "\n")
    app.run(host="0.0.0.0", port=5001, debug=True, use_reloader=False)

