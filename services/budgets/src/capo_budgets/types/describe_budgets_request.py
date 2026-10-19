"""Generated from Smithy shape ``com.amazonaws.budgets#DescribeBudgetsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_budgets.types.account_id
    import capo_budgets.types.generic_string
    import capo_budgets.types.max_results_describe_budgets
    import capo_budgets.types.nullable_boolean


class DescribeBudgetsRequest(TypedDict, closed=True):
    account_id: "capo_budgets.types.account_id.AccountId"
    """<p>The <code>accountId</code> that is associated with the budgets that you want to describe.</p>"""
    max_results: NotRequired[
        "capo_budgets.types.max_results_describe_budgets.MaxResultsDescribeBudgets"
    ]
    """<p>An integer that represents how many budgets a paginated response contains. The default is 100.</p>"""
    next_token: NotRequired["capo_budgets.types.generic_string.GenericString"]
    """<p>The pagination token that you include in your request to indicate the next set of results that you want to retrieve.</p>"""
    show_filter_expression: NotRequired[
        "capo_budgets.types.nullable_boolean.NullableBoolean"
    ]
    """<p>Specifies whether the response includes the filter expression associated with the budgets. By showing the filter expression, you can see detailed filtering logic applied to the budgets, such as Amazon Web Services services or tags that are being tracked.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeBudgetsRequest) -> dict:
    out: dict = {}
    out["AccountId"] = value["account_id"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "show_filter_expression" in value:
        out["ShowFilterExpression"] = value["show_filter_expression"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeBudgetsRequest:
    out: DescribeBudgetsRequest = {}  # type: ignore[typeddict-item]
    if data.get("AccountId") is not None:
        out["account_id"] = data["AccountId"]
    else:
        out["account_id"] = ""
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("ShowFilterExpression") is not None:
        out["show_filter_expression"] = data["ShowFilterExpression"]
    return out
