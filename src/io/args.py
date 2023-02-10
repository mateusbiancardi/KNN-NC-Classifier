
import argparse
from typing import Any


def parse_args() -> Any:
    """ le os argumentos de linha de comando usando a biblioteca argparse """

    parser = argparse.ArgumentParser()
    parser.add_argument('config_path', type=str)
    parser.add_argument('report_path', type=str)
    args = parser.parse_args()

    # Exemplo. Utilizar o argparse na versao final
    return args
