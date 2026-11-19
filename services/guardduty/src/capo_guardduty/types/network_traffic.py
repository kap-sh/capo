"""Generated from Smithy shape ``com.amazonaws.guardduty#NetworkTraffic``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.count


class NetworkTraffic(TypedDict, closed=True):
    bytes_sent: NotRequired["capo_guardduty.types.count.Count"]
    """<p>The number of bytes sent.</p>"""
    bytes_received: NotRequired["capo_guardduty.types.count.Count"]
    """<p>The number of bytes received.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NetworkTraffic) -> dict:
    out: dict = {}
    if "bytes_sent" in value:
        out["bytesSent"] = value["bytes_sent"]
    if "bytes_received" in value:
        out["bytesReceived"] = value["bytes_received"]
    return out


def deserialize_json(data: dict) -> NetworkTraffic:
    out: NetworkTraffic = {}  # type: ignore[typeddict-item]
    if data.get("bytesSent") is not None:
        out["bytes_sent"] = data["bytesSent"]
    if data.get("bytesReceived") is not None:
        out["bytes_received"] = data["bytesReceived"]
    return out
