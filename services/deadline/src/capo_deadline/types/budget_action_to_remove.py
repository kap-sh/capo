"""Generated from Smithy shape ``com.amazonaws.deadline#BudgetActionToRemove``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.budget_action_type
    import capo_deadline.types.threshold_percentage


class BudgetActionToRemove(TypedDict, closed=True):
    type: "capo_deadline.types.budget_action_type.BudgetActionType"
    """The type of budget action to remove."""
    threshold_percentage: "capo_deadline.types.threshold_percentage.ThresholdPercentage"
    """The percentage threshold for the budget action to remove."""


# --- restJson1 ser/de ---
def serialize_json(value: BudgetActionToRemove) -> dict:
    out: dict = {}
    import capo_deadline.types.budget_action_type

    out["type"] = capo_deadline.types.budget_action_type.serialize_json(value["type"])
    out["thresholdPercentage"] = (
        "NaN"
        if value["threshold_percentage"] != value["threshold_percentage"]
        else "Infinity"
        if value["threshold_percentage"] == float("inf")
        else "-Infinity"
        if value["threshold_percentage"] == float("-inf")
        else value["threshold_percentage"]
    )
    return out


def deserialize_json(data: dict) -> BudgetActionToRemove:
    out: BudgetActionToRemove = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        import capo_deadline.types.budget_action_type

        out["type"] = capo_deadline.types.budget_action_type.deserialize_json(
            data["type"]
        )
    else:
        import typing

        out["type"] = typing.cast(
            "capo_deadline.types.budget_action_type.BudgetActionType", ""
        )
    if data.get("thresholdPercentage") is not None:
        out["threshold_percentage"] = float(data["thresholdPercentage"])
    else:
        out["threshold_percentage"] = 0.0
    return out
