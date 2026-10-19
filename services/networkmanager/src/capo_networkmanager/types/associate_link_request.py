"""Generated from Smithy shape ``com.amazonaws.networkmanager#AssociateLinkRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_networkmanager.types.device_id
    import capo_networkmanager.types.global_network_id
    import capo_networkmanager.types.link_id


class AssociateLinkRequest(TypedDict, closed=True):
    global_network_id: "capo_networkmanager.types.global_network_id.GlobalNetworkId"
    """<p>The ID of the global network.</p>"""
    device_id: "capo_networkmanager.types.device_id.DeviceId"
    """<p>The ID of the device.</p>"""
    link_id: "capo_networkmanager.types.link_id.LinkId"
    """<p>The ID of the link.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssociateLinkRequest) -> dict:
    out: dict = {}
    out["DeviceId"] = value["device_id"]
    out["LinkId"] = value["link_id"]
    return out


def deserialize_json(data: dict) -> AssociateLinkRequest:
    out: AssociateLinkRequest = {}  # type: ignore[typeddict-item]
    if data.get("DeviceId") is not None:
        out["device_id"] = data["DeviceId"]
    else:
        out["device_id"] = ""
    if data.get("LinkId") is not None:
        out["link_id"] = data["LinkId"]
    else:
        out["link_id"] = ""
    return out
