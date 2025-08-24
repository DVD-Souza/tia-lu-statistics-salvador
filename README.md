# 📊 Tia Lu Delivery: Biblioteca de Estatística

Este repositório é parte do projeto **Tia Lu Delivery**, um novo aplicativo da empresa FoodDelivery. O objetivo é desenvolver uma biblioteca de estatística essencial para a área de dados.

A classe `Statistics` é a peça central deste projeto. Ela foi projetada para realizar uma variedade de cálculos estatísticos sobre conjuntos de dados, tornando a análise mais rápida e eficiente.

## 🚀 Como Usar

A classe `Statistics` opera sobre um dicionário que simula um conjunto de dados, onde as chaves são os nomes das colunas e os valores são listas de dados.

### Exemplo

Para começar, importe a classe e crie uma instância com seu conjunto de dados.

```python
dataset = {
    'pedidos': [10, 20, 15, 25, 30, 20],
    'precos': [5.5, 12.0, 8.0, 15.0, 20.0, 12.0]
}

stats = Statistics(dataset)

# Calcula a média da coluna 'pedidos'
media_pedidos = stats.mean('pedidos')
print(f"Média de pedidos: {media_pedidos}")

# Calcula a mediana da coluna 'precos'
mediana_precos = stats.median('precos')
print(f"Mediana dos preços: {mediana_precos}")
