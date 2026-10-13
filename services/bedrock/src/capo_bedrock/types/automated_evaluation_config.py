"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedEvaluationConfig``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock.types.automated_evaluation_custom_metric_config
    import capo_bedrock.types.evaluation_dataset_metric_configs
    import capo_bedrock.types.evaluator_model_config


class AutomatedEvaluationConfig(TypedDict, closed=True):
    dataset_metric_configs: "capo_bedrock.types.evaluation_dataset_metric_configs.EvaluationDatasetMetricConfigs"
    """<p>Configuration details of the prompt datasets and metrics you want to use for your evaluation job.</p>"""
    evaluator_model_config: NotRequired[
        "capo_bedrock.types.evaluator_model_config.EvaluatorModelConfig"
    ]
    """<p>Contains the evaluator model configuration details. <code>EvaluatorModelConfig</code> is required for evaluation jobs that use a knowledge base or in model evaluation job that use a model as judge. This model computes all evaluation related metrics.</p>"""
    custom_metric_config: NotRequired[
        "capo_bedrock.types.automated_evaluation_custom_metric_config.AutomatedEvaluationCustomMetricConfig"
    ]
    """<p>Defines the configuration of custom metrics to be used in an evaluation job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedEvaluationConfig) -> dict:
    out: dict = {}
    import capo_bedrock.types.evaluation_dataset_metric_configs

    out["datasetMetricConfigs"] = (
        capo_bedrock.types.evaluation_dataset_metric_configs.serialize_json(
            value["dataset_metric_configs"]
        )
    )
    if "evaluator_model_config" in value:
        import capo_bedrock.types.evaluator_model_config

        out["evaluatorModelConfig"] = (
            capo_bedrock.types.evaluator_model_config.serialize_json(
                value["evaluator_model_config"]
            )
        )
    if "custom_metric_config" in value:
        import capo_bedrock.types.automated_evaluation_custom_metric_config

        out["customMetricConfig"] = (
            capo_bedrock.types.automated_evaluation_custom_metric_config.serialize_json(
                value["custom_metric_config"]
            )
        )
    return out


def deserialize_json(data: dict) -> AutomatedEvaluationConfig:
    out: AutomatedEvaluationConfig = {}  # type: ignore[typeddict-item]
    if data.get("datasetMetricConfigs") is not None:
        import capo_bedrock.types.evaluation_dataset_metric_configs

        out["dataset_metric_configs"] = (
            capo_bedrock.types.evaluation_dataset_metric_configs.deserialize_json(
                data["datasetMetricConfigs"]
            )
        )
    else:
        raise DeserializationError(
            "AutomatedEvaluationConfig.dataset_metric_configs required"
        )
    if data.get("evaluatorModelConfig") is not None:
        import capo_bedrock.types.evaluator_model_config

        out["evaluator_model_config"] = (
            capo_bedrock.types.evaluator_model_config.deserialize_json(
                data["evaluatorModelConfig"]
            )
        )
    if data.get("customMetricConfig") is not None:
        import capo_bedrock.types.automated_evaluation_custom_metric_config

        out["custom_metric_config"] = (
            capo_bedrock.types.automated_evaluation_custom_metric_config.deserialize_json(
                data["customMetricConfig"]
            )
        )
    return out


def redact_sensitive(value: AutomatedEvaluationConfig) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "dataset_metric_configs" in value:
        import capo_bedrock.types.evaluation_dataset_metric_configs

        out["dataset_metric_configs"] = (
            capo_bedrock.types.evaluation_dataset_metric_configs.redact_sensitive(
                value["dataset_metric_configs"]
            )
        )
    if "custom_metric_config" in value:
        import capo_bedrock.types.automated_evaluation_custom_metric_config

        out["custom_metric_config"] = (
            capo_bedrock.types.automated_evaluation_custom_metric_config.redact_sensitive(
                value["custom_metric_config"]
            )
        )
    return out
