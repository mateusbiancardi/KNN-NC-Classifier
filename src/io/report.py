
from typing import Dict


def write_report(path: str, config: Dict, metrics_values) -> None:
    """ escreve o arquivo de relatorio do experimento """
    file = open(path, 'w')
    file.write (f'accuracy: {metrics_values["accuracy"]:.2f}')