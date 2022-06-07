from lavis.common.registry import registry

from lavis.datasets.builders.base_dataset_builder import BaseDatasetBuilder
from lavis.datasets.datasets.snli_ve_datasets import SNLIVisualEntialmentDataset


@registry.register_builder("snli_ve")
class SNLIVisualEntailmentBuilder(BaseDatasetBuilder):
    train_dataset_cls = SNLIVisualEntialmentDataset
    eval_dataset_cls = SNLIVisualEntialmentDataset

    def __init__(self, cfg=None):
        super().__init__(cfg)

    @classmethod
    def default_config_path(cls, type="default"):
        paths = {"default": "lavis/configs/datasets/snli_ve/defaults.yaml"}

        return paths[type]

    def _download_vis(self):
        pass