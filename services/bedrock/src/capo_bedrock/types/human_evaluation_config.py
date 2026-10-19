"""Generated from Smithy shape ``com.amazonaws.bedrock#HumanEvaluationConfig``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock.types.evaluation_dataset_metric_configs
    import capo_bedrock.types.human_evaluation_custom_metrics
    import capo_bedrock.types.human_workflow_config


class HumanEvaluationConfig(TypedDict, closed=True):
    human_workflow_config: NotRequired[
        "capo_bedrock.types.human_workflow_config.HumanWorkflowConfig"
    ]
    """<p>The parameters of the human workflow.</p>"""
    custom_metrics: NotRequired[
        "capo_bedrock.types.human_evaluation_custom_metrics.HumanEvaluationCustomMetrics"
    ]
    """<p>A <code>HumanEvaluationCustomMetric</code> object. It contains the names the metrics, how the metrics are to be evaluated, an optional description.</p>"""
    dataset_metric_configs: "capo_bedrock.types.evaluation_dataset_metric_configs.EvaluationDatasetMetricConfigs"
    """<p>Use to specify the metrics, task, and prompt dataset to be used in your model evaluation job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HumanEvaluationConfig) -> dict:
    out: dict = {}
    if "human_workflow_config" in value:
        import capo_bedrock.types.human_workflow_config

        out["humanWorkflowConfig"] = (
            capo_bedrock.types.human_workflow_config.serialize_json(
                value["human_workflow_config"]
            )
        )
    if "custom_metrics" in value:
        import capo_bedrock.types.human_evaluation_custom_metrics

        out["customMetrics"] = (
            capo_bedrock.types.human_evaluation_custom_metrics.serialize_json(
                value["custom_metrics"]
            )
        )
    import capo_bedrock.types.evaluation_dataset_metric_configs

    out["datasetMetricConfigs"] = (
        capo_bedrock.types.evaluation_dataset_metric_configs.serialize_json(
            value["dataset_metric_configs"]
        )
    )
    return out


def deserialize_json(data: dict) -> HumanEvaluationConfig:
    out: HumanEvaluationConfig = {}  # type: ignore[typeddict-item]
    if data.get("humanWorkflowConfig") is not None:
        import capo_bedrock.types.human_workflow_config

        out["human_workflow_config"] = (
            capo_bedrock.types.human_workflow_config.deserialize_json(
                data["humanWorkflowConfig"]
            )
        )
    if data.get("customMetrics") is not None:
        import capo_bedrock.types.human_evaluation_custom_metrics

        out["custom_metrics"] = (
            capo_bedrock.types.human_evaluation_custom_metrics.deserialize_json(
                data["customMetrics"]
            )
        )
    if data.get("datasetMetricConfigs") is not None:
        import capo_bedrock.types.evaluation_dataset_metric_configs

        out["dataset_metric_configs"] = (
            capo_bedrock.types.evaluation_dataset_metric_configs.deserialize_json(
                data["datasetMetricConfigs"]
            )
        )
    else:
        out["dataset_metric_configs"] = []
    return out


def redact_sensitive(value: HumanEvaluationConfig) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "human_workflow_config" in value:
        import capo_bedrock.types.human_workflow_config

        out["human_workflow_config"] = (
            capo_bedrock.types.human_workflow_config.redact_sensitive(
                value["human_workflow_config"]
            )
        )
    if "custom_metrics" in value:
        import capo_bedrock.types.human_evaluation_custom_metrics

        out["custom_metrics"] = (
            capo_bedrock.types.human_evaluation_custom_metrics.redact_sensitive(
                value["custom_metrics"]
            )
        )
    if "dataset_metric_configs" in value:
        import capo_bedrock.types.evaluation_dataset_metric_configs

        out["dataset_metric_configs"] = (
            capo_bedrock.types.evaluation_dataset_metric_configs.redact_sensitive(
                value["dataset_metric_configs"]
            )
        )
    return out
