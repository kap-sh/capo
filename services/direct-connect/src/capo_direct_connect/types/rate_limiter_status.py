"""Generated from Smithy shape ``com.amazonaws.directconnect#RateLimiterStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_direct_connect.types.bandwidth
    import capo_direct_connect.types.count


class RateLimiterStatus(TypedDict, closed=True):
    max_allowed: "capo_direct_connect.types.count.Count"
    """<p>The maximum number of rate limiters allowed on the connection.</p>"""
    in_use: "capo_direct_connect.types.count.Count"
    """<p>The number of rate limiters currently in use on the connection.</p>"""
    remaining: "capo_direct_connect.types.count.Count"
    """<p>The number of rate limiters remaining (available) on the connection.</p>"""
    total_bandwidth: NotRequired["capo_direct_connect.types.bandwidth.Bandwidth"]
    """<p>The total bandwidth allocated across all rate limiters on the connection.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RateLimiterStatus) -> dict:
    out: dict = {}
    out["maxAllowed"] = value.get("max_allowed", 0)
    out["inUse"] = value.get("in_use", 0)
    out["remaining"] = value.get("remaining", 0)
    if "total_bandwidth" in value:
        out["totalBandwidth"] = value["total_bandwidth"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RateLimiterStatus:
    out: RateLimiterStatus = {}  # type: ignore[typeddict-item]
    if data.get("maxAllowed") is not None:
        out["max_allowed"] = data["maxAllowed"]
    else:
        out["max_allowed"] = 0
    if data.get("inUse") is not None:
        out["in_use"] = data["inUse"]
    else:
        out["in_use"] = 0
    if data.get("remaining") is not None:
        out["remaining"] = data["remaining"]
    else:
        out["remaining"] = 0
    if data.get("totalBandwidth") is not None:
        out["total_bandwidth"] = data["totalBandwidth"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: RateLimiterStatus) -> dict:
    out: dict = {}
    out["maxAllowed"] = value.get("max_allowed", 0)
    out["inUse"] = value.get("in_use", 0)
    out["remaining"] = value.get("remaining", 0)
    if "total_bandwidth" in value:
        out["totalBandwidth"] = value["total_bandwidth"]
    return out


def deserialize_cbor(data: dict) -> RateLimiterStatus:
    out: RateLimiterStatus = {}  # type: ignore[typeddict-item]
    if data.get("maxAllowed") is not None:
        out["max_allowed"] = data["maxAllowed"]
    else:
        out["max_allowed"] = 0
    if data.get("inUse") is not None:
        out["in_use"] = data["inUse"]
    else:
        out["in_use"] = 0
    if data.get("remaining") is not None:
        out["remaining"] = data["remaining"]
    else:
        out["remaining"] = 0
    if data.get("totalBandwidth") is not None:
        out["total_bandwidth"] = data["totalBandwidth"]
    return out
