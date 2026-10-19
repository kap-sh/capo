"""Generated from Smithy shape ``com.amazonaws.bedrockagent#IncompatibleConnectionDataTypeFlowValidationDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent.types.flow_connection_name


class IncompatibleConnectionDataTypeFlowValidationDetails(TypedDict, closed=True):
    connection: "capo_bedrock_agent.types.flow_connection_name.FlowConnectionName"
    """<p>The name of the connection with incompatible data types.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IncompatibleConnectionDataTypeFlowValidationDetails) -> dict:
    out: dict = {}
    out["connection"] = value["connection"]
    return out


def deserialize_json(data: dict) -> IncompatibleConnectionDataTypeFlowValidationDetails:
    out: IncompatibleConnectionDataTypeFlowValidationDetails = {}  # type: ignore[typeddict-item]
    if data.get("connection") is not None:
        out["connection"] = data["connection"]
    else:
        out["connection"] = ""
    return out
