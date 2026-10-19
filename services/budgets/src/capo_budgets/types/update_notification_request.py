"""Generated from Smithy shape ``com.amazonaws.budgets#UpdateNotificationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_budgets.errors import DeserializationError

if TYPE_CHECKING:
    import capo_budgets.types.account_id
    import capo_budgets.types.budget_name
    import capo_budgets.types.notification


class UpdateNotificationRequest(TypedDict, closed=True):
    account_id: "capo_budgets.types.account_id.AccountId"
    """<p>The <code>accountId</code> that is associated with the budget whose notification you want to update.</p>"""
    budget_name: "capo_budgets.types.budget_name.BudgetName"
    """<p>The name of the budget whose notification you want to update.</p>"""
    old_notification: "capo_budgets.types.notification.Notification"
    """<p>The previous notification that is associated with a budget.</p>"""
    new_notification: "capo_budgets.types.notification.Notification"
    """<p>The updated notification to be associated with a budget.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateNotificationRequest) -> dict:
    out: dict = {}
    out["AccountId"] = value["account_id"]
    out["BudgetName"] = value["budget_name"]
    import capo_budgets.types.notification

    out["OldNotification"] = capo_budgets.types.notification.serialize_aws_json_1_1(
        value["old_notification"]
    )
    import capo_budgets.types.notification

    out["NewNotification"] = capo_budgets.types.notification.serialize_aws_json_1_1(
        value["new_notification"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateNotificationRequest:
    out: UpdateNotificationRequest = {}  # type: ignore[typeddict-item]
    if data.get("AccountId") is not None:
        out["account_id"] = data["AccountId"]
    else:
        out["account_id"] = ""
    if data.get("BudgetName") is not None:
        out["budget_name"] = data["BudgetName"]
    else:
        out["budget_name"] = ""
    if data.get("OldNotification") is not None:
        import capo_budgets.types.notification

        out["old_notification"] = (
            capo_budgets.types.notification.deserialize_aws_json_1_1(
                data["OldNotification"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateNotificationRequest.old_notification required"
        )
    if data.get("NewNotification") is not None:
        import capo_budgets.types.notification

        out["new_notification"] = (
            capo_budgets.types.notification.deserialize_aws_json_1_1(
                data["NewNotification"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateNotificationRequest.new_notification required"
        )
    return out
