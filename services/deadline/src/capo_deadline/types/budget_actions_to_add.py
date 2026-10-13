"""Generated from Smithy shape ``com.amazonaws.deadline#BudgetActionsToAdd``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_deadline.types.budget_action_to_add

BudgetActionsToAdd: TypeAlias = list[
    "capo_deadline.types.budget_action_to_add.BudgetActionToAdd"
]


# --- restJson1 ser/de ---
def serialize_json(value: BudgetActionsToAdd) -> list:
    import capo_deadline.types.budget_action_to_add

    out: list = []
    for item in value:
        out.append(capo_deadline.types.budget_action_to_add.serialize_json(item))
    return out


def deserialize_json(data: list) -> BudgetActionsToAdd:
    import capo_deadline.types.budget_action_to_add

    out: BudgetActionsToAdd = []
    for item in data:
        if item is None:
            continue
        out.append(capo_deadline.types.budget_action_to_add.deserialize_json(item))
    return out


def redact_sensitive(value: BudgetActionsToAdd) -> list[Any]:
    import capo_deadline.types.budget_action_to_add

    return [
        capo_deadline.types.budget_action_to_add.redact_sensitive(item)
        for item in value
    ]
