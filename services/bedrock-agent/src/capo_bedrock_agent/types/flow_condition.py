"""Generated from Smithy shape ``com.amazonaws.bedrockagent#FlowCondition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agent.types.flow_condition_expression
    import capo_bedrock_agent.types.flow_condition_name


class FlowCondition(TypedDict, closed=True):
    name: "capo_bedrock_agent.types.flow_condition_name.FlowConditionName"
    """<p>A name for the condition that you can reference.</p>"""
    expression: NotRequired[
        "capo_bedrock_agent.types.flow_condition_expression.FlowConditionExpression"
    ]
    """<p>Defines the condition. You must refer to at least one of the inputs in the condition. For more information, expand the Condition node section in <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/flows-how-it-works.html#flows-nodes">Node types in prompt flows</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FlowCondition) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "expression" in value:
        out["expression"] = value["expression"]
    return out


def deserialize_json(data: dict) -> FlowCondition:
    out: FlowCondition = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("FlowCondition.name required")
    if data.get("expression") is not None:
        out["expression"] = data["expression"]
    return out
