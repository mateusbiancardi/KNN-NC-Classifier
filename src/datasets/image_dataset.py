
from typing import Tuple, Any, Dict
from .dataset_interface import DatasetInterface

import cv2

class ImageDataset(DatasetInterface):
    def __init__(self, path: str) -> None:
        super().__init__(path)
        # ler arquivo contendo os nomes das imagens e as classes e armazenar
        # em uma lista

        path = "/home/lcee/Documentos/POO-P2/TRAB2-POO-UFES/data/datasets/img_small/test.txt"

        with open(path, "r") as file:
            self.list = file.readlines()

    def size(self) -> int:
        # retornar tamanho do dataset (numero de linhas do arquivo)

        return len(self.list)

    def get(self, idx: int) -> Tuple[Any, str]:
        # ler a i-esima imagem do disco usando a biblioteca cv2 e retornar
        # a imagem e a respectiva classe


        imagePath, imageClass = self.list[idx-1].split()

        image = cv2.imread(imagePath, cv2.IMREAD_GRAYSCALE)

        return image, imageClass
