"""Generated from Smithy shape ``com.amazonaws.deadline#BudgetActionToAdd``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.budget_action_type
    import capo_deadline.types.description
    import capo_deadline.types.threshold_percentage


class BudgetActionToAdd(TypedDict, closed=True):
    type: "capo_deadline.types.budget_action_type.BudgetActionType"
    """<p>The type of budget action to add.</p>"""
    threshold_percentage: "capo_deadline.types.threshold_percentage.ThresholdPercentage"
    """<p>The percentage threshold for the budget action to add.</p>"""
    description: NotRequired["capo_deadline.types.description.Description"]
    """<p>A description for the budget action to add.</p> <important> <p>This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.</p> </important>"""


# --- restJson1 ser/de ---
def serialize_json(value: BudgetActionToAdd) -> dict:
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
    if "description" in value:
        out["description"] = value["description"]
    return out


def deserialize_json(data: dict) -> BudgetActionToAdd:
    out: BudgetActionToAdd = {}  # type: ignore[typeddict-item]
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
    if data.get("description") is not None:
        out["description"] = data["description"]
    return out


def redact_sensitive(value: BudgetActionToAdd) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    return out
