"""Generated from Smithy shape ``com.amazonaws.deadline#ListBudgetsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.budget_status
    import capo_deadline.types.farm_id
    import capo_deadline.types.max_results
    import capo_deadline.types.next_token


class ListBudgetsRequest(TypedDict, closed=True):
    farm_id: "capo_deadline.types.farm_id.FarmId"
    """The farm ID associated with the budgets."""
    next_token: NotRequired["capo_deadline.types.next_token.NextToken"]
    """The token for the next set of results, or <code>null</code> to start from the beginning."""
    max_results: NotRequired["capo_deadline.types.max_results.MaxResults"]
    """The maximum number of results to return. Use this parameter with <code>NextToken</code> to get results as a set of sequential pages."""
    status: NotRequired["capo_deadline.types.budget_status.BudgetStatus"]
    """The status to list for the budgets."""


# --- restJson1 ser/de ---
def serialize_json(value: ListBudgetsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListBudgetsRequest:
    out: ListBudgetsRequest = {}  # type: ignore[typeddict-item]
    return out
