"""Generated from Smithy shape ``com.amazonaws.connect#EvaluationFormScoreThreshold``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connect.types.evaluation_score_percentage
    import capo_connect.types.performance_category_name


class EvaluationFormScoreThreshold(TypedDict, closed=True):
    performance_category: (
        "capo_connect.types.performance_category_name.PerformanceCategoryName"
    )
    """<p>The performance category name.</p>"""
    min_score_percentage: (
        "capo_connect.types.evaluation_score_percentage.EvaluationScorePercentage"
    )
    """<p>The minimum score percentage for the performance category.</p>"""
    max_score_percentage: (
        "capo_connect.types.evaluation_score_percentage.EvaluationScorePercentage"
    )
    """<p>The maximum score percentage for the performance category.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationFormScoreThreshold) -> dict:
    out: dict = {}
    import capo_connect.types.performance_category_name

    out["PerformanceCategory"] = (
        capo_connect.types.performance_category_name.serialize_json(
            value["performance_category"]
        )
    )
    out["MinScorePercentage"] = (
        "NaN"
        if value.get("min_score_percentage", 0) != value.get("min_score_percentage", 0)
        else "Infinity"
        if value.get("min_score_percentage", 0) == float("inf")
        else "-Infinity"
        if value.get("min_score_percentage", 0) == float("-inf")
        else value.get("min_score_percentage", 0)
    )
    out["MaxScorePercentage"] = (
        "NaN"
        if value.get("max_score_percentage", 0) != value.get("max_score_percentage", 0)
        else "Infinity"
        if value.get("max_score_percentage", 0) == float("inf")
        else "-Infinity"
        if value.get("max_score_percentage", 0) == float("-inf")
        else value.get("max_score_percentage", 0)
    )
    return out


def deserialize_json(data: dict) -> EvaluationFormScoreThreshold:
    out: EvaluationFormScoreThreshold = {}  # type: ignore[typeddict-item]
    if data.get("PerformanceCategory") is not None:
        import capo_connect.types.performance_category_name

        out["performance_category"] = (
            capo_connect.types.performance_category_name.deserialize_json(
                data["PerformanceCategory"]
            )
        )
    else:
        import typing

        out["performance_category"] = typing.cast(
            "capo_connect.types.performance_category_name.PerformanceCategoryName", ""
        )
    if data.get("MinScorePercentage") is not None:
        out["min_score_percentage"] = float(data["MinScorePercentage"])
    else:
        out["min_score_percentage"] = 0
    if data.get("MaxScorePercentage") is not None:
        out["max_score_percentage"] = float(data["MaxScorePercentage"])
    else:
        out["max_score_percentage"] = 0
    return out
