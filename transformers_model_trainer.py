import typing as tp

import pandas as pd
from torch.utils.data import Dataset


class CustomDataset(Dataset):
    """
    This class designs logic to retrieve data from a custom dataset.
    According to pytorch Datacet conception any map style dataset
    should implement at least __len__ and __getitem__ methods.
    """

    def __init__(
        self,
    ) -> None:
        """
        YOUR CODE HERE
        """
        pass

    def __len__(self) -> int:
        """
        returns number of rows in data
        """

        """
        YOUR CODE HERE
        """
        pass

    def __getitem__(self, idx: int) -> tp.Dict[str, tp.Any]:
        """
        retrieves data for single index.
        may include data processing and transformations.
        E.g. augmenting data or tokenizing it.
        returns dict with keys "input_ids", "label" and probably some more metadata (you decide whethere you need something more here)
        """

        """
        YOUR CODE HERE
        """
        pass


class ModelTrainer:
    """
    This class implements logic run an experiemnt with a provided transformers classification model.
    It incudes following components:
    - load data
    - load and configure a model and its artifacts
    - train model
    - validate model
    - save model
    - compue metrics
    - run_experiment (as the man entrypoint to execute all flow)

    Attention: current module intentionally doesnt support model inference or model serving.
    It is a good practice to separate train/inference classes otherwise it is hard to maintain it all.

    """

    def __init__(self):
        """
        YOUR CODE HERE
        """
        pass

    def configure_optimizer(self) -> None:
        """
        adds a self.optimizer attribute with a chosen optimizer and its params.
        """

        """
        YOUR CODE HERE
        """
        pass

    def configure_scheduler(self) -> None:
        """
        adds a self.scheduler attribute with a chosen scheduler (e.g. ReduceLROnPlateau).
        """

        """
        YOUR CODE HERE
        """
        pass

    def apply_data_parallel(self) -> None:
        """
        checks number of available cuda devices,
        if number of GPUs is > 1, moves self.model to a DataParallel state for faster training.
        """

        """
        YOUR CODE HERE
        """
        pass

    def load_data(self, filename: str, split: str) -> pd.DataFrame:
        """
        uses Datasets library to load a dataset, takes as input dataset name (e.g. "imdb")
        and a split. Loads data into pandas.
        """

        """
        YOUR CODE HERE
        """
        pass

    def train(self, dataset: CustomDataset) -> None:
        """
        YOUR CODE HERE
        """
        pass

    def validate(self, dataset: CustomDataset) -> tp.Dict[str, tp.Iterable]:
        """
        takes a trained model and runs it on validation data.
        Returns a dict with the keys "valid_labels" and "valid_preds" and corrsponding values.
        """

        """
        YOUR CODE HERE
        """
        pass

    def compute_metrics_report(
        self, labels: tp.Iterable, predictions: tp.Iterable
    ) -> tp.Any:
        """
        Computes classification metric (or several metrcis) for given task.
        """

        """
        YOUR CODE HERE
        """
        pass

    def save_model(self, dst_path: str) -> None:
        """
        Saves model to dst_path. Be careful to check if a model is on DataParallel state.
        If it is, one needs to process it accordingly.
        """

        """
        YOUR CODE HERE
        """
        pass

    def run_experiment(self):
        """
        Main entrypoint.
        Runs the flow from loading data to computing metrics.
        """

        """
        YOUR CODE HERE
        """
        pass


if __name__ == "__main__":
    """run experiment"""
    model_trainer = ModelTrainer(...)
    model_trainer.run_experiment()
