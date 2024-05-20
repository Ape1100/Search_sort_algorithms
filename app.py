# Merge sort algorithm for sorting videos by title
def merge_sort_videos(videos):
    if len(videos) <= 1:
        return videos
    
    mid = len(videos) // 2
    left_half = videos[:mid]
    right_half = videos[mid:]
    
    left_half = merge_sort_videos(left_half)
    right_half = merge_sort_videos(right_half)

    return merge(left_half, right_half)

def merge(left_half, right_half):
    result = []
    left_index, right_index = 0, 0
    
    # Compare elements 
    while left_index < len(left_half) and right_index < len(right_half):
        if left_half[left_index]['title'] < right_half[right_index]['title']:
            result.append(left_half[left_index])
            left_index += 1
        else:
            result.append(right_half[right_index])
            right_index += 1
   
    while left_index < len(left_half):
        result.append(left_half[left_index])
        left_index += 1
    
    while right_index < len(right_half):
        result.append(right_half[right_index])
        right_index += 1
    
    return result

# Test
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

sorted_videos = merge_sort_videos(videos)
for video in sorted_videos:
    print(video['title'])
