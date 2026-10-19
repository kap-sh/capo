"""Generated from Smithy shape ``com.amazonaws.internetmonitor#Network``."""

from typing_extensions import TypedDict


class Network(TypedDict, closed=True):
    as_name: "str"
    """<p>The name of the internet service provider (ISP) or network (ASN).</p>"""
    as_number: "int"
    """<p>The Autonomous System Number (ASN) of the internet provider or network.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Network) -> dict:
    out: dict = {}
    out["ASName"] = value["as_name"]
    out["ASNumber"] = value["as_number"]
    return out


def deserialize_json(data: dict) -> Network:
    out: Network = {}  # type: ignore[typeddict-item]
    if data.get("ASName") is not None:
        out["as_name"] = data["ASName"]
    else:
        out["as_name"] = ""
    if data.get("ASNumber") is not None:
        out["as_number"] = data["ASNumber"]
    else:
        out["as_number"] = 0
    return out
