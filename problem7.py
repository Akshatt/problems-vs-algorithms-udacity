from collections import defaultdict

class RouteTrieNode:
    def __init__(self, handler=None):
        self.children = defaultdict(RouteTrieNode)
        self.handler = handler
        
class RouteTrie:
    def __init__(self, root_handler):
        self.root = RouteTrieNode(root_handler)

        
    def insert(self, path, handler):
        path_seg = path.split('/')
        node = self.root
        for seg in path_seg:
            if seg != '':
                node = node.children[seg]
                
        node.handler = handler

        
    def find(self, path):
        path_seg = path.split('/')
        node = self.root
        for seg in path_seg:
            if seg != '':
                node = node.children[seg]
        return node.handler   
    
        
class Router:
    def __init__(self, root_handler):
        self.route_trie = RouteTrie(root_handler)
        
    def add_handler(self, path, handler):
        self.route_trie.insert(path, handler)

    def lookup(self, path):
        return self.route_trie.find(path)


# create the router and add a route
router = Router("root handler")  # remove the 'not found handler' if you did not implement this
router.add_handler("/home", "home handler")  # add a route
router.add_handler("/home/about", "about handler")  # add a route
router.add_handler("/home/about/me/you", "you handler")  # add a route


# some lookups with the expected output
print(router.lookup("/")) # should print 'root handler'
print(router.lookup("/home")) # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about")) # should print 'about handler'
print(router.lookup("/home/about/")) # should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/me")) # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about/me/you"))
