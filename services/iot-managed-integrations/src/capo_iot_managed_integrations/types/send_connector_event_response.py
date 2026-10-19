"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#SendConnectorEventResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iot_managed_integrations.types.connector_id


class SendConnectorEventResponse(TypedDict, closed=True):
    connector_id: "capo_iot_managed_integrations.types.connector_id.ConnectorId"
    """<p>The id of the connector between the third-party cloud provider and IoT managed integrations.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SendConnectorEventResponse) -> dict:
    out: dict = {}
    out["ConnectorId"] = value["connector_id"]
    return out


def deserialize_json(data: dict) -> SendConnectorEventResponse:
    out: SendConnectorEventResponse = {}  # type: ignore[typeddict-item]
    if data.get("ConnectorId") is not None:
        out["connector_id"] = data["ConnectorId"]
    else:
        out["connector_id"] = ""
    return out
