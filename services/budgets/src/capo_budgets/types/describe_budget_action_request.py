"""Generated from Smithy shape ``com.amazonaws.budgets#DescribeBudgetActionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_budgets.types.account_id
    import capo_budgets.types.action_id
    import capo_budgets.types.budget_name


class DescribeBudgetActionRequest(TypedDict, closed=True):
    account_id: "capo_budgets.types.account_id.AccountId"
    budget_name: "capo_budgets.types.budget_name.BudgetName"
    action_id: "capo_budgets.types.action_id.ActionId"
    """<p> A system-generated universally unique identifier (UUID) for the action. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeBudgetActionRequest) -> dict:
    out: dict = {}
    out["AccountId"] = value["account_id"]
    out["BudgetName"] = value["budget_name"]
    out["ActionId"] = value["action_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeBudgetActionRequest:
    out: DescribeBudgetActionRequest = {}  # type: ignore[typeddict-item]
    if data.get("AccountId") is not None:
        out["account_id"] = data["AccountId"]
    else:
        out["account_id"] = ""
    if data.get("BudgetName") is not None:
        out["budget_name"] = data["BudgetName"]
    else:
        out["budget_name"] = ""
    if data.get("ActionId") is not None:
        out["action_id"] = data["ActionId"]
    else:
        out["action_id"] = ""
    return out
