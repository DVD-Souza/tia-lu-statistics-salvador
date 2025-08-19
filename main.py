class Statistics:
    def __init__(self, dataset):
        if not isinstance(dataset, dict):
            raise TypeError("O dataset deve ser um dicionário, onde cada chave é uma coluna e o valor é uma lista.")
        tamanhos = [len(val) for val in dataset.values()]
        if len(set(tamanhos)) != 1:
            raise ValueError("Todas as colunas devem ter o mesmo número de elementos.")
        for coluna, valores in dataset.items():
            if not valores:
                raise ValueError(f"A coluna '{coluna}' está vazia.")
            tipo = type(valores[0])
            if not all(isinstance(v, tipo) for v in valores):
                raise TypeError(f"A coluna '{coluna}' deve ter todos os elementos do mesmo tipo.")
        self.dataset = dataset

    def colunas(self):
        return list(self.dataset.keys())

    def linhas(self):
        return len(next(iter(self.dataset.values())))

    def media(self, coluna):
        """Calcula a média de uma coluna numérica"""
        if coluna not in self.dataset:
            raise KeyError(f"A coluna '{coluna}' não existe no dataset.")
        
        valores = self.dataset[coluna]
        
        # Verifica se são números
        if not all(isinstance(v, (int, float)) for v in valores):
            raise TypeError(f"A coluna '{coluna}' não é numérica, não é possível calcular a média.")
        
        return sum(valores) / len(valores)

    def calcular_frequencia_absoluta(self, coluna):
        """Calcula a frequência absoluta de cada valor em uma coluna"""
        if coluna not in self.dataset:
            raise KeyError(f"A coluna '{coluna}' não existe no dataset.")
        
        valores = self.dataset[coluna]
        frequencia = {}
        
        for valor in valores:
            if valor in frequencia:
                frequencia[valor] += 1
            else:
                frequencia[valor] = 1
        
        return frequencia
        

    def calcular_frequência_acumulada(self, coluna):
        """Calcula a frequência acumulada de cada valor em uma coluna"""
        frequencia_absoluta = self.calcular_frequencia_absoluta(coluna)
        valores_ordenados = sorted(frequencia_absoluta.keys())
        
        frequencia_acumulada = {}
        acumulado = 0
        
        for valor in valores_ordenados:
            acumulado += frequencia_absoluta[valor]
            frequencia_acumulada[valor] = acumulado
        
        return frequencia_acumulada
