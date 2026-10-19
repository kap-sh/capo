"""Generated from Smithy shape ``com.amazonaws.iotsecuretunneling#DescribeTunnelRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iotsecuretunneling.types.tunnel_id


class DescribeTunnelRequest(TypedDict, closed=True):
    tunnel_id: "capo_iotsecuretunneling.types.tunnel_id.TunnelId"
    """<p>The tunnel to describe.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeTunnelRequest) -> dict:
    out: dict = {}
    out["tunnelId"] = value["tunnel_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeTunnelRequest:
    out: DescribeTunnelRequest = {}  # type: ignore[typeddict-item]
    if data.get("tunnelId") is not None:
        out["tunnel_id"] = data["tunnelId"]
    else:
        out["tunnel_id"] = ""
    return out
