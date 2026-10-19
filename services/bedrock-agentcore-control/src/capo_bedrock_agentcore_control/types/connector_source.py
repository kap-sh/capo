"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ConnectorSource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.connector_id
    import capo_bedrock_agentcore_control.types.connector_version


class ConnectorSource(TypedDict, closed=True):
    connector_id: "capo_bedrock_agentcore_control.types.connector_id.ConnectorId"
    """<p>The identifier for the connector integration (for example, <code>bedrock-knowledge-bases</code>).</p>"""
    version: NotRequired[
        "capo_bedrock_agentcore_control.types.connector_version.ConnectorVersion"
    ]
    """<p>The version of the connector to use (for example, <code>1.1.0</code>). If you don't specify a version, the service uses the latest available version.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConnectorSource) -> dict:
    out: dict = {}
    out["connectorId"] = value["connector_id"]
    if "version" in value:
        out["version"] = value["version"]
    return out


def deserialize_json(data: dict) -> ConnectorSource:
    out: ConnectorSource = {}  # type: ignore[typeddict-item]
    if data.get("connectorId") is not None:
        out["connector_id"] = data["connectorId"]
    else:
        out["connector_id"] = ""
    if data.get("version") is not None:
        out["version"] = data["version"]
    return out
