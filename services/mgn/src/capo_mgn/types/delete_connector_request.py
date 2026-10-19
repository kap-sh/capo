"""Generated from Smithy shape ``com.amazonaws.mgn#DeleteConnectorRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_mgn.types.connector_id


class DeleteConnectorRequest(TypedDict, closed=True):
    connector_id: "capo_mgn.types.connector_id.ConnectorID"
    """<p>Delete Connector request connector ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteConnectorRequest) -> dict:
    out: dict = {}
    out["connectorID"] = value["connector_id"]
    return out


def deserialize_json(data: dict) -> DeleteConnectorRequest:
    out: DeleteConnectorRequest = {}  # type: ignore[typeddict-item]
    if data.get("connectorID") is not None:
        out["connector_id"] = data["connectorID"]
    else:
        out["connector_id"] = ""
    return out
