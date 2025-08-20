class Statistics:
    def __init__(self, dataset: dict):
        if not isinstance(dataset, dict):
            raise TypeError
        sizes = [len(values) for values in dataset.values()]
        if len(set(sizes)) != 1:
            raise ValueError
        for column, values in dataset.items():
            if not values:
                raise ValueError
            
            value_type = type(values[0])
            if not all(isinstance(v, value_type) for v in values):
                raise TypeError
        
        self.dataset = dataset

    def mean(self, column: str) -> float:
        if column not in self.dataset:
            raise KeyError(f"A coluna '{column}' não existe no dataset.")
        
        values = self.dataset[column]
        
        if not all(isinstance(v, (int, float)) for v in values):
            raise TypeError
        
        return sum(values) / len(values)

    def absolute_frequency(self, column: str) -> dict:
        if column not in self.dataset:
            raise KeyError(f"A coluna '{column}' não existe no dataset.")
        
        values = self.dataset[column]
        frequency = {}
        
        for value in values:
            frequency[value] = frequency.get(value, 0) + 1
        
        return frequency

    def cumulative_frequency(self, column: str) -> dict:
        if column not in self.dataset:
            raise KeyError(f"A coluna '{column}' não existe no dataset.")
        
        absolute_freq = self.absolute_frequency(column)
        sorted_values = sorted(absolute_freq.keys())
        
        cumulative_freq = {}
        cumulative = 0
        
        for value in sorted_values:
            cumulative += absolute_freq[value]
            cumulative_freq[value] = cumulative
        
        return cumulative_freq

            
    
