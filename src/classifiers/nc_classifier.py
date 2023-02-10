
import heapq
import math
from typing import Dict, List

from .classifier_interface import ClassifierInterface
from src.datasets.dataset_interface import DatasetInterface


class NearestCentroidClassifier(ClassifierInterface):
    def __init__(self) -> None:
        super().__init__()

    def train(self, train_dataset: DatasetInterface) -> None:
        """ calcular os centroides por classe """
        # Armazena os vetores de treino
        self.train_samples = []
        for i in range(train_dataset.size()):
            self.train_samples.append(train_dataset.get(i))

        # Verifica as classes existentes
        self.class_finder = {}
        for i in range(len(self.train_samples)):
            cls = self.train_samples[i][1]

            if cls not in self.class_finder:
                self.class_finder[cls] = []
            
            self.class_finder[cls].append(self.train_samples[i][0])

        # Calcula o centróide
        self.average_vector = {}
        for cls, lst_vetores in self.class_finder.items():
            """ calcular centroides para cada classe   """
            # Para cada dimensão do vetor
            for j in range(len(lst_vetores[0])):
                sum = 0
                for i in range(len(lst_vetores)):        
                    # Para cada vetor
                    sum += lst_vetores[i][j]

                if cls not in self.average_vector:
                    self.average_vector[cls] = []

                self.average_vector[cls].append(sum/len(lst_vetores[0]))
                
        

    def predict(self, test_dataset: DatasetInterface) -> List[str]:
        """ para cada amostra no dataset, buscar o centroide mais proximo e respectiva retornar a classe """
        # Cálculo da distância euclidiana dos vetores de teste e os centróides
        euclidian_All = []
        euclidian_list = {}
        # Criação da biblioteca que armazena a distância do vetor a cada centróide 
        for cls, _ in self.average_vector.items():
            clsTemp = cls
            for i in range(test_dataset.size()):
                amostra, classe = test_dataset.get(i)
                sum_total = 0
                
                for j in range (len(self.average_vector[cls])):
                    sum_total += math.pow(float(amostra[j]) - float(self.average_vector[cls][j]), 2)

                euclidian_Distance = math.sqrt(sum_total)
                euclidian_All.append(euclidian_Distance)

            if cls not in euclidian_list:
                euclidian_list[cls] = []

            euclidian_list[cls].append(euclidian_All)
            euclidian_All = []
        
        # Verifica a menor distância do vetor a classe e retorna o predict 
        # de cada vetor
        minor_distance = math.inf
        minor_temporary = 0
        minor_index = []

        for i in range(len(euclidian_list[clsTemp][0])):
            for cls, _ in euclidian_list.items():
                if euclidian_list[cls][0][i] < minor_distance:
                    minor_distance = euclidian_list[cls][0][i]
                    minor_temporary = cls
            minor_distance = math.inf
            minor_index.append(minor_temporary)
            
        return minor_index