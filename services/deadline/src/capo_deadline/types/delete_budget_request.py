"""Generated from Smithy shape ``com.amazonaws.deadline#DeleteBudgetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.budget_id
    import capo_deadline.types.farm_id


class DeleteBudgetRequest(TypedDict, closed=True):
    farm_id: "capo_deadline.types.farm_id.FarmId"
    """The farm ID of the farm to remove from the budget."""
    budget_id: "capo_deadline.types.budget_id.BudgetId"
    """The budget ID of the budget to delete."""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteBudgetRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteBudgetRequest:
    out: DeleteBudgetRequest = {}  # type: ignore[typeddict-item]
    return out
