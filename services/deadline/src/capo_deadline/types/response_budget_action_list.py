"""Generated from Smithy shape ``com.amazonaws.deadline#ResponseBudgetActionList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_deadline.types.response_budget_action

ResponseBudgetActionList: TypeAlias = list[
    "capo_deadline.types.response_budget_action.ResponseBudgetAction"
]


# --- restJson1 ser/de ---
def serialize_json(value: ResponseBudgetActionList) -> list:
    import capo_deadline.types.response_budget_action

    out: list = []
    for item in value:
        out.append(capo_deadline.types.response_budget_action.serialize_json(item))
    return out


def deserialize_json(data: list) -> ResponseBudgetActionList:
    import capo_deadline.types.response_budget_action

    out: ResponseBudgetActionList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_deadline.types.response_budget_action.deserialize_json(item))
    return out


def redact_sensitive(value: ResponseBudgetActionList) -> list[Any]:
    import capo_deadline.types.response_budget_action

    return [
        capo_deadline.types.response_budget_action.redact_sensitive(item)
        for item in value
    ]
