"""Generated from Smithy shape ``com.amazonaws.bedrockagent#NeptuneAnalyticsConfiguration``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agent.types.graph_arn
    import capo_bedrock_agent.types.neptune_analytics_field_mapping


class NeptuneAnalyticsConfiguration(TypedDict, closed=True):
    graph_arn: "capo_bedrock_agent.types.graph_arn.GraphArn"
    """<p>The Amazon Resource Name (ARN) of the Neptune Analytics vector store.</p>"""
    field_mapping: "capo_bedrock_agent.types.neptune_analytics_field_mapping.NeptuneAnalyticsFieldMapping"
    """<p>Contains the names of the fields to which to map information about the vector store.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NeptuneAnalyticsConfiguration) -> dict:
    out: dict = {}
    out["graphArn"] = value["graph_arn"]
    import capo_bedrock_agent.types.neptune_analytics_field_mapping

    out["fieldMapping"] = (
        capo_bedrock_agent.types.neptune_analytics_field_mapping.serialize_json(
            value["field_mapping"]
        )
    )
    return out


def deserialize_json(data: dict) -> NeptuneAnalyticsConfiguration:
    out: NeptuneAnalyticsConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("graphArn") is not None:
        out["graph_arn"] = data["graphArn"]
    else:
        raise DeserializationError("NeptuneAnalyticsConfiguration.graph_arn required")
    if data.get("fieldMapping") is not None:
        import capo_bedrock_agent.types.neptune_analytics_field_mapping

        out["field_mapping"] = (
            capo_bedrock_agent.types.neptune_analytics_field_mapping.deserialize_json(
                data["fieldMapping"]
            )
        )
    else:
        raise DeserializationError(
            "NeptuneAnalyticsConfiguration.field_mapping required"
        )
    return out


def redact_sensitive(value: NeptuneAnalyticsConfiguration) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "graph_arn" in value:
        out["graph_arn"] = "*** Sensitive Data Redacted ***"
    return out
