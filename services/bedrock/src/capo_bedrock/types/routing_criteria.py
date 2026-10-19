"""Generated from Smithy shape ``com.amazonaws.bedrock#RoutingCriteria``."""

from typing_extensions import TypedDict


class RoutingCriteria(TypedDict, closed=True):
    response_quality_difference: "float"
    """<p>The criteria's response quality difference.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RoutingCriteria) -> dict:
    out: dict = {}
    out["responseQualityDifference"] = (
        "NaN"
        if value["response_quality_difference"] != value["response_quality_difference"]
        else "Infinity"
        if value["response_quality_difference"] == float("inf")
        else "-Infinity"
        if value["response_quality_difference"] == float("-inf")
        else value["response_quality_difference"]
    )
    return out


def deserialize_json(data: dict) -> RoutingCriteria:
    out: RoutingCriteria = {}  # type: ignore[typeddict-item]
    if data.get("responseQualityDifference") is not None:
        out["response_quality_difference"] = float(data["responseQualityDifference"])
    else:
        out["response_quality_difference"] = 0.0
    return out
