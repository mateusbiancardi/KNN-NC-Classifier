
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

        self.average_vector = {}
        for cls, lst_vetores in self.class_finder.items():
            """ calcular centroides para cada classe   """
            # para cada vetor in lst_vetores
            for j in range(len(lst_vetores[0])):
                sum = 0
                for i in range(len(lst_vetores)):        
                    # para cada dimensao do vetor
                    sum += lst_vetores[i][j]

                if cls not in self.average_vector:
                    self.average_vector[cls] = []

                self.average_vector[cls].append(sum/len(lst_vetores))
                    # ....
            #print (self.average_vector[cls])
    
        return self.average_vector
        

    def predict(self, test_dataset: DatasetInterface) -> List[str]:
        """ para cada amostra no dataset, buscar o centroide mais proximo e respectiva retornar a classe """
        euclidian_All = []
        euclidian_list = {}
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

        #print (euclidian_list[cls])
        minor_distance = math.inf
        minor_temporary = 0
        minor_index = []

        for i in range(len(euclidian_list)):
            for cls, _ in euclidian_list.items():
                if euclidian_list[cls][0][i] < minor_distance:
                    minor_distance = euclidian_list[cls][0][i]
                    minor_temporary = cls
                minor_index.append(minor_temporary)
                minor_distance = math.inf

        #print (minor_index)
        
        result = []
        for i in range(len(minor_index)):
            class_count = {}
            for cls, _ in euclidian_list.items():
                if minor_index[i] in class_count:
                    class_count[minor_index[i]] += 1
                else:
                    class_count[minor_index[i]] = 1
                result.append(max(class_count, key=class_count.get))  
        print (result)
        return result
