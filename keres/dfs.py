GRAPH= {
    "S": ["A", "B"],
    "A": ["S", "B", "D"],
    "B": ["A", "C", "S"],
    "C": ["B", "E"],
    "D": ["A", "G"],
    "E": ["C"]
}


def dfs(graph, start, goal):

    """Depth first search"""
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
                queue.insert(0, new_path)
    return None




print(dfs(GRAPH, "S", "G"))