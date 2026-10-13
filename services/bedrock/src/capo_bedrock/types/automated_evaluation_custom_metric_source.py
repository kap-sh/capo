"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedEvaluationCustomMetricSource``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_bedrock.types.custom_metric_definition


class _AutomatedEvaluationCustomMetricSource_customMetricDefinition(
    TypedDict, closed=True
):
    customMetricDefinition: (
        "capo_bedrock.types.custom_metric_definition.CustomMetricDefinition"
    )


AutomatedEvaluationCustomMetricSource: TypeAlias = (
    _AutomatedEvaluationCustomMetricSource_customMetricDefinition
)


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedEvaluationCustomMetricSource) -> dict:
    if "customMetricDefinition" in value:
        import capo_bedrock.types.custom_metric_definition

        return {
            "customMetricDefinition": capo_bedrock.types.custom_metric_definition.serialize_json(
                value["customMetricDefinition"]
            )
        }
    else:
        raise SerializationError(
            "AutomatedEvaluationCustomMetricSource: no variant present"
        )


def deserialize_json(data: dict) -> AutomatedEvaluationCustomMetricSource:
    if data.get("customMetricDefinition") is not None:
        import capo_bedrock.types.custom_metric_definition

        return {
            "customMetricDefinition": capo_bedrock.types.custom_metric_definition.deserialize_json(
                data["customMetricDefinition"]
            )
        }
    else:
        raise DeserializationError(
            "AutomatedEvaluationCustomMetricSource: no recognized variant key"
        )


def redact_sensitive(value: AutomatedEvaluationCustomMetricSource) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "customMetricDefinition" in value:
        out["customMetricDefinition"] = "*** Sensitive Data Redacted ***"
    return out
