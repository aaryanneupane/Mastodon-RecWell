import networkx as nx
from torch_geometric.utils import from_networkx
import torch

class GraphBuilder:
    def __init__(self, users, posts, interactions, keywordConnections):
        self.users = users
        self.posts = posts
        self.interactions = interactions
        self.keywordConnections = keywordConnections

    def buildGraph(self):
        # Create a graph using networkx
        G = nx.Graph()

        # Add user and post nodes
        for user in self.users:
            G.add_node(user, node_type='user')
        for post in self.posts:
            G.add_node(post, node_type='post')

        # Add user-post interaction edges
        for interaction in self.interactions:
            G.add_edge(interaction['user'], interaction['post'])

        # Add keyword-based post-post edges
        for connection in self.keywordConnections:
            G.add_edge(connection['post1'], connection['post2'])

        # Convert the networkx graph to PyTorch Geometric Data format
        edgeIndex = torch.tensor(list(G.edges), dtype=torch.long).t().contiguous()
        nodeFeatures = torch.randn((len(self.users) + len(self.posts), 16))  # Example node features

        data = from_networkx(G)
        data.x = nodeFeatures
        data.edge_index = edgeIndex

        return data
        