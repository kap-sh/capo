"""Generated from Smithy shape ``com.amazonaws.budgets#UpdateSubscriberRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_budgets.errors import DeserializationError

if TYPE_CHECKING:
    import capo_budgets.types.account_id
    import capo_budgets.types.budget_name
    import capo_budgets.types.notification
    import capo_budgets.types.subscriber


class UpdateSubscriberRequest(TypedDict, closed=True):
    account_id: "capo_budgets.types.account_id.AccountId"
    """<p>The <code>accountId</code> that is associated with the budget whose subscriber you want to update.</p>"""
    budget_name: "capo_budgets.types.budget_name.BudgetName"
    """<p>The name of the budget whose subscriber you want to update.</p>"""
    notification: "capo_budgets.types.notification.Notification"
    """<p>The notification whose subscriber you want to update.</p>"""
    old_subscriber: "capo_budgets.types.subscriber.Subscriber"
    """<p>The previous subscriber that is associated with a budget notification.</p>"""
    new_subscriber: "capo_budgets.types.subscriber.Subscriber"
    """<p>The updated subscriber that is associated with a budget notification.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateSubscriberRequest) -> dict:
    out: dict = {}
    out["AccountId"] = value["account_id"]
    out["BudgetName"] = value["budget_name"]
    import capo_budgets.types.notification

    out["Notification"] = capo_budgets.types.notification.serialize_aws_json_1_1(
        value["notification"]
    )
    import capo_budgets.types.subscriber

    out["OldSubscriber"] = capo_budgets.types.subscriber.serialize_aws_json_1_1(
        value["old_subscriber"]
    )
    import capo_budgets.types.subscriber

    out["NewSubscriber"] = capo_budgets.types.subscriber.serialize_aws_json_1_1(
        value["new_subscriber"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateSubscriberRequest:
    out: UpdateSubscriberRequest = {}  # type: ignore[typeddict-item]
    if data.get("AccountId") is not None:
        out["account_id"] = data["AccountId"]
    else:
        raise DeserializationError("UpdateSubscriberRequest.account_id required")
    if data.get("BudgetName") is not None:
        out["budget_name"] = data["BudgetName"]
    else:
        raise DeserializationError("UpdateSubscriberRequest.budget_name required")
    if data.get("Notification") is not None:
        import capo_budgets.types.notification

        out["notification"] = capo_budgets.types.notification.deserialize_aws_json_1_1(
            data["Notification"]
        )
    else:
        raise DeserializationError("UpdateSubscriberRequest.notification required")
    if data.get("OldSubscriber") is not None:
        import capo_budgets.types.subscriber

        out["old_subscriber"] = capo_budgets.types.subscriber.deserialize_aws_json_1_1(
            data["OldSubscriber"]
        )
    else:
        raise DeserializationError("UpdateSubscriberRequest.old_subscriber required")
    if data.get("NewSubscriber") is not None:
        import capo_budgets.types.subscriber

        out["new_subscriber"] = capo_budgets.types.subscriber.deserialize_aws_json_1_1(
            data["NewSubscriber"]
        )
    else:
        raise DeserializationError("UpdateSubscriberRequest.new_subscriber required")
    return out


def redact_sensitive(value: UpdateSubscriberRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "old_subscriber" in value:
        import capo_budgets.types.subscriber

        out["old_subscriber"] = capo_budgets.types.subscriber.redact_sensitive(
            value["old_subscriber"]
        )
    if "new_subscriber" in value:
        import capo_budgets.types.subscriber

        out["new_subscriber"] = capo_budgets.types.subscriber.redact_sensitive(
            value["new_subscriber"]
        )
    return out
