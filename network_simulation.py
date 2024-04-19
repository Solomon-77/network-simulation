import networkx as nx
import matplotlib.pyplot as plt

def create_centralized_network(n):
    return nx.star_graph(n)

def create_decentralized_network(n):
    return nx.erdos_renyi_graph(n, 0.5)

# Uses Breadth-First Search(BFS) Algorithm
def simulate_info_distribution(G, start_node):
    visited = [start_node]
    queue = [start_node]

    while queue:
        node = queue.pop(0)
        neighbors = G.neighbors(node)
        queue.extend(neighbor for neighbor in neighbors if neighbor not in visited)
        visited.extend(neighbor for neighbor in neighbors if neighbor not in visited)

    return visited

def plot_networks(centralized_network, decentralized_network):
    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)
    nx.draw(centralized_network, with_labels=True)
    plt.title("Centralized Network")
    plt.subplot(1, 2, 2)
    nx.draw(decentralized_network, with_labels=True)
    plt.title("Decentralized Network")
    plt.show()

def main():
    n = 30 # No. of nodes to simulate
    centralized_network = create_centralized_network(n)
    decentralized_network = create_decentralized_network(n)

    plot_networks(centralized_network, decentralized_network)

if __name__ == "__main__":
    main()