"""Generated from Smithy shape ``com.amazonaws.bedrockagent#UnsatisfiedConnectionConditionsFlowValidationDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent.types.flow_connection_name


class UnsatisfiedConnectionConditionsFlowValidationDetails(TypedDict, closed=True):
    connection: "capo_bedrock_agent.types.flow_connection_name.FlowConnectionName"
    """<p>The name of the connection with unsatisfied conditions.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UnsatisfiedConnectionConditionsFlowValidationDetails) -> dict:
    out: dict = {}
    out["connection"] = value["connection"]
    return out


def deserialize_json(
    data: dict,
) -> UnsatisfiedConnectionConditionsFlowValidationDetails:
    out: UnsatisfiedConnectionConditionsFlowValidationDetails = {}  # type: ignore[typeddict-item]
    if data.get("connection") is not None:
        out["connection"] = data["connection"]
    else:
        out["connection"] = ""
    return out
