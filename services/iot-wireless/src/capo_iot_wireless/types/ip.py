"""Generated from Smithy shape ``com.amazonaws.iotwireless#Ip``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iot_wireless.types.ip_address


class Ip(TypedDict, closed=True):
    ip_address: "capo_iot_wireless.types.ip_address.IPAddress"
    """<p>IP address information.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Ip) -> dict:
    out: dict = {}
    out["IpAddress"] = value["ip_address"]
    return out


def deserialize_json(data: dict) -> Ip:
    out: Ip = {}  # type: ignore[typeddict-item]
    if data.get("IpAddress") is not None:
        out["ip_address"] = data["IpAddress"]
    else:
        out["ip_address"] = ""
    return out
