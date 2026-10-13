"""Generated from Smithy shape ``com.amazonaws.bedrock#EvaluationDatasetMetricConfigs``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock.types.evaluation_dataset_metric_config

EvaluationDatasetMetricConfigs: TypeAlias = list[
    "capo_bedrock.types.evaluation_dataset_metric_config.EvaluationDatasetMetricConfig"
]


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationDatasetMetricConfigs) -> list:
    import capo_bedrock.types.evaluation_dataset_metric_config

    out: list = []
    for item in value:
        out.append(
            capo_bedrock.types.evaluation_dataset_metric_config.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> EvaluationDatasetMetricConfigs:
    import capo_bedrock.types.evaluation_dataset_metric_config

    out: EvaluationDatasetMetricConfigs = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock.types.evaluation_dataset_metric_config.deserialize_json(item)
        )
    return out


def redact_sensitive(value: EvaluationDatasetMetricConfigs) -> list[Any]:
    import capo_bedrock.types.evaluation_dataset_metric_config

    return [
        capo_bedrock.types.evaluation_dataset_metric_config.redact_sensitive(item)
        for item in value
    ]
