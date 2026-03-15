from flask import Flask, request, jsonify
from flask_cors import CORS
from search_engine import BarcelonaSearchEngine

app = Flask(__name__)
CORS(app)

search_engine = BarcelonaSearchEngine()

@app.route('/')
def index():
    return jsonify({
        'name': 'Barcelona Search Engine',
        'status': 'running'
    })

@app.route('/search', methods=['GET'])
def search():
    keyword = request.args.get('q', '')
    method = request.args.get('method', 'bfs')
    
    if not keyword:
        return jsonify({'success': False, 'message': 'Keyword tidak boleh kosong'})
    
    use_bfs = method.lower() == 'bfs'


    try:
        result = search_engine.keyword_search(keyword, use_bfs)
        return jsonify(result)
    except Exception as e:
        return jsonify({
            'success': False, 
            'message': f'Terjadi kesalahan: {str(e)}'
        })

@app.route('/locations', methods=['GET'])
def get_locations():
    locations = []
    for loc_id, loc_data in search_engine.locations.items():
        locations.append({
            'id': loc_id,
            'name': loc_data.get('name', ''),
            'category': loc_data.get('category', '')
        })
    return jsonify({'success': True, 'locations': locations})

if __name__ == '__main__':
    print("=" * 50)
    print("BARCELONA SEARCH ENGINE BACKEND")
    print("=" * 50)
    print("Server running di http://localhost:5000")
    print("Coba buka: http://localhost:5000/search?q=barcelona")
    print("=" * 50)
    app.run(debug=True, port=5000)
