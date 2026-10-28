"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedEvaluationCustomMetricSource``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock.errors import DeserializationError, SerializationError
from capo_bedrock.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_bedrock.types.custom_metric_definition


class AutomatedEvaluationCustomMetricSourceCustomMetricDefinitionMember(
    TypedDict, closed=True
):
    customMetricDefinition: (
        "capo_bedrock.types.custom_metric_definition.CustomMetricDefinition"
    )


AutomatedEvaluationCustomMetricSource: TypeAlias = (
    AutomatedEvaluationCustomMetricSourceCustomMetricDefinitionMember
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedEvaluationCustomMetricSource) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"AutomatedEvaluationCustomMetricSource: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "customMetricDefinition" in value:
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
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError(
            "AutomatedEvaluationCustomMetricSource: no recognized variant key"
        )


def redact_sensitive(value: AutomatedEvaluationCustomMetricSource) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "customMetricDefinition" in value:
        out["customMetricDefinition"] = "*** Sensitive Data Redacted ***"
    return out
