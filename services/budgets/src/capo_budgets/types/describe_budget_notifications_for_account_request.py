"""Generated from Smithy shape ``com.amazonaws.budgets#DescribeBudgetNotificationsForAccountRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_budgets.types.account_id
    import capo_budgets.types.generic_string
    import capo_budgets.types.max_results_budget_notifications


class DescribeBudgetNotificationsForAccountRequest(TypedDict, closed=True):
    account_id: "capo_budgets.types.account_id.AccountId"
    max_results: NotRequired[
        "capo_budgets.types.max_results_budget_notifications.MaxResultsBudgetNotifications"
    ]
    """<p> An integer that represents how many budgets a paginated response contains. The default is 50. </p>"""
    next_token: NotRequired["capo_budgets.types.generic_string.GenericString"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeBudgetNotificationsForAccountRequest) -> dict:
    out: dict = {}
    out["AccountId"] = value["account_id"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> DescribeBudgetNotificationsForAccountRequest:
    out: DescribeBudgetNotificationsForAccountRequest = {}  # type: ignore[typeddict-item]
    if data.get("AccountId") is not None:
        out["account_id"] = data["AccountId"]
    else:
        out["account_id"] = ""
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
