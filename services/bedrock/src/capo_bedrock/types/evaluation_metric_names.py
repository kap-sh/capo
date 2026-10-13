"""Generated from Smithy shape ``com.amazonaws.bedrock#EvaluationMetricNames``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock.types.evaluation_metric_name

EvaluationMetricNames: TypeAlias = list[
    "capo_bedrock.types.evaluation_metric_name.EvaluationMetricName"
]


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationMetricNames) -> list:
    return list(value)


def deserialize_json(data: list) -> EvaluationMetricNames:
    return [item for item in data if item is not None]


def redact_sensitive(value: EvaluationMetricNames) -> list[Any]:
    return ["*** Sensitive Data Redacted ***"] * len(value)
