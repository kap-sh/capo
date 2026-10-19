"""Generated from Smithy shape ``com.amazonaws.cleanrooms#AccessBudget``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cleanrooms.types.access_budget_details_list
    import capo_cleanrooms.types.budgeted_resource_arn
    import capo_cleanrooms.types.remaining_budget


class AccessBudget(TypedDict, closed=True):
    resource_arn: "capo_cleanrooms.types.budgeted_resource_arn.BudgetedResourceArn"
    """<p>The Amazon Resource Name (ARN) of the access budget resource.</p>"""
    details: "capo_cleanrooms.types.access_budget_details_list.AccessBudgetDetailsList"
    """<p>Detailed budget information including time bounds, remaining budget, and refresh settings.</p>"""
    aggregate_remaining_budget: "capo_cleanrooms.types.remaining_budget.RemainingBudget"
    """<p>The total remaining budget across all budget parameters, showing the lower value between the per-period budget and lifetime budget for this access budget. For individual parameter budgets, see <code>remainingBudget</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AccessBudget) -> dict:
    out: dict = {}
    out["resourceArn"] = value["resource_arn"]
    import capo_cleanrooms.types.access_budget_details_list

    out["details"] = capo_cleanrooms.types.access_budget_details_list.serialize_json(
        value["details"]
    )
    out["aggregateRemainingBudget"] = value["aggregate_remaining_budget"]
    return out


def deserialize_json(data: dict) -> AccessBudget:
    out: AccessBudget = {}  # type: ignore[typeddict-item]
    if data.get("resourceArn") is not None:
        out["resource_arn"] = data["resourceArn"]
    else:
        out["resource_arn"] = ""
    if data.get("details") is not None:
        import capo_cleanrooms.types.access_budget_details_list

        out["details"] = (
            capo_cleanrooms.types.access_budget_details_list.deserialize_json(
                data["details"]
            )
        )
    else:
        out["details"] = []
    if data.get("aggregateRemainingBudget") is not None:
        out["aggregate_remaining_budget"] = data["aggregateRemainingBudget"]
    else:
        out["aggregate_remaining_budget"] = 0
    return out
