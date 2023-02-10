

from typing import Dict
import json

def load_config(path: str) -> Dict:
    """ le o arquivo json e retorna como um dicionario """
    dummy_JSON_string = """
    {
        "type": "news",
        "train_path": "data/datasets/news-medium-small/train.txt",
        "test_path": "data/datasets/news-medium-small/test.txt",
        "classifier": "nc"
    }
    """

    dummy_dict = json.loads(dummy_JSON_string)
    
    # we're returning dummy values just to make the main program runnable
    # dummy_dict = {
    #     "type": "image",
    #     "train_path": "data/datasets/img_small/train.txt",
    #     "test_path": "data/datasets/img_small/test.txt",
    #     "classifier": "knn"
    # } 


    return dummy_dict
