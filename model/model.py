import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._graph = nx.Graph()
        self._nodes = DAO.getAllNodes()
        self._idMapAO = {}
        for n in self._nodes:
            self._idMapAO[n.object_id] = n

    def buildGraph(self):
        # Aggiunge i nodi (li recupero dal database)

        self._graph.add_nodes_from(self._nodes)

        # Aggiunge gli archi (li recupero dal database)
        self.addEdges2()

    def getInfoCompConnessa(self, id_oggetto):

        # cercare la componente connessa che contiene id_oggetto
        if not self.hasNode(id_oggetto):
            return None

        source = self._idMapAO[id_oggetto]

        dfsTree = nx.dfs_tree(self._graph, source)
        print("size connessa con dfs_tree", len(dfsTree.nodes()))

        # Strategia 2

        dfsPred = nx.dfs_predecessors(self._graph, source)
        print("size connessa con dfs_Pred", len(dfsPred.values()))

        # Strategia 3 --> implementeremo sempre questa
        conn = nx.node_connected_component(self._graph, source)
        print("size connessa con connected component", len(conn))

        return len(conn)




    def hasNode(self, id_oggetto):
        return id_oggetto in self._idMapAO

    def addEdges(self):
        for u in self._nodes:
            for v in self._nodes:
                peso = DAO.getEdgePeso(u, v)
                if peso is not None:
                    self._graph.add_edge(u, v, weight=peso)
                    print(f"Aggiunto arco fra {u} e {v} con peso {peso}")

    def addEdges2(self):
        allEdges = DAO.getAllEdges(self._idMapAO)
        for e in allEdges:
            self._graph.add_edge(e.o1, e.o2, weight=e.weight)

    # Metodi di controllo
    def getNumNodes(self):
        return len(self._graph.nodes)

    def getNumEdges(self):
        return len(self._graph.edges)




