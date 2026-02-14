from flask import Flask, request, jsonify
from flask_cors import CORS
from inference import semantic_search
from roadmap import build_roadmap
from fishbone_roadmap import build_fishbone_roadmap
import traceback


def create_app() -> Flask:
    app = Flask(__name__)
    # Configure CORS to allow all origins for development
    CORS(app, resources={r"/*": {"origins": "*", "methods": ["GET", "POST", "OPTIONS"], "allow_headers": ["Content-Type"]}})
    
    # Debug: Print when app is created
    print("=" * 60)
    print("Creating Flask app...")
    print("=" * 60)
    
    @app.route("/", methods=["GET"])
    def root() -> tuple:
        """Root endpoint - shows API info or fishbone data if query provided"""
        query = request.args.get("q", type=str, default=None)
        
        # If query parameter is provided, return fishbone data
        if query:
            top_k = request.args.get("k", type=int, default=25)
            try:
                results = semantic_search(query=query, top_k=top_k)
                if not results:
                    return jsonify({
                        "query": query,
                        "articles": [],
                        "videos": [],
                        "total_articles": 0,
                        "total_videos": 0
                    }), 200
                fishbone = build_fishbone_roadmap(query=query, results=results)
                return jsonify(fishbone), 200
            except Exception as e:
                traceback.print_exc()
                return jsonify({"error": str(e), "type": type(e).__name__}), 500
        
        # Otherwise, return API info
        return jsonify({
            "message": "Learnora Backend API",
            "version": "2.0",
            "endpoints": {
                "health": "/api/health",
                "search": "/api/search",
                "roadmap": "/api/roadmap",
                "fishbone": "/api/fishbone"
            },
            "usage": {
                "api_info": "GET /",
                "fishbone_data": "GET /?q=your_query&k=25"
            }
        }), 200
    
    @app.route("/api/health", methods=["GET"])
    def health() -> tuple:
        print("HEALTH ENDPOINT CALLED!")
        return jsonify({"status": "ok", "server": "learnora_backend_v2"}), 200
    
    @app.route("/test_server", methods=["GET"])
    def test_server() -> tuple:
        print("TEST_SERVER ENDPOINT CALLED!")
        return jsonify({
            "message": "This is the Learnora backend server",
            "version": "2.0",
            "routes": [str(r.rule) for r in app.url_map.iter_rules() if not str(r.rule).startswith('/static')]
        }), 200

    @app.route("/api/search", methods=["GET"])
    def search_endpoint() -> tuple:
        try:
            query = request.args.get("q", type=str, default=None)
            top_k = request.args.get("k", type=int, default=10)
            if not query:
                return jsonify({"error": "Missing required query param 'q'"}), 400
            results = semantic_search(query=query, top_k=top_k)
            return jsonify({"query": query, "results": results}), 200
        except Exception as e:
            traceback.print_exc()
            return jsonify({"error": str(e)}), 500

    @app.route("/api/roadmap", methods=["GET"])
    def roadmap_endpoint() -> tuple:
        try:
            query = request.args.get("q", type=str, default=None)
            top_k = request.args.get("k", type=int, default=25)
            max_steps = request.args.get("steps", type=int, default=5)
            if not query:
                return jsonify({"error": "Missing required query param 'q'"}), 400
            
            # Perform semantic search
            results = semantic_search(query=query, top_k=top_k)
            
            # Check if we got results
            if not results:
                return jsonify({
                    "query": query,
                    "steps": [],
                    "message": "No results found for your query"
                }), 200
            
            # Build roadmap
            roadmap = build_roadmap(query=query, results=results, max_steps=max_steps)
            
            return jsonify({"query": query, "steps": roadmap}), 200
        except Exception as e:
            traceback.print_exc()
            return jsonify({"error": str(e), "type": type(e).__name__}), 500

    @app.route("/api/fishbone", methods=["GET", "OPTIONS"])
    def fishbone_endpoint() -> tuple:
        if request.method == "OPTIONS":
            # Handle CORS preflight
            response = jsonify({})
            response.headers.add("Access-Control-Allow-Origin", "*")
            response.headers.add("Access-Control-Allow-Headers", "Content-Type")
            response.headers.add("Access-Control-Allow-Methods", "GET, OPTIONS")
            return response, 200
        
        print("=" * 60)
        print("FISHBONE ENDPOINT CALLED!")
        print(f"Query: {request.args.get('q')}")
        print(f"Full URL: {request.url}")
        print(f"Headers: {dict(request.headers)}")
        print("=" * 60)
        try:
            query = request.args.get("q", type=str, default=None)
            top_k = request.args.get("k", type=int, default=25)
            if not query:
                return jsonify({"error": "Missing required query param 'q'"}), 400
            
            # Perform semantic search
            results = semantic_search(query=query, top_k=top_k)
            
            # Check if we got results
            if not results:
                return jsonify({
                    "query": query,
                    "articles": [],
                    "videos": [],
                    "total_articles": 0,
                    "total_videos": 0
                }), 200
            
            # Build fishbone roadmap
            fishbone = build_fishbone_roadmap(query=query, results=results)
            return jsonify(fishbone), 200
        except Exception as e:
            traceback.print_exc()
            return jsonify({"error": str(e), "type": type(e).__name__}), 500

    # Debug: Print all registered routes
    print("\nRegistered routes:")
    routes_list = []
    for rule in app.url_map.iter_rules():
        if not rule.rule.startswith('/static'):
            print(f"  {rule.rule:30s} -> {rule.endpoint}")
            routes_list.append(rule.rule)
    print("=" * 60)
    print(f"Total routes: {len(routes_list)}")
    print("=" * 60 + "\n")
    
    # Add a catch-all route to see what's being requested
    @app.before_request
    def log_every_request():
        print(f"\n{'='*60}")
        print(f">>> INCOMING REQUEST: {request.method} {request.path}")
        print(f"    Full URL: {request.url}")
        print(f"    Endpoint: {request.endpoint}")
        print(f"{'='*60}")
    
    # Add 404 error handler to debug route issues
    @app.errorhandler(404)
    def handle_404(e):
        # Ignore favicon and other browser resource requests
        if request.path in ['/favicon.ico', '/robots.txt', '/manifest.json']:
            return '', 204  # No content
        
        print(f"\n{'!'*60}")
        print(f"404 ERROR - Route not found!")
        print(f"  Requested path: {request.path}")
        print(f"  Method: {request.method}")
        print(f"  Full URL: {request.url}")
        print(f"  Available routes in app:")
        for rule in app.url_map.iter_rules():
            if not rule.rule.startswith('/static'):
                print(f"    {rule.rule:30s} ({', '.join(rule.methods)})")
        print(f"{'!'*60}\n")
        return jsonify({
            "error": "Route not found",
            "requested_path": request.path,
            "method": request.method,
            "available_routes": [str(r.rule) for r in app.url_map.iter_rules() if not str(r.rule).startswith('/static')]
        }), 404
    
    return app


if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("STARTING FLASK SERVER")
    print("=" * 60)
    app = create_app()
    print("\n" + "=" * 60)
    print("SERVER IS NOW RUNNING")
    print("Listening on: http://0.0.0.0:5001")
    print("Test: http://localhost:5001/api/health")
    print("=" * 60 + "\n")
    # Run without reloader to avoid issues with route registration
    app.run(host="0.0.0.0", port=5001, debug=True, use_reloader=False)



