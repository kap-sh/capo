"""Generated from Smithy shape ``com.amazonaws.connect#UserQuickConnectConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connect.types.contact_flow_id
    import capo_connect.types.user_id


class UserQuickConnectConfig(TypedDict, closed=True):
    user_id: "capo_connect.types.user_id.UserId"
    """<p>The identifier of the user.</p>"""
    contact_flow_id: "capo_connect.types.contact_flow_id.ContactFlowId"
    """<p>The identifier of the flow.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UserQuickConnectConfig) -> dict:
    out: dict = {}
    out["UserId"] = value["user_id"]
    out["ContactFlowId"] = value["contact_flow_id"]
    return out


def deserialize_json(data: dict) -> UserQuickConnectConfig:
    out: UserQuickConnectConfig = {}  # type: ignore[typeddict-item]
    if data.get("UserId") is not None:
        out["user_id"] = data["UserId"]
    else:
        out["user_id"] = ""
    if data.get("ContactFlowId") is not None:
        out["contact_flow_id"] = data["ContactFlowId"]
    else:
        out["contact_flow_id"] = ""
    return out
