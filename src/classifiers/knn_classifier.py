
from typing import Dict, List
from .classifier_interface import ClassifierInterface
from src.datasets.dataset_interface import DatasetInterface
import math
from collections import Counter
import heapq


class KnnClassifier(ClassifierInterface):
    def __init__(self) -> None:
        super().__init__()

    def train(self, train_dataset: DatasetInterface) -> None:
        # salvar as amostras do dataset
        self.train_samples = []
        for i in range(train_dataset.size()):
            self.train_samples.append(train_dataset.get(i))
            


    def predict(self, test_dataset: DatasetInterface) -> List[str]:
        """ para cada amostra no dataset, buscar os k vizinhos mais proximos e 
        retornar a classe mais frequente entre eles """
        k = 5
        euclidian_All = []
        euclidian_list = []

        # Lê todas as amostras de treino e calcula a distância euclidiana
        for j in range(test_dataset.size()):
            amostra, classe = test_dataset.get(j)

            for m in range(len(self.train_samples)):
                
                sum_total = 0
                for i in range(len(amostra)):                
                    sum_total += math.pow(float(amostra[i]) - float(self.train_samples[m][0][i]), 2)

                # armazena todas as distancias em uma lista
                euclidian_Distance = math.sqrt(sum_total)
                euclidian_All.append(euclidian_Distance)
            
            
            euclidian_list.append(euclidian_All)
            euclidian_All = []
            
        k_neighbors_all = []
        k_smallest_index = []
        k_temporary_index = []

        # Pega os index dos menores valores de distância euclidiana
        for m in range(test_dataset.size()):
            k_neighbors_all = heapq.nsmallest(k, euclidian_list[m])
            for i in range(k):
                k_temporary_index.append(euclidian_list[m].index(k_neighbors_all[i]))

            k_smallest_index.append(k_temporary_index)
            k_temporary_index = []
        

        # Calcula qual classe mais apareceu e retorna uma lista com os valores
        result = []
        for m in range(test_dataset.size()):
            class_count = {}
            for i in k_smallest_index[m]:
                if self.train_samples[i][1] in class_count:
                    class_count[self.train_samples[i][1]] += 1
                else:
                    class_count[self.train_samples[i][1]] = 1
            result.append(max(class_count, key=class_count.get))  
        return result