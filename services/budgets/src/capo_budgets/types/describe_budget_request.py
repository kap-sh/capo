"""Generated from Smithy shape ``com.amazonaws.budgets#DescribeBudgetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_budgets.types.account_id
    import capo_budgets.types.budget_name
    import capo_budgets.types.nullable_boolean


class DescribeBudgetRequest(TypedDict, closed=True):
    account_id: "capo_budgets.types.account_id.AccountId"
    """<p>The <code>accountId</code> that is associated with the budget that you want a description of.</p>"""
    budget_name: "capo_budgets.types.budget_name.BudgetName"
    """<p>The name of the budget that you want a description of.</p>"""
    show_filter_expression: NotRequired[
        "capo_budgets.types.nullable_boolean.NullableBoolean"
    ]
    """<p>Specifies whether the response includes the filter expression associated with the budget. By showing the filter expression, you can see detailed filtering logic applied to the budget, such as Amazon Web Services services or tags that are being tracked.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeBudgetRequest) -> dict:
    out: dict = {}
    out["AccountId"] = value["account_id"]
    out["BudgetName"] = value["budget_name"]
    if "show_filter_expression" in value:
        out["ShowFilterExpression"] = value["show_filter_expression"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeBudgetRequest:
    out: DescribeBudgetRequest = {}  # type: ignore[typeddict-item]
    if data.get("AccountId") is not None:
        out["account_id"] = data["AccountId"]
    else:
        out["account_id"] = ""
    if data.get("BudgetName") is not None:
        out["budget_name"] = data["BudgetName"]
    else:
        out["budget_name"] = ""
    if data.get("ShowFilterExpression") is not None:
        out["show_filter_expression"] = data["ShowFilterExpression"]
    return out
