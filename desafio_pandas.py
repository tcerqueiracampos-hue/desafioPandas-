import pandas as pd

produtos = {
    "nome": ["Notebook", "Mouse", "Celular", "Livro", "Teclado"],
    "preco": [2500, 120, 3200, 23, 150],
    "categoria": [
        "informatica",
        "informatica",
        "eletronicos",
        "papelaria",
        "informatica"
    ]
}

df = pd.DataFrame(produtos)
#Mostre apenas os produtos com preço maior que R$ 100.

print("\n[ PRODUTOS ACIMA DE R$ 100 ]")
print(df[df["preco"] > 100].to_string(index=False))

# Mostre apenas os produtos da categoria informatica

print("\n[ PRODUTOS DE INFORMÁTICA ]")
print(df[df["categoria"] == "informatica"].to_string(index=False))

# calcule a média dos preços dos produtos.

def calcular_total(produtos):
    return sum(produtos["preco"])

def calcular_media(produtos):
    total = calcular_total(produtos)
    return total / len(produtos["preco"])

print(calcular_media(produtos))

# Agrupe os produtos por categoria.
#Calcule a soma dos preços de cada categoria.
# Descubra qual categoria possui o maior valor total

print(
    df.groupby("categoria")["preco"].sum()
)

totais = df.groupby("categoria")["preco"].sum()

maior_categoria = totais.idxmax()

print("Categoria com maior valor:", maior_categoria)