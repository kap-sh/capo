"""Generated from Smithy shape ``com.amazonaws.location#WiFiAccessPoint``."""

from typing_extensions import TypedDict


class WiFiAccessPoint(TypedDict, closed=True):
    mac_address: "str"
    """<p>Medium access control address (Mac).</p>"""
    rss: "int"
    """<p>Received signal strength (dBm) of the WLAN measurement data.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WiFiAccessPoint) -> dict:
    out: dict = {}
    out["MacAddress"] = value["mac_address"]
    out["Rss"] = value["rss"]
    return out


def deserialize_json(data: dict) -> WiFiAccessPoint:
    out: WiFiAccessPoint = {}  # type: ignore[typeddict-item]
    if data.get("MacAddress") is not None:
        out["mac_address"] = data["MacAddress"]
    else:
        out["mac_address"] = ""
    if data.get("Rss") is not None:
        out["rss"] = data["Rss"]
    else:
        out["rss"] = 0
    return out
