from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

# Define the videos list
videos = [
    {'id': 1, 'title': 'The Art of Coding', 'duration': 32},
    {'id': 2, 'title': 'Exploring the Cosmos', 'duration': 44},
    {'id': 3, 'title': 'Cooking Masterclass: Italian Cuisine', 'duration': 76},
    {'id': 4, 'title': 'History Uncovered: Ancient Civilizations', 'duration': 77},
    {'id': 5, 'title': 'Fitness Fundamentals: Strength Training', 'duration': 59},
    {'id': 6, 'title': 'Digital Photography Essentials', 'duration': 45},
    {'id': 7, 'title': 'Financial Planning for Beginners', 'duration': 40},
    {'id': 8, 'title': "Nature's Wonders: National Geographic", 'duration': 45},
    {'id': 9, 'title': 'Artificial Intelligence Revolution', 'duration': 87},
    {'id': 10, 'title': 'Travel Diaries: Discovering Europe', 'duration': 78}
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['GET'])
def search_videos():
    query = request.args.get('query')
    if not query:
        return jsonify({'error': 'Query parameter is required'}), 400
    
    # Perform binary search
    result = binary_search_videos(videos, query)
    
    return jsonify({'videos': result})

# Binary search algorithm for searching videos by title
def binary_search_videos(videos, query):
    left = 0
    right = len(videos) - 1
    
    while left <= right:
        mid = (left + right) // 2
        mid_title = videos[mid]['title']
        
        if mid_title == query:
            return [videos[mid]]
        elif mid_title < query:
            left = mid + 1
        else:
            right = mid - 1
    
    return []

# Ignore favicon.ico request errors
@app.route('/favicon.ico')
def favicon():
    return jsonify({'message': 'favicon.ico not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)

