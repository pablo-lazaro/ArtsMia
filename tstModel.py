from model.model import Model

mdl = Model()
mdl.buildGraph()
print(f"Grafo creato, contine {mdl.getNumNodes()} nodi e {mdl.getNumEdges()} archi")

mdl.getInfoCompConnessa(1224)