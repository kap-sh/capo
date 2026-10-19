"""Generated from Smithy shape ``com.amazonaws.sesv2#PutDedicatedIpWarmupAttributesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_sesv2.types.ip
    import capo_sesv2.types.percentage100_wrapper


class PutDedicatedIpWarmupAttributesRequest(TypedDict, closed=True):
    ip: "capo_sesv2.types.ip.Ip"
    """<p>The dedicated IP address that you want to update the warm-up attributes for.</p>"""
    warmup_percentage: "capo_sesv2.types.percentage100_wrapper.Percentage100Wrapper"
    """<p>The warm-up percentage that you want to associate with the dedicated IP address.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutDedicatedIpWarmupAttributesRequest) -> dict:
    out: dict = {}
    out["WarmupPercentage"] = value["warmup_percentage"]
    return out


def deserialize_json(data: dict) -> PutDedicatedIpWarmupAttributesRequest:
    out: PutDedicatedIpWarmupAttributesRequest = {}  # type: ignore[typeddict-item]
    if data.get("WarmupPercentage") is not None:
        out["warmup_percentage"] = data["WarmupPercentage"]
    else:
        out["warmup_percentage"] = 0
    return out
