"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#InferenceConnectorSource``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.inference_connector_id


class InferenceConnectorSource(TypedDict, closed=True):
    connector_id: "capo_bedrock_agentcore_control.types.inference_connector_id.InferenceConnectorId"
    """<p>The identifier for the inference connector (for example, <code>bedrock-mantle</code>, <code>openai</code>, or <code>anthropic</code>).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InferenceConnectorSource) -> dict:
    out: dict = {}
    out["connectorId"] = value["connector_id"]
    return out


def deserialize_json(data: dict) -> InferenceConnectorSource:
    out: InferenceConnectorSource = {}  # type: ignore[typeddict-item]
    if data.get("connectorId") is not None:
        out["connector_id"] = data["connectorId"]
    else:
        out["connector_id"] = ""
    return out
