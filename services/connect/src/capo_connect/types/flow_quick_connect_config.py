"""Generated from Smithy shape ``com.amazonaws.connect#FlowQuickConnectConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connect.types.contact_flow_id


class FlowQuickConnectConfig(TypedDict, closed=True):
    contact_flow_id: "capo_connect.types.contact_flow_id.ContactFlowId"
    """<p> The contact flow ID for the quick connect configuration. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FlowQuickConnectConfig) -> dict:
    out: dict = {}
    out["ContactFlowId"] = value["contact_flow_id"]
    return out


def deserialize_json(data: dict) -> FlowQuickConnectConfig:
    out: FlowQuickConnectConfig = {}  # type: ignore[typeddict-item]
    if data.get("ContactFlowId") is not None:
        out["contact_flow_id"] = data["ContactFlowId"]
    else:
        out["contact_flow_id"] = ""
    return out
