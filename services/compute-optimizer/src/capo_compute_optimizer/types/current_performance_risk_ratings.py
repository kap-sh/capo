"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#CurrentPerformanceRiskRatings``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_compute_optimizer.types.high
    import capo_compute_optimizer.types.low
    import capo_compute_optimizer.types.medium
    import capo_compute_optimizer.types.very_low


class CurrentPerformanceRiskRatings(TypedDict, closed=True):
    high: "capo_compute_optimizer.types.high.High"
    """<p>A count of the applicable resource types with a high performance risk rating.</p>"""
    medium: "capo_compute_optimizer.types.medium.Medium"
    """<p>A count of the applicable resource types with a medium performance risk rating.</p>"""
    low: "capo_compute_optimizer.types.low.Low"
    """<p>A count of the applicable resource types with a low performance risk rating.</p>"""
    very_low: "capo_compute_optimizer.types.very_low.VeryLow"
    """<p>A count of the applicable resource types with a very low performance risk rating.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CurrentPerformanceRiskRatings) -> dict:
    out: dict = {}
    out["high"] = value.get("high", 0)
    out["medium"] = value.get("medium", 0)
    out["low"] = value.get("low", 0)
    out["veryLow"] = value.get("very_low", 0)
    return out


def deserialize_aws_json_1_0(data: dict) -> CurrentPerformanceRiskRatings:
    out: CurrentPerformanceRiskRatings = {}  # type: ignore[typeddict-item]
    if data.get("high") is not None:
        out["high"] = data["high"]
    else:
        out["high"] = 0
    if data.get("medium") is not None:
        out["medium"] = data["medium"]
    else:
        out["medium"] = 0
    if data.get("low") is not None:
        out["low"] = data["low"]
    else:
        out["low"] = 0
    if data.get("veryLow") is not None:
        out["very_low"] = data["veryLow"]
    else:
        out["very_low"] = 0
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CurrentPerformanceRiskRatings) -> dict:
    out: dict = {}
    out["high"] = value.get("high", 0)
    out["medium"] = value.get("medium", 0)
    out["low"] = value.get("low", 0)
    out["veryLow"] = value.get("very_low", 0)
    return out


def deserialize_cbor(data: dict) -> CurrentPerformanceRiskRatings:
    out: CurrentPerformanceRiskRatings = {}  # type: ignore[typeddict-item]
    if data.get("high") is not None:
        out["high"] = data["high"]
    else:
        out["high"] = 0
    if data.get("medium") is not None:
        out["medium"] = data["medium"]
    else:
        out["medium"] = 0
    if data.get("low") is not None:
        out["low"] = data["low"]
    else:
        out["low"] = 0
    if data.get("veryLow") is not None:
        out["very_low"] = data["veryLow"]
    else:
        out["very_low"] = 0
    return out
