"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#HttpConnectorSource``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.connector_id


class HttpConnectorSource(TypedDict, closed=True):
    connector_id: "capo_bedrock_agentcore_control.types.connector_id.ConnectorId"
    """<p>The identifier for the HTTP connector integration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HttpConnectorSource) -> dict:
    out: dict = {}
    out["connectorId"] = value["connector_id"]
    return out


def deserialize_json(data: dict) -> HttpConnectorSource:
    out: HttpConnectorSource = {}  # type: ignore[typeddict-item]
    if data.get("connectorId") is not None:
        out["connector_id"] = data["connectorId"]
    else:
        out["connector_id"] = ""
    return out
