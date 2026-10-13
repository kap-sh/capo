"""Generated from Smithy shape ``com.amazonaws.budgets#CreateBudgetRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_budgets.errors import DeserializationError

if TYPE_CHECKING:
    import capo_budgets.types.account_id
    import capo_budgets.types.budget
    import capo_budgets.types.notification_with_subscribers_list
    import capo_budgets.types.resource_tag_list


class CreateBudgetRequest(TypedDict, closed=True):
    account_id: "capo_budgets.types.account_id.AccountId"
    """<p>The <code>accountId</code> that is associated with the budget.</p>"""
    budget: "capo_budgets.types.budget.Budget"
    """<p>The budget object that you want to create.</p>"""
    notifications_with_subscribers: NotRequired[
        "capo_budgets.types.notification_with_subscribers_list.NotificationWithSubscribersList"
    ]
    """<p>A notification that you want to associate with a budget. A budget can have up to five notifications, and each notification can have one SNS subscriber and up to 10 email subscribers. If you include notifications and subscribers in your <code>CreateBudget</code> call, Amazon Web Services creates the notifications and subscribers for you.</p>"""
    resource_tags: NotRequired["capo_budgets.types.resource_tag_list.ResourceTagList"]
    """<p>An optional list of tags to associate with the specified budget. Each tag consists of a key and a value, and each key must be unique for the resource.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateBudgetRequest) -> dict:
    out: dict = {}
    out["AccountId"] = value["account_id"]
    import capo_budgets.types.budget

    out["Budget"] = capo_budgets.types.budget.serialize_aws_json_1_1(value["budget"])
    if "notifications_with_subscribers" in value:
        import capo_budgets.types.notification_with_subscribers_list

        out["NotificationsWithSubscribers"] = (
            capo_budgets.types.notification_with_subscribers_list.serialize_aws_json_1_1(
                value["notifications_with_subscribers"]
            )
        )
    if "resource_tags" in value:
        import capo_budgets.types.resource_tag_list

        out["ResourceTags"] = (
            capo_budgets.types.resource_tag_list.serialize_aws_json_1_1(
                value["resource_tags"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateBudgetRequest:
    out: CreateBudgetRequest = {}  # type: ignore[typeddict-item]
    if data.get("AccountId") is not None:
        out["account_id"] = data["AccountId"]
    else:
        raise DeserializationError("CreateBudgetRequest.account_id required")
    if data.get("Budget") is not None:
        import capo_budgets.types.budget

        out["budget"] = capo_budgets.types.budget.deserialize_aws_json_1_1(
            data["Budget"]
        )
    else:
        raise DeserializationError("CreateBudgetRequest.budget required")
    if data.get("NotificationsWithSubscribers") is not None:
        import capo_budgets.types.notification_with_subscribers_list

        out["notifications_with_subscribers"] = (
            capo_budgets.types.notification_with_subscribers_list.deserialize_aws_json_1_1(
                data["NotificationsWithSubscribers"]
            )
        )
    if data.get("ResourceTags") is not None:
        import capo_budgets.types.resource_tag_list

        out["resource_tags"] = (
            capo_budgets.types.resource_tag_list.deserialize_aws_json_1_1(
                data["ResourceTags"]
            )
        )
    return out


def redact_sensitive(value: CreateBudgetRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "notifications_with_subscribers" in value:
        import capo_budgets.types.notification_with_subscribers_list

        out["notifications_with_subscribers"] = (
            capo_budgets.types.notification_with_subscribers_list.redact_sensitive(
                value["notifications_with_subscribers"]
            )
        )
    return out
