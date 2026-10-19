"""Generated from Smithy shape ``com.amazonaws.cleanrooms#DifferentialPrivacyPrivacyBudgetAggregation``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cleanrooms.types.differential_privacy_aggregation_type


class DifferentialPrivacyPrivacyBudgetAggregation(TypedDict, closed=True):
    type: "capo_cleanrooms.types.differential_privacy_aggregation_type.DifferentialPrivacyAggregationType"
    """<p>The different types of aggregation functions that you can perform.</p>"""
    max_count: "int"
    """<p>The maximum number of aggregation functions that you can perform with the given privacy budget.</p>"""
    remaining_count: "int"
    """<p>The remaining number of aggregation functions that can be run with the available privacy budget.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DifferentialPrivacyPrivacyBudgetAggregation) -> dict:
    out: dict = {}
    import capo_cleanrooms.types.differential_privacy_aggregation_type

    out["type"] = (
        capo_cleanrooms.types.differential_privacy_aggregation_type.serialize_json(
            value["type"]
        )
    )
    out["maxCount"] = value["max_count"]
    out["remainingCount"] = value["remaining_count"]
    return out


def deserialize_json(data: dict) -> DifferentialPrivacyPrivacyBudgetAggregation:
    out: DifferentialPrivacyPrivacyBudgetAggregation = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        import capo_cleanrooms.types.differential_privacy_aggregation_type

        out["type"] = (
            capo_cleanrooms.types.differential_privacy_aggregation_type.deserialize_json(
                data["type"]
            )
        )
    else:
        import typing

        out["type"] = typing.cast(
            "capo_cleanrooms.types.differential_privacy_aggregation_type.DifferentialPrivacyAggregationType",
            "",
        )
    if data.get("maxCount") is not None:
        out["max_count"] = data["maxCount"]
    else:
        out["max_count"] = 0
    if data.get("remainingCount") is not None:
        out["remaining_count"] = data["remainingCount"]
    else:
        out["remaining_count"] = 0
    return out
