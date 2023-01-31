
from typing import Tuple, Any, Dict
from .dataset_interface import DatasetInterface


class NewsDataset(DatasetInterface):
    def __init__(self, path: str) -> None:
        super().__init__(path)
        # ler arquivo contendo os nomes dos arquivos de noticias e as classes

        path = 'data/datasets/news-tiny/test.txt'
        with open(path, "r", encoding='latin-1', errors='ignore') as file:
            self.list = file.readlines()

    def size(self) -> int:
        # retornar o numero de noticias no dataset (numero de linhas no arquivo)

        return len(self.list)

    def get(self, idx: int) -> Tuple[Any, str]:
        # ler a i-esima noticia do disco e retornar o texto como uma string e
        # a classe
        newsText, newsClass = self.list[idx].split()

        return newsText, newsClass
