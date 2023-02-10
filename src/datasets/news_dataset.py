
from typing import Tuple, Any, Dict
from .dataset_interface import DatasetInterface


class NewsDataset(DatasetInterface):
    def __init__(self, path: str, train_path: str) -> None:
        super().__init__(path)
        # ler arquivo contendo os nomes dos arquivos de noticias e as classes

        # Stopwords, path da notícia e path da notícia de treino
        self.path = path
        self.train_path = train_path
        self.stopwords = ['de',  'a',  'o',  'que',  'e',  'do',  'da',  'em',  'um',  'para',  'é',  'com',  'não',  'uma',  'os',  'no',  'se',  'na',  'por',  'mais',  'as',  'dos',  'como',  'mas',  'foi',  'ao',  'ele',  'das',  'tem',  'à',  'seu',  'sua',  'ou',  'ser',  'quando',  'muito',  'há',  'nos',  'já',  'está',  'eu',  'também',  'só',  'pelo',  'pela',  'até',  'isso',  'ela',  'entre',  'era',  'depois',  'sem',  'mesmo',  'aos',  'ter',  'seus',  'quem',  'nas',  'me',  'esse',  'eles',  'estão',  'você',  'tinha',  'foram',  'essa',  'num',  'nem',  'suas',  'meu',  'às',  'minha',  'têm',  'numa',  'pelos',  'elas',  'havia',  'seja',  'qual',  'será',  'nós',  'tenho',  'lhe',  'deles',  'essas',  'esses',  'pelas',  'este',  'fosse',  'dele',  'tu',  'te',  'vocês',  'vos',  'lhes',  'meus',  'minhas',  'teu',  'tua',  'teus',  'tuas',  'nosso',  'nossa',  'nossos',  'nossas',  'dela',  'delas',  'esta',  'estes',  'estas',  'aquele',  'aquela',  'aqueles',  'aquelas',  'isto',  'aquilo',  'estou',  'está',  'estamos',  'estão',  'estive',  'esteve',  'estivemos',  'estiveram',  'estava',  'estávamos',  'estavam',  'estivera',  'estivéramos',  'esteja',  'estejamos',  'estejam',  'estivesse',  'estivéssemos',  'estivessem',  'estiver',  'estivermos',  'estiverem',  'hei',  'há',  'havemos',  'hão',  'houve',  'houvemos',  'houveram',  'houvera',  'houvéramos',  'haja',  'hajamos',  'hajam',  'houvesse',  'houvéssemos',  'houvessem',  'houver',  'houvermos',  'houverem',  'houverei',  'houverá',  'houveremos',  'houverão',  'houveria',  'houveríamos',  'houveriam',  'sou',  'somos',  'são',  'era',  'éramos',  'eram',  'fui',  'foi',  'fomos',  'foram',  'fora',  'fôramos',  'seja',  'sejamos',  'sejam',  'fosse',  'fôssemos',  'fossem',  'for',  'formos',  'forem',  'serei',  'será',  'seremos',  'serão',  'seria',  'seríamos',  'seriam',  'tenho',  'tem',  'temos',  'tém',  'tinha',  'tínhamos',  'tinham',  'tive',  'teve',  'tivemos',  'tiveram',  'tivera',  'tivéramos',  'tenha',  'tenhamos',  'tenham',  'tivesse',  'tivéssemos',  'tivessem',  'tiver',  'tivermos',  'tiverem',  'terei',  'terá',  'teremos',  'terão',  'teria',  'teríamos',  'teriam']
        
        with open(self.path, "r", encoding='latin-1', errors='ignore') as file:
            self.list = file.readlines()

        with open(self.train_path, "r", encoding='latin-1', errors='ignore') as trainFile:
            self.trainList = trainFile.readlines()
        
        self.path, _ = self.path.rsplit("/", 1)
        self.train_path, _ = self.train_path.rsplit("/", 1)

        # Armazena todas as palavras de treino
        self.trainWords = self.train_words()

    def size(self) -> int:
        # retornar o numero de noticias no dataset (numero de linhas no arquivo)
        return len(self.list)

    def get(self, idx: int) -> Tuple[Any, str]:
        # ler a i-esima noticia do disco e retornar o texto como uma string e
        # a classe
        newsPath, newsClass = self.list[idx].split()
        newsPath = self.path + '/' + newsPath

        with open(newsPath, 'r') as nPath:
            self.words = nPath.readline().split()

        self.words = self.removeStopWords(self.stopwords, self.words)

        # Atribui cada palavra de todos as palavras de train em um dicionario
        word_count = {}
        for i in self.trainWords:        
            word_count[i] = 0

        # Verifica a quantidade de cada palavra e vetoriza
        word_vector = []
        for i in range(len(self.words)):
            if self.words[i] not in word_count:
                word_count[self.words[i]] = 1
            else:
                word_count[self.words[i]] += 1
    
        for i in self.trainWords:
            word_vector.append(word_count[i])

        return word_vector, newsClass
    
    def train_words(self):
        words = ''
        for i in range(len(self.trainList)):
            trainNewsPath, _ = self.trainList[i].split()
            trainNewsPath = self.train_path + '/' + trainNewsPath

            with open(trainNewsPath, 'r') as trainNPath:
                words += trainNPath.readline()
        words = words.split()
        words = self.removeStopWords(self.stopwords, words)

        return words
            
    def removeStopWords (self, stopwords, words):
        for i in stopwords:
            for j in words:
                if i == j:
                    words.remove(i)
        return words