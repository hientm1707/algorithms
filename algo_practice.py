from typing import Union 
from collections import defaultdict

def print_func_name(func):
    def wrapper(*args, **kwargs):
        print(f'Printing result of function =={func.__name__}== with params: {args}')
        print('Result: \n')
        return func(*args, **kwargs)
    return wrapper


graph_input = defaultdict(chr)
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

graph_topo = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}
# A -> B -> D -> E -> F -> C

@print_func_name
def dfs_recursive(graph:dict, start_node):
    res = []
    visited = set()
    def dfs_util(graph, next_node, visited):
        visited.add(next_node)
        res.append(next_node)
        for dep in graph[next_node]:
            if dep not in visited:
                dfs_util(graph, next_node=dep, visited=visited)
    dfs_util(graph=graph, next_node=start_node, visited=visited)
    print(res)
    return res

@print_func_name
def topological_sort(graph: dict):  #topo sort dont use start node, have to traverse all keys
    def topo_util(node, stack, visited):
        visited.add(node)
        for adj in graph[node]:
            if adj not in visited:
                topo_util(node=adj, stack=stack, visited=visited)
        stack.append(node) ## Mark This line

    visited = set()
    stack = []

    for key in graph.keys():
        if key not in visited:
            topo_util(node=key, stack=stack, visited=visited)    

    res = stack[::-1]
    print(res)
    return res

@print_func_name
def dfs_stack(graph:dict, start_node):
    visited = set()
    res = []
    stack = [start_node]
    while stack:
        top = stack.pop()
        if top not in visited:
            visited.add(top)
            res.append(top)
        for neighbor in graph[top]:
            if neighbor not in visited:     
                stack.append(neighbor)
                #Note là not visited mới append vào stack or queue, và append vào result
    print(res)
    return res


    #     if top not in visited:
    #         visited.add(top)
    #         res.append(top)
    #     for adj in graph[top]:
    #         if adj not in visited:
    #             dfs_util(graph, start_node=adj, stack=stack, visited=visited)
    # print(res)
    # return res 


@print_func_name
def bfs(graph:dict, start_node: Union[int, str]):
    queue = [start_node]
    visited = set()
    res = []
    while queue:
        front = queue.pop(0)
        if front not in visited:
            res.append(front)
            visited.add(front)
            for neighbor in graph[front]:
                if neighbor not in visited:
                    queue.append(neighbor)

    print(res)
    return res
# test

# dfs_recursive(graph, start_node='A')
# dfs_stack(graph, start_node='A')
topological_sort(graph_topo)
# bfs(graph, start_node='A')