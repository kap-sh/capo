"""Generated from Smithy shape ``com.amazonaws.trustedadvisor#RecommendationCostOptimizingAggregates``."""

from typing_extensions import TypedDict


class RecommendationCostOptimizingAggregates(TypedDict, closed=True):
    estimated_monthly_savings: "float"
    """<p>The estimated monthly savings</p>"""
    estimated_percent_monthly_savings: "float"
    """<p>The estimated percently monthly savings</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RecommendationCostOptimizingAggregates) -> dict:
    out: dict = {}
    out["estimatedMonthlySavings"] = (
        "NaN"
        if value["estimated_monthly_savings"] != value["estimated_monthly_savings"]
        else "Infinity"
        if value["estimated_monthly_savings"] == float("inf")
        else "-Infinity"
        if value["estimated_monthly_savings"] == float("-inf")
        else value["estimated_monthly_savings"]
    )
    out["estimatedPercentMonthlySavings"] = (
        "NaN"
        if value["estimated_percent_monthly_savings"]
        != value["estimated_percent_monthly_savings"]
        else "Infinity"
        if value["estimated_percent_monthly_savings"] == float("inf")
        else "-Infinity"
        if value["estimated_percent_monthly_savings"] == float("-inf")
        else value["estimated_percent_monthly_savings"]
    )
    return out


def deserialize_json(data: dict) -> RecommendationCostOptimizingAggregates:
    out: RecommendationCostOptimizingAggregates = {}  # type: ignore[typeddict-item]
    if data.get("estimatedMonthlySavings") is not None:
        out["estimated_monthly_savings"] = float(data["estimatedMonthlySavings"])
    else:
        out["estimated_monthly_savings"] = 0.0
    if data.get("estimatedPercentMonthlySavings") is not None:
        out["estimated_percent_monthly_savings"] = float(
            data["estimatedPercentMonthlySavings"]
        )
    else:
        out["estimated_percent_monthly_savings"] = 0.0
    return out
