"""Generated from Smithy shape ``com.amazonaws.budgets#UpdateBudgetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_budgets.errors import DeserializationError

if TYPE_CHECKING:
    import capo_budgets.types.account_id
    import capo_budgets.types.budget


class UpdateBudgetRequest(TypedDict, closed=True):
    account_id: "capo_budgets.types.account_id.AccountId"
    """<p>The <code>accountId</code> that is associated with the budget that you want to update.</p>"""
    new_budget: "capo_budgets.types.budget.Budget"
    """<p>The budget that you want to update your budget to.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateBudgetRequest) -> dict:
    out: dict = {}
    out["AccountId"] = value["account_id"]
    import capo_budgets.types.budget

    out["NewBudget"] = capo_budgets.types.budget.serialize_aws_json_1_1(
        value["new_budget"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateBudgetRequest:
    out: UpdateBudgetRequest = {}  # type: ignore[typeddict-item]
    if data.get("AccountId") is not None:
        out["account_id"] = data["AccountId"]
    else:
        out["account_id"] = ""
    if data.get("NewBudget") is not None:
        import capo_budgets.types.budget

        out["new_budget"] = capo_budgets.types.budget.deserialize_aws_json_1_1(
            data["NewBudget"]
        )
    else:
        raise DeserializationError("UpdateBudgetRequest.new_budget required")
    return out
