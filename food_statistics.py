class Statistics:
    """
    Uma classe para realizar cálculos estatísticos em um conjunto de dados.

    Atributos
    ----------
    dataset : dict[str, list]
        O conjunto de dados, estruturado como um dicionário onde as chaves
        são os nomes das colunas e os valores são listas com os dados.
    """
    def __init__(self, dataset):
        """
        Inicializa o objeto Statistics.

        Parâmetros
        ----------
        dataset : dict[str, list]
            O conjunto de dados, onde as chaves representam os nomes das
            colunas e os valores são as listas de dados correspondentes.
        """
        
        # validação do dataset como dicionário 
        if not isinstance(dataset, dict):
            raise TypeError("O dataset deve ser um dicionário.")
    
        # nesse caso, podemos omitir a variável column 
        for _, values in dataset.items():
            if not isinstance(values, list):
               raise TypeError("Todos os valores no dicionário do dataset devem ser listas.")
        
        #aqui era legal que values fosse chamada de column 
        #para ficar mais legível 
        lengths = [len(values) for values in dataset.values()]
        if len(set(lengths)) != 1:
            raise ValueError("Todas as colunas no dataset devem ter o mesmo tamanho.")
        
        self.dataset = dataset

    def mean(self, column):
        """
        Calcula a média aritmética de uma coluna.

        Fórmula:
        $$ \mu = \frac{1}{N} \sum_{i=1}^{N} x_i $$

        Parâmetros
        ----------
        column : str
            O nome da coluna (chave do dicionário do dataset).

        Retorno
        -------
        float
            A média dos valores na coluna.
        """
        #aqui seria legal ter uma função para extrair dados da coluna 
        if column not in self.dataset:
            raise KeyError(f"A coluna '{column}' não existe no dataset.")
        
        dados = self.dataset[column]
        
        #até aqui a função retornando os dados

        # eu não sei se retornar 0.0 para uma lista vazia é uma boa
        # eu achava melhor lançar uma exceção para o caso da lista tá vazia
        if len(dados) == 0:
            return 0.0

        soma = 0
        for i in dados:
            soma += i

        # a soma poderia ser feito de outra forma:
        # soma = sum(dados) -> a função sum realiza a soma de todos os valores dentro
        # de uma lista
        media = soma / len(dados)

        return media

    def median(self, column):
        """
        Calcula a mediana de uma coluna.

        A mediana é o valor central de um conjunto de dados ordenado.

        Parâmetros
        ----------
        column : str
            O nome da coluna (chave do dicionário do dataset).

        Retorno
        -------
        float
            O valor da mediana da coluna.
        """
        # aqui é a mesma coisa que eu falei na outra métrica:
        # essa parte de extrair os dados deveria ser uma função a parte
        if column not in self.dataset:
            raise KeyError(f"A coluna '{column}' não existe no dataset.")
        
        data = self.dataset[column]

        n = len(data) # o ideal é termos nome de variáveis mais significativos 
        # length, size, number_elements

        # não sei se retornar zero para uma lista vazia é legal 
        # eu acho que seria legal retornar um valueError informando o dataset tá vazio
        if n == 0:
           return 0.0
        
        sorted_data = sorted(data) #boa a ordenação poderia ser feita assim
        if n % 2 == 1:
            return sorted_data[n // 2] #bom uso da divisão inteira
        else: 
            middle1 = sorted_data[n // 2 - 1]
            middle2 = sorted_data[n // 2]
            return (middle1 + middle2) / 2 # estratégia para mediana com tamanho de conjunto
        #pares

    def mode(self, column):
        """
        Encontra a moda (ou modas) de uma coluna.

        A moda é o valor que aparece com mais frequência no conjunto de dados.

        Parâmetros
        ----------
        column : str
            O nome da coluna (chave do dicionário do dataset).

        Retorno
        -------
        list
            Uma lista contendo o(s) valor(es) da moda.
        """       
        stats = self.dataset[column]
        
        #eu ainda acho que deveria lançar a exceção
        if not stats:
            return []  
        
        # o ideal aqui era chamar primeiro o freq acumulada
        #ela já daria conta de fazer esse processamento da frequência dos itens 
        #únicos da coluna
        counts = {}
        for i in stats:
            counts[i] = counts.get(i, 0) + 1
        
        max_freq = max(counts.values())
        modal = [item for item, freq in counts.items() if freq == max_freq] 
        #retorna os itens com o maior valor de frequência
        
        return modal

    def stdev(self, column):
        """
        Calcula o desvio padrão populacional de uma coluna.

        Fórmula:
        $$ \sigma = \sqrt{\frac{\sum_{i=1}^{N} (x_i - \mu)^2}{N}} $$

        Parâmetros
        ----------
        column : str
            O nome da coluna (chave do dicionário do dataset).

        Retorno
        -------
        float
            O desvio padrão dos valores na coluna.
        """
        
        stats = self.dataset[column]
        
        #eu ainda continuo achando que lançar a exceção fosse o melhor
        if not stats:
            return 0.0
        
        #aqui deveria reutilizar a função que calcula a variância

        #calcula a média
        sum = 0
        for i in stats:
            sum+=i
        average = sum/len(stats)
        
        #calcula a variância
        squares = 0
        for k in stats:
            squares+=(k-average) ** 2
        
        variance = squares/len(stats)
        
        #calcula o desvio padrão
        #esse método deveria ser apenas a chamada da variância e 
        # o cálculo da raiz quadrada da variância. 
        deviation = variance ** 0.5
        
        return float(deviation)
        
        

    def variance(self, column):
        """
        Calcula a variância populacional de uma coluna.

        Fórmula:
        $$ \sigma^2 = \frac{\sum_{i=1}^{N} (x_i - \mu)^2}{N} $$

        Parâmetros
        ----------
        column : str
            O nome da coluna (chave do dicionário do dataset).

        Retorno
        -------
        float
            A variância dos valores na coluna.
        """
        dados = self.dataset[column]

        #continuo achando que deveria lançar a exceção
        if len(dados) == 0:
            return 0.0

        #calcula a média 
        #aqui deveria ter chamado o método de calcular média
        soma = 0
        for i in dados:
            soma += i
        media = soma/len(dados)

        # a função deveria começar daqui
        numero_qdr = 0 #um nome ideal seria soma_quadrado_diferencas
        for j in dados: #j é um nome muito genérico, poderai ser amostra, valor
            numero_qdr += ( j - media) ** 2

        variancia = numero_qdr / len(dados) # aqui não precisava dessa variável 
        #poderia ter colocada a equação direto no return 
        # return numero_qdr / len(dados)
        return variancia

    def covariance(self, column_a, column_b):
        """
        Calcula a covariância entre duas colunas.

        Fórmula:
        $$ \text{cov}(X, Y) = \frac{\sum_{i=1}^{N} (x_i - \mu_x)(y_i - \mu_y)}{N} $$

        Parâmetros
        ----------
        column_a : str
            O nome da primeira coluna (X).
        column_b : str
            O nome da segunda coluna (Y).

        Retorno
        -------
        float
            O valor da covariância entre as duas colunas.
        """
        #se tivessemos a função que obtém os dados da coluna, essas validações 
        # não seriam repetidas tantas vezes
        dados_a = self.dataset[column_a]
        dados_b = self.dataset[column_b]

        #aqui deveria lançar uma exceção
        if len(dados_a) == 0 or len(dados_b) == 0:
            return 0.0

        #deveria ter chamado a função de media
        media_a = sum(dados_a) / len(dados_a)
        media_b = sum(dados_b) / len(dados_b)

        #o cálculo da covariância deveria ser aqui
        soma_covar = 0
        for x, y in zip(dados_a, dados_b):
            soma_covar += (x - media_a) * (y - media_b)

        covariancia = soma_covar / len(dados_a) 

        #o return aqui deveria ser já com a equação
        #return soma_covariancia / len(dados_a)
        return covariancia

    def itemset(self, column):
        """
        Retorna o conjunto de itens únicos em uma coluna.

        Parâmetros
        ----------
        column : str
            O nome da coluna (chave do dicionário do dataset).

        Retorno
        -------
        set
            Um conjunto com os valores únicos da coluna.
        """
        #aqui deveria ter a chamada da função 
        dados = self.dataset[column]

        itens_unicos = set(dados) # poderia já retornar o set
        #return set(dados)

        return itens_unicos

    def absolute_frequency(self, column):
        """
        Calcula a frequência absoluta de cada item em uma coluna.

        Parâmetros
        ----------
        column : str
            O nome da coluna (chave do dicionário do dataset).

        Retorno
        -------
        dict
            Um dicionário onde as chaves são os itens e os valores são
            suas contagens (frequência absoluta).
        """
        #ainda acho que essas validações e a obtenção dos dados deveria estar
        # na mesma função de obter_dados
        if column not in self.dataset:
            raise KeyError(f"A coluna '{column}' não existe no dataset.")
        
        values = self.dataset[column] # o nome aqui poderia ser column_values

        frequency = {} #como aqui pode armazenar a frequência de vários valores 
        # o nome da variável deveria ser frequencies
        
        for value in values:
            frequency[value] = frequency.get(value, 0) + 1
        
        return frequency

    def relative_frequency(self, column):
        """
        Calcula a frequência relativa de cada item em uma coluna.

        Parâmetros
        ----------
        column : str
            O nome da coluna (chave do dicionário do dataset).

        Retorno
        -------
        dict
            Um dicionário onde as chaves são os itens e os valores são
            suas proporções (frequência relativa).
        """
        #chamada da função que valida
        stats = self.dataset[column] #column_values seria um bom nome
        
        if len(stats) == 0:
            return {}
        
        #aqui deveria ser uma chamada para a função de calcular a freq absoluta
        total = len(stats)
        relative = {} #relative_frequencies seria um bom nome
        for i in stats:
            relative[i] = relative.get(i, 0) + 1  

        #aqui você calcularia a freq relativa
        #relative_frequencies = {item: (count / total) * 100 for item, count in absolute_frequencies.items()}
        for k in relative:
            relative[k] = relative[k]/total
                
        #retornaria relative_frequencies
        return relative
        
    

    def cumulative_frequency(self, column, frequency_method='absolute'):
        """
        Calcula a frequência acumulada (absoluta ou relativa) de uma coluna.

        A frequência é calculada sobre os itens ordenados.

        Parâmetros
        ----------
        column : str
            O nome da coluna (chave do dicionário do dataset).
        frequency_method : str, opcional
            O método a ser usado: 'absolute' para contagem acumulada ou
            'relative' para proporção acumulada (padrão é 'absolute').

        Retorno
        -------
        dict
            Um dicionário ordenado com os itens como chaves e suas
            frequências acumuladas como valores.
        """
        #essa validação deveria ser feita em outra função onde se obtem o valor
        #então, não estaria duplicada aqui
        if column not in self.dataset:
            raise KeyError(f"A coluna '{column}' não existe no dataset.")
        
        if frequency_method == 'absolute':
            freq = self.absolute_frequency(column) #a variável deveria ser chamada de frequencies
        elif frequency_method == 'relative':
            freq = self.relative_frequency(column) #a variável deveria ser chamada de frequencies
        else:
         raise ValueError("O 'frequency_method' deve ser 'absolute' ou 'relative'.") #identação está errada
        
        sorted_values = sorted(freq.keys())
        cumulative_freq = {}
        cumulative = 0
        
        for value in sorted_values:
            cumulative += freq[value]
            cumulative_freq[value] = cumulative
        
        return cumulative_freq


    def conditional_probability(self, column, value1, value2):
        """
        Calcula a probabilidade condicional P(X_i = value1 | X_{i-1} = value2).

        Este método trata a coluna como uma sequência e calcula a probabilidade
        de encontrar `value1` imediatamente após `value2`.

        Fórmula: P(A|B) = Contagem de sequências (B, A) / Contagem total de B

        Parâmetros
        ----------
        column : str
            O nome da coluna (chave do dicionário do dataset).
        value1 : any
            O valor do evento consequente (A).
        value2 : any
            O valor do evento condicionante (B).

        Retorno
        -------
        float
            A probabilidade condicional, um valor entre 0 e 1.
        """
        #essa validação deveria tá em outro método
        if column not in self.dataset:
            raise KeyError(f"A coluna '{column}' não existe no dataset.")
        
        stats = self.dataset[column]
        if len(stats) < 2:
            return 0.0
        
        count_b = 0
        count_ba = 0
        
        #calcula a quantidade de eventos que acontecem b 
        event = stats[0]
        for i in stats[0:]:
            if event == value2:
                count_b += 1
                # calcula a quantidade de eventos que acontecem a e b juntos
                if i == value1:
                    count_ba += 1
            event = i 
            
        if count_b > 0:
            prob_a = count_ba/count_b
            return round(prob_a, 7)  #eu acho que 5 seria o suficiente
        else: 
            return 0.0