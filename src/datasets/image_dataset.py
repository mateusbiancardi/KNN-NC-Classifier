
from typing import Tuple, Any, Dict
from .dataset_interface import DatasetInterface

import cv2

class ImageDataset(DatasetInterface):
    def __init__(self, path: str) -> None:
        super().__init__(path)
        # ler arquivo contendo os nomes das imagens e as classes e armazenar
        # em uma lista

        
        self.path = path

        with open(self.path, "r") as file:
            self.list = file.readlines()
        
        self.path, _ = self.path.rsplit("/", 1)

    def size(self) -> int:
        # retornar tamanho do dataset (numero de linhas do arquivo)
        self.dataset_size = len(self.list)

        return self.dataset_size

    def get(self, idx: int) -> Tuple[Any, str]:
        # ler a i-esima imagem do disco usando a biblioteca cv2 e retornar
        # a imagem e a respectiva classe
        vector_image = []

        imagePath, imageClass = self.list[idx].split()
        imagePath = self.path + '/' + imagePath
        image = cv2.imread(imagePath, cv2.IMREAD_GRAYSCALE)

        for i in range (len(image)):
            for j in range(len(image[0])):
                vector_image.append(int(image[i][j]))

        #print (vector_image)

        return vector_image, str(imageClass)
