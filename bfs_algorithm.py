from collections import deque
import time

class BFSGraph:
    def __init__(self, locations_data):
        self.graph = {}
        self.locations = locations_data
        self._build_graph()
    
    def _build_graph(self):
        for loc_id, location in self.locations.items():
            self.graph[loc_id] = location.get('neighbors', [])
    
    def bfs_search(self, start_node, target_keyword=None):

        if start_node not in self.graph:
            return {'found': False, 'results': [], 'visited_nodes': [], 'execution_time': 0}
        
        start_time = time.time()
        visited = set()
        queue = deque([(start_node, [start_node], 0)])
        results = []
        
        while queue:
            current_node, path, depth = queue.popleft()

            if current_node not in visited:

                visited.add(current_node)

                location = self.locations.get(current_node, {})

                keyword_match = False

                if not target_keyword:
                    keyword_match = True
                else:
                    keyword = target_keyword.lower()

                    for key, value in location.items():

                        if isinstance(value, str):
                            if keyword in value.lower():
                                keyword_match = True
                                break

                        elif isinstance(value, list):
                            for item in value:
                                if isinstance(item, str) and keyword in item.lower():
                                    keyword_match = True
                                    break

                            if keyword_match:
                                break

                if keyword_match:
                    results.append({
                        'location_id': current_node,
                        'location_data': location,
                        'path': path.copy(),
                        'depth': depth
                    })

                for neighbor in self.graph.get(current_node, []):
                    if neighbor not in visited:
                        new_path = path + [neighbor]
                        queue.append((neighbor, new_path, depth + 1))

        end_time = time.time()

        return {
            'found': len(results) > 0,
            'results': results,
            'total_found': len(results),
            'visited_nodes': list(visited),
            'execution_time': end_time - start_time
        }