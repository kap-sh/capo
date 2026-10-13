"""Generated from Smithy shape ``com.amazonaws.bedrockagent#ConditionFlowNodeConfiguration``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agent.types.flow_conditions


class ConditionFlowNodeConfiguration(TypedDict, closed=True):
    conditions: "capo_bedrock_agent.types.flow_conditions.FlowConditions"
    """<p>An array of conditions. Each member contains the name of a condition and an expression that defines the condition.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConditionFlowNodeConfiguration) -> dict:
    out: dict = {}
    import capo_bedrock_agent.types.flow_conditions

    out["conditions"] = capo_bedrock_agent.types.flow_conditions.serialize_json(
        value["conditions"]
    )
    return out


def deserialize_json(data: dict) -> ConditionFlowNodeConfiguration:
    out: ConditionFlowNodeConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("conditions") is not None:
        import capo_bedrock_agent.types.flow_conditions

        out["conditions"] = capo_bedrock_agent.types.flow_conditions.deserialize_json(
            data["conditions"]
        )
    else:
        raise DeserializationError("ConditionFlowNodeConfiguration.conditions required")
    return out


def redact_sensitive(value: ConditionFlowNodeConfiguration) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "conditions" in value:
        import capo_bedrock_agent.types.flow_conditions

        out["conditions"] = capo_bedrock_agent.types.flow_conditions.redact_sensitive(
            value["conditions"]
        )
    return out
