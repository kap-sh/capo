"""Generated from Smithy shape ``com.amazonaws.wafv2#RevenuePathStatistics``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_wafv2.types.monetization_amount_value
    import capo_wafv2.types.path_string
    import capo_wafv2.types.percentage_value
    import capo_wafv2.types.request_count


class RevenuePathStatistics(TypedDict, closed=True):
    path: "capo_wafv2.types.path_string.PathString"
    """<p>The URI path.</p>"""
    percentage: "capo_wafv2.types.percentage_value.PercentageValue"
    """<p>The percentage of total revenue from this path.</p>"""
    amount: "capo_wafv2.types.monetization_amount_value.MonetizationAmountValue"
    """<p>The total revenue amount from this path in the specified currency.</p>"""
    request_count: "capo_wafv2.types.request_count.RequestCount"
    """<p>The number of monetized requests to this path.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RevenuePathStatistics) -> dict:
    out: dict = {}
    out["Path"] = value["path"]
    out["Percentage"] = (
        "NaN"
        if value.get("percentage", 0) != value.get("percentage", 0)
        else "Infinity"
        if value.get("percentage", 0) == float("inf")
        else "-Infinity"
        if value.get("percentage", 0) == float("-inf")
        else value.get("percentage", 0)
    )
    out["Amount"] = value["amount"]
    out["RequestCount"] = value.get("request_count", 0)
    return out


def deserialize_aws_json_1_1(data: dict) -> RevenuePathStatistics:
    out: RevenuePathStatistics = {}  # type: ignore[typeddict-item]
    if data.get("Path") is not None:
        out["path"] = data["Path"]
    else:
        out["path"] = ""
    if data.get("Percentage") is not None:
        out["percentage"] = float(data["Percentage"])
    else:
        out["percentage"] = 0
    if data.get("Amount") is not None:
        out["amount"] = data["Amount"]
    else:
        out["amount"] = ""
    if data.get("RequestCount") is not None:
        out["request_count"] = data["RequestCount"]
    else:
        out["request_count"] = 0
    return out
