"""Generated from Smithy shape ``com.amazonaws.mediaconnect#MergeRouterInputIndexedStreamDetails``."""

from typing_extensions import NotRequired, TypedDict


class MergeRouterInputIndexedStreamDetails(TypedDict, closed=True):
    source_index: "int"
    """<p>The index number (0 or 1) assigned to this source in the merge configuration.</p>"""
    source_ip_address: NotRequired["str"]
    """<p>The IP address of the source for this indexed stream in the merge setup.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MergeRouterInputIndexedStreamDetails) -> dict:
    out: dict = {}
    out["sourceIndex"] = value["source_index"]
    if "source_ip_address" in value:
        out["sourceIpAddress"] = value["source_ip_address"]
    return out


def deserialize_json(data: dict) -> MergeRouterInputIndexedStreamDetails:
    out: MergeRouterInputIndexedStreamDetails = {}  # type: ignore[typeddict-item]
    if data.get("sourceIndex") is not None:
        out["source_index"] = data["sourceIndex"]
    else:
        out["source_index"] = 0
    if data.get("sourceIpAddress") is not None:
        out["source_ip_address"] = data["sourceIpAddress"]
    return out
