
from typing import Dict, List
from .classifier_interface import ClassifierInterface
from src.datasets.dataset_interface import DatasetInterface
import math
from collections import Counter


class KnnClassifier(ClassifierInterface):
    def __init__(self) -> None:
        super().__init__()

    def train(self, train_dataset: DatasetInterface) -> None:
        # salvar as amostras do dataset
        self.train_samples = []
        for i in range(train_dataset.size()):
            sample, classe = train_dataset.get(i)
            self.train_samples.append((sample, classe))
            print (self.train_samples)


    def predict(self, test_dataset: DatasetInterface) -> List[str]:
        """ para cada amostra no dataset, buscar os k vizinhos mais proximos e 
        retornar a classe mais frequente entre eles """

        k = 5
        k_neighbors = []
        vector_class = []
        for m in range(k):
            #armazena o infinito e 'nada' nas listas
            k_neighbors.append(math.inf)
            vector_class.append(None)

        for j in range(test_dataset.size()):
            sum_total = 0
            for i in range(test_dataset.size()):
                #j "entra" no conjunto (vetor, classe), 0 entra no vetor e
                # i entra na coordenada do vetor (xi ou yi) 
                sum_total += test_dataset[j][0][0][i] - self.train_samples[j][0][0][i]

            print (sum_total)
            
            euclidian_Distance = math.sqrt(sum_total)


            # Verifica o maior numero, depois verifica o indice desse numero na lista 
            # k_neighbors
            bigger_number = max(k_neighbors)
            bigger_index = k_neighbors.index(bigger_number)

            # verifica se o maior numero obtido da lista anteriormente é maior que a distancia euclidiana
            # se sim, armazena ela na posição do maior valor e sua respectiva classe
            if euclidian_Distance < k_neighbors[bigger_index]:
                k_neighbors[bigger_index] = euclidian_Distance
                vector_class[bigger_index] = test_dataset[j][1]
        
        count = Counter(vector_class)
        most_Common = count.most_common(1)[0][0]

        return most_Common
