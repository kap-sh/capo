"""Generated from Smithy shape ``com.amazonaws.bedrockagent#FlowConditionalConnectionConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agent.types.flow_condition_name


class FlowConditionalConnectionConfiguration(TypedDict, closed=True):
    condition: "capo_bedrock_agent.types.flow_condition_name.FlowConditionName"
    """<p>The condition that triggers this connection. For more information about how to write conditions, see the <b>Condition</b> node type in the <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/node-types.html">Node types</a> topic in the Amazon Bedrock User Guide.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FlowConditionalConnectionConfiguration) -> dict:
    out: dict = {}
    out["condition"] = value["condition"]
    return out


def deserialize_json(data: dict) -> FlowConditionalConnectionConfiguration:
    out: FlowConditionalConnectionConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("condition") is not None:
        out["condition"] = data["condition"]
    else:
        raise DeserializationError(
            "FlowConditionalConnectionConfiguration.condition required"
        )
    return out
