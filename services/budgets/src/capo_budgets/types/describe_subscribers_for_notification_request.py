"""Generated from Smithy shape ``com.amazonaws.budgets#DescribeSubscribersForNotificationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_budgets.errors import DeserializationError

if TYPE_CHECKING:
    import capo_budgets.types.account_id
    import capo_budgets.types.budget_name
    import capo_budgets.types.generic_string
    import capo_budgets.types.max_results
    import capo_budgets.types.notification


class DescribeSubscribersForNotificationRequest(TypedDict, closed=True):
    account_id: "capo_budgets.types.account_id.AccountId"
    """<p>The <code>accountId</code> that is associated with the budget whose subscribers you want descriptions of.</p>"""
    budget_name: "capo_budgets.types.budget_name.BudgetName"
    """<p>The name of the budget whose subscribers you want descriptions of.</p>"""
    notification: "capo_budgets.types.notification.Notification"
    """<p>The notification whose subscribers you want to list.</p>"""
    max_results: NotRequired["capo_budgets.types.max_results.MaxResults"]
    """<p>An optional integer that represents how many entries a paginated response contains.</p>"""
    next_token: NotRequired["capo_budgets.types.generic_string.GenericString"]
    """<p>The pagination token that you include in your request to indicate the next set of results that you want to retrieve.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeSubscribersForNotificationRequest) -> dict:
    out: dict = {}
    out["AccountId"] = value["account_id"]
    out["BudgetName"] = value["budget_name"]
    import capo_budgets.types.notification

    out["Notification"] = capo_budgets.types.notification.serialize_aws_json_1_1(
        value["notification"]
    )
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeSubscribersForNotificationRequest:
    out: DescribeSubscribersForNotificationRequest = {}  # type: ignore[typeddict-item]
    if data.get("AccountId") is not None:
        out["account_id"] = data["AccountId"]
    else:
        out["account_id"] = ""
    if data.get("BudgetName") is not None:
        out["budget_name"] = data["BudgetName"]
    else:
        out["budget_name"] = ""
    if data.get("Notification") is not None:
        import capo_budgets.types.notification

        out["notification"] = capo_budgets.types.notification.deserialize_aws_json_1_1(
            data["Notification"]
        )
    else:
        raise DeserializationError(
            "DescribeSubscribersForNotificationRequest.notification required"
        )
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
