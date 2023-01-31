
from src.datasets.dataset_factory import create_dataset
from src.classifiers.classifier_factory import create_classifier
from src.experiment import Experiment
from src.io.args import parse_args
from src.io.config import load_config
from src.io.report import write_report


def main():
    # obter os nomes dos arquivos de configuracao e de saida da linha de comando
    # args = parse_args()
    # le o arquivo json e retorna como um dicionario
    config = load_config("data/configs/knn_image_config.json")

    train_dataset = create_dataset(config["train_path"], config["type"])
    test_dataset = create_dataset(config["test_path"], config["type"])
    classifier = create_classifier(config["classifier"])

    experiment = Experiment(train_dataset, test_dataset)
    metrics = experiment.run(classifier)

    # escreve o arquivo de saida
    write_report("report.txt", config, metrics)

    print("Success.")


if __name__ == "__main__":
    main()
