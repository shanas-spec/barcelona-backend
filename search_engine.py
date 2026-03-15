from barcelona_data import get_all_locations, search_by_keyword, get_location
from bfs_algorithm import BFSGraph
import time

class BarcelonaSearchEngine:
    def __init__(self):
        self.locations = get_all_locations()
        self.bfs_graph = BFSGraph(self.locations)
    
    def keyword_search(self, keyword, use_bfs=True, start_node='gracia'):
        start_time = time.time()
        
        if use_bfs:
            bfs_result = self.bfs_graph.bfs_search(start_node, keyword)
            results = []
            for result in bfs_result.get('results', []):
                loc_data = result['location_data']
                results.append({
                    'id': result['location_id'],
                    'name': loc_data.get('name', ''),
                    'category': loc_data.get('category', ''),
                    'description': loc_data.get('description', ''),
                    'depth': result['depth']
                })
            
            return {
                'success': True,
                'keyword': keyword,
                'total_results': len(results),
                'results': results,
                'metadata': {
                    'method': 'BFS',
                    'execution_time': bfs_result['execution_time'],
                    'visited_nodes': len(bfs_result['visited_nodes'])
                }
            }
        else:
            location_ids = search_by_keyword(keyword)
            results = []
            for loc_id in location_ids:
                loc_data = get_location(loc_id)
                if loc_data:
                    results.append({
                        'id': loc_id,
                        'name': loc_data.get('name', ''),
                        'category': loc_data.get('category', ''),
                        'description': loc_data.get('description', '')
                    })
            
            return {
                'success': True,
                'keyword': keyword,
                'total_results': len(results),
                'results': results,
                'metadata': {
                    'method': 'Direct Index',
                    'execution_time': time.time() - start_time
                }
            }
