"""Generated from Smithy shape ``com.amazonaws.customerprofiles#GetObjectTypeAttributeStatisticsPercentiles``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_customer_profiles.types.double


class GetObjectTypeAttributeStatisticsPercentiles(TypedDict, closed=True):
    p5: "capo_customer_profiles.types.double.Double"
    """<p>The 5th percentile value of the attribute.</p>"""
    p25: "capo_customer_profiles.types.double.Double"
    """<p>The 25th percentile value of the attribute.</p>"""
    p50: "capo_customer_profiles.types.double.Double"
    """<p>The 50th percentile (median) value of the attribute.</p>"""
    p75: "capo_customer_profiles.types.double.Double"
    """<p>The 75th percentile value of the attribute.</p>"""
    p95: "capo_customer_profiles.types.double.Double"
    """<p>The 95th percentile value of the attribute.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetObjectTypeAttributeStatisticsPercentiles) -> dict:
    out: dict = {}
    out["P5"] = (
        "NaN"
        if value["p5"] != value["p5"]
        else "Infinity"
        if value["p5"] == float("inf")
        else "-Infinity"
        if value["p5"] == float("-inf")
        else value["p5"]
    )
    out["P25"] = (
        "NaN"
        if value["p25"] != value["p25"]
        else "Infinity"
        if value["p25"] == float("inf")
        else "-Infinity"
        if value["p25"] == float("-inf")
        else value["p25"]
    )
    out["P50"] = (
        "NaN"
        if value["p50"] != value["p50"]
        else "Infinity"
        if value["p50"] == float("inf")
        else "-Infinity"
        if value["p50"] == float("-inf")
        else value["p50"]
    )
    out["P75"] = (
        "NaN"
        if value["p75"] != value["p75"]
        else "Infinity"
        if value["p75"] == float("inf")
        else "-Infinity"
        if value["p75"] == float("-inf")
        else value["p75"]
    )
    out["P95"] = (
        "NaN"
        if value["p95"] != value["p95"]
        else "Infinity"
        if value["p95"] == float("inf")
        else "-Infinity"
        if value["p95"] == float("-inf")
        else value["p95"]
    )
    return out


def deserialize_json(data: dict) -> GetObjectTypeAttributeStatisticsPercentiles:
    out: GetObjectTypeAttributeStatisticsPercentiles = {}  # type: ignore[typeddict-item]
    if data.get("P5") is not None:
        out["p5"] = float(data["P5"])
    else:
        out["p5"] = 0.0
    if data.get("P25") is not None:
        out["p25"] = float(data["P25"])
    else:
        out["p25"] = 0.0
    if data.get("P50") is not None:
        out["p50"] = float(data["P50"])
    else:
        out["p50"] = 0.0
    if data.get("P75") is not None:
        out["p75"] = float(data["P75"])
    else:
        out["p75"] = 0.0
    if data.get("P95") is not None:
        out["p95"] = float(data["P95"])
    else:
        out["p95"] = 0.0
    return out
