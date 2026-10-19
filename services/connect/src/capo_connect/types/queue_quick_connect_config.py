"""Generated from Smithy shape ``com.amazonaws.connect#QueueQuickConnectConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connect.types.contact_flow_id
    import capo_connect.types.queue_id


class QueueQuickConnectConfig(TypedDict, closed=True):
    queue_id: "capo_connect.types.queue_id.QueueId"
    """<p>The identifier for the queue.</p>"""
    contact_flow_id: "capo_connect.types.contact_flow_id.ContactFlowId"
    """<p>The identifier of the flow.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: QueueQuickConnectConfig) -> dict:
    out: dict = {}
    out["QueueId"] = value["queue_id"]
    out["ContactFlowId"] = value["contact_flow_id"]
    return out


def deserialize_json(data: dict) -> QueueQuickConnectConfig:
    out: QueueQuickConnectConfig = {}  # type: ignore[typeddict-item]
    if data.get("QueueId") is not None:
        out["queue_id"] = data["QueueId"]
    else:
        out["queue_id"] = ""
    if data.get("ContactFlowId") is not None:
        out["contact_flow_id"] = data["ContactFlowId"]
    else:
        out["contact_flow_id"] = ""
    return out
