"""Generated from Smithy shape ``com.amazonaws.iotsecuretunneling#CloseTunnelRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotsecuretunneling.types.delete_flag
    import capo_iotsecuretunneling.types.tunnel_id


class CloseTunnelRequest(TypedDict, closed=True):
    tunnel_id: "capo_iotsecuretunneling.types.tunnel_id.TunnelId"
    """<p>The ID of the tunnel to close.</p>"""
    delete: NotRequired["capo_iotsecuretunneling.types.delete_flag.DeleteFlag"]
    """<p>When set to true, IoT Secure Tunneling deletes the tunnel data immediately.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CloseTunnelRequest) -> dict:
    out: dict = {}
    out["tunnelId"] = value["tunnel_id"]
    if "delete" in value:
        out["delete"] = value["delete"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CloseTunnelRequest:
    out: CloseTunnelRequest = {}  # type: ignore[typeddict-item]
    if data.get("tunnelId") is not None:
        out["tunnel_id"] = data["tunnelId"]
    else:
        out["tunnel_id"] = ""
    if data.get("delete") is not None:
        out["delete"] = data["delete"]
    return out
