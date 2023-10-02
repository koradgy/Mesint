GRAPH= {
    "S": ["A", "B"],
    "A": ["S", "B", "D"],
    "B": ["A", "C", "S"],
    "C": ["B", "E"],
    "D": ["A", "G"],
    "E": ["C"]
}


def bfs(graph, start, goal):

    """Breath first search"""
    #init queue

    queue=[]

    queue.append([start])
    while  queue:
        #take first element
        path=queue.pop(0)
        end_node=path[-1]
        if end_node==goal:
            return path
        for adjacent in graph.get(end_node, []):
            if adjacent not in path:
                new_path=list(path)+[adjacent]
                queue.append( new_path)
    return None

print(bfs(GRAPH, "S", "G"))