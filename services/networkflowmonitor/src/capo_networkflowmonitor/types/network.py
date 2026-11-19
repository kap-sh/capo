"""Generated from Smithy shape ``com.amazonaws.networkflowmonitor#Network``."""

from typing_extensions import NotRequired, TypedDict


class Network(TypedDict, closed=True):
    as_name: NotRequired["str"]
    """<p>The name of the autonomous system that the network belongs to.</p>"""
    as_number: NotRequired["int"]
    """<p>The autonomous system number (ASN) of the autonomous system that the network belongs to.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Network) -> dict:
    out: dict = {}
    if "as_name" in value:
        out["asName"] = value["as_name"]
    if "as_number" in value:
        out["asNumber"] = value["as_number"]
    return out


def deserialize_json(data: dict) -> Network:
    out: Network = {}  # type: ignore[typeddict-item]
    if data.get("asName") is not None:
        out["as_name"] = data["asName"]
    if data.get("asNumber") is not None:
        out["as_number"] = data["asNumber"]
    return out
