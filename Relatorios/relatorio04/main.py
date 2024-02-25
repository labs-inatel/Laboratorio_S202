from database import Database
from save_json import writeAJson

db = Database(database="loja_de_roupas", collection="vendas")
# db.resetDatabase()

class ProductAnalyzer:

    # Customer B's total spend:
    def totalB(self):
        result = db.collection.aggregate([
            {"$unwind": "$produtos"},
            {"$match": {"cliente_id": "B"}},
            {"$group": {"_id": "$cliente_id",
                        "total": {"$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}}},
            {"$group": {"_id": 2, "total": {"$avg": "$total"}}}
        ])
        writeAJson(result, "totalB")
        pass

    # Least sold product:
    def menos_vendido(self):
        result = db.collection.aggregate([
            {"$unwind": "$produtos"},
            {"$group": {"_id": "$produtos.nome", "total": {"$sum": "$produtos.quantidade"}}},
            {"$sort": {"total": 1}},
            {"$limit": 1}
        ])
        writeAJson(result, "menos_vendido")
        pass

    # Customer who spent less on purchases:
    def menor_comprador(self):
        result = db.collection.aggregate([
            {"$unwind": "$produtos"},
            {"$group": {"_id": {"cliente": "$cliente_id", "data": "$data_compra"},
                        "total": {"$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}}},
            {"$sort": {"_id.data": 1, "total": 1}},
            {"$group": {"_id": "$_id.data", "cliente": {"$first": "$_id.cliente"}, "total": {"$first": "$total"}}}
        ])
        writeAJson(result, "menor_comprador")
        pass

    # Products sold with the quantity of two or more units:
    def lista_produto(self):
        result = db.collection.aggregate([
            {"$unwind": "$produtos"},
            {"$match": {"produtos.quantidade": {"$gt": 2}}},
            {"$group": {"_id": "$produtos.nome", "total": {"$sum": "$produtos.quantidade"}}},
            {"$sort": {"total": -1}},
        ])
        writeAJson(result, "lista_produto")
        pass

# Calling the functions:
ProductAnalyzer.totalB(db.collection)
ProductAnalyzer.menos_vendido(db.collection)
ProductAnalyzer.menor_comprador(db.collection)
ProductAnalyzer.lista_produto(db.collection)

