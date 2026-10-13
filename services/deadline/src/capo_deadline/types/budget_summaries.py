"""Generated from Smithy shape ``com.amazonaws.deadline#BudgetSummaries``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_deadline.types.budget_summary

BudgetSummaries: TypeAlias = list["capo_deadline.types.budget_summary.BudgetSummary"]


# --- restJson1 ser/de ---
def serialize_json(value: BudgetSummaries) -> list:
    import capo_deadline.types.budget_summary

    out: list = []
    for item in value:
        out.append(capo_deadline.types.budget_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> BudgetSummaries:
    import capo_deadline.types.budget_summary

    out: BudgetSummaries = []
    for item in data:
        if item is None:
            continue
        out.append(capo_deadline.types.budget_summary.deserialize_json(item))
    return out


def redact_sensitive(value: BudgetSummaries) -> list[Any]:
    import capo_deadline.types.budget_summary

    return [capo_deadline.types.budget_summary.redact_sensitive(item) for item in value]
