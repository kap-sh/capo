"""Generated from Smithy shape ``com.amazonaws.deadline#ResponseBudgetAction``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_deadline.errors import DeserializationError

if TYPE_CHECKING:
    import capo_deadline.types.budget_action_type
    import capo_deadline.types.description
    import capo_deadline.types.threshold_percentage


class ResponseBudgetAction(TypedDict, closed=True):
    type: "capo_deadline.types.budget_action_type.BudgetActionType"
    """<p>The action taken on the budget once scheduling stops.</p>"""
    threshold_percentage: "capo_deadline.types.threshold_percentage.ThresholdPercentage"
    """<p>The percentage threshold for the budget.</p>"""
    description: NotRequired["capo_deadline.types.description.Description"]
    """<p>The budget action description.</p> <important> <p>This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.</p> </important>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResponseBudgetAction) -> dict:
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


def deserialize_json(data: dict) -> ResponseBudgetAction:
    out: ResponseBudgetAction = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        import capo_deadline.types.budget_action_type

        out["type"] = capo_deadline.types.budget_action_type.deserialize_json(
            data["type"]
        )
    else:
        raise DeserializationError("ResponseBudgetAction.type required")
    if data.get("thresholdPercentage") is not None:
        out["threshold_percentage"] = float(data["thresholdPercentage"])
    else:
        raise DeserializationError("ResponseBudgetAction.threshold_percentage required")
    if data.get("description") is not None:
        out["description"] = data["description"]
    return out


def redact_sensitive(value: ResponseBudgetAction) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    return out
