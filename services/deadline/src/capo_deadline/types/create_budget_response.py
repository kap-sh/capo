"""Generated from Smithy shape ``com.amazonaws.deadline#CreateBudgetResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.budget_id


class CreateBudgetResponse(TypedDict, closed=True):
    budget_id: "capo_deadline.types.budget_id.BudgetId"
    """The budget ID."""


# --- restJson1 ser/de ---
def serialize_json(value: CreateBudgetResponse) -> dict:
    out: dict = {}
    out["budgetId"] = value["budget_id"]
    return out


def deserialize_json(data: dict) -> CreateBudgetResponse:
    out: CreateBudgetResponse = {}  # type: ignore[typeddict-item]
    if data.get("budgetId") is not None:
        out["budget_id"] = data["budgetId"]
    else:
        out["budget_id"] = ""
    return out
