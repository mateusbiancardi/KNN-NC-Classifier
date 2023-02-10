
from typing import Dict


def write_report(path: str, config: Dict, metrics_values) -> None:
    """ escreve o arquivo de relatorio do experimento """

    pathDataset = config["train_path"][:-9]

    file = open(path, 'w')
    file.write (f'dataset: {config["type"]}\n'
                f'classifier: {config["classifier"]}\n'
                f'path: {pathDataset}\n'
                f'training time per sample: {metrics_values["train_time"]:.4f}s\n'
                f'inference time per sample: {metrics_values["pred_time"]:.4f}s\n'
                f'accuracy: {metrics_values["accuracy"]:.2f}'
    )