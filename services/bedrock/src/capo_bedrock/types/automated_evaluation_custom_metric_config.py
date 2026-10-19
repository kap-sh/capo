"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedEvaluationCustomMetricConfig``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock.types.automated_evaluation_custom_metrics
    import capo_bedrock.types.custom_metric_evaluator_model_config


class AutomatedEvaluationCustomMetricConfig(TypedDict, closed=True):
    custom_metrics: "capo_bedrock.types.automated_evaluation_custom_metrics.AutomatedEvaluationCustomMetrics"
    """<p>Defines a list of custom metrics to be used in an Amazon Bedrock evaluation job.</p>"""
    evaluator_model_config: "capo_bedrock.types.custom_metric_evaluator_model_config.CustomMetricEvaluatorModelConfig"
    """<p>Configuration of the evaluator model you want to use to evaluate custom metrics in an Amazon Bedrock evaluation job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedEvaluationCustomMetricConfig) -> dict:
    out: dict = {}
    import capo_bedrock.types.automated_evaluation_custom_metrics

    out["customMetrics"] = (
        capo_bedrock.types.automated_evaluation_custom_metrics.serialize_json(
            value["custom_metrics"]
        )
    )
    import capo_bedrock.types.custom_metric_evaluator_model_config

    out["evaluatorModelConfig"] = (
        capo_bedrock.types.custom_metric_evaluator_model_config.serialize_json(
            value["evaluator_model_config"]
        )
    )
    return out


def deserialize_json(data: dict) -> AutomatedEvaluationCustomMetricConfig:
    out: AutomatedEvaluationCustomMetricConfig = {}  # type: ignore[typeddict-item]
    if data.get("customMetrics") is not None:
        import capo_bedrock.types.automated_evaluation_custom_metrics

        out["custom_metrics"] = (
            capo_bedrock.types.automated_evaluation_custom_metrics.deserialize_json(
                data["customMetrics"]
            )
        )
    else:
        out["custom_metrics"] = []
    if data.get("evaluatorModelConfig") is not None:
        import capo_bedrock.types.custom_metric_evaluator_model_config

        out["evaluator_model_config"] = (
            capo_bedrock.types.custom_metric_evaluator_model_config.deserialize_json(
                data["evaluatorModelConfig"]
            )
        )
    else:
        raise DeserializationError(
            "AutomatedEvaluationCustomMetricConfig.evaluator_model_config required"
        )
    return out


def redact_sensitive(value: AutomatedEvaluationCustomMetricConfig) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "custom_metrics" in value:
        import capo_bedrock.types.automated_evaluation_custom_metrics

        out["custom_metrics"] = (
            capo_bedrock.types.automated_evaluation_custom_metrics.redact_sensitive(
                value["custom_metrics"]
            )
        )
    return out
