"""Generated from Smithy shape ``com.amazonaws.deadline#GetBudgetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.budget_id
    import capo_deadline.types.farm_id


class GetBudgetRequest(TypedDict, closed=True):
    farm_id: "capo_deadline.types.farm_id.FarmId"
    """The farm ID of the farm connected to the budget."""
    budget_id: "capo_deadline.types.budget_id.BudgetId"
    """The budget ID."""


# --- restJson1 ser/de ---
def serialize_json(value: GetBudgetRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetBudgetRequest:
    out: GetBudgetRequest = {}  # type: ignore[typeddict-item]
    return out
