"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#AccessBudget``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cleanroomsml.types.access_budget_details_list
    import capo_cleanroomsml.types.budget
    import capo_cleanroomsml.types.budgeted_resource_arn


class AccessBudget(TypedDict, closed=True):
    resource_arn: "capo_cleanroomsml.types.budgeted_resource_arn.BudgetedResourceArn"
    """<p>The Amazon Resource Name (ARN) of the resource that this access budget applies to.</p>"""
    details: (
        "capo_cleanroomsml.types.access_budget_details_list.AccessBudgetDetailsList"
    )
    """<p>A list of budget details for this resource. Contains active budget periods that apply to the resource.</p>"""
    aggregate_remaining_budget: "capo_cleanroomsml.types.budget.Budget"
    """<p>The total remaining budget across all active budget periods for this resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AccessBudget) -> dict:
    out: dict = {}
    out["resourceArn"] = value["resource_arn"]
    import capo_cleanroomsml.types.access_budget_details_list

    out["details"] = capo_cleanroomsml.types.access_budget_details_list.serialize_json(
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
        import capo_cleanroomsml.types.access_budget_details_list

        out["details"] = (
            capo_cleanroomsml.types.access_budget_details_list.deserialize_json(
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
