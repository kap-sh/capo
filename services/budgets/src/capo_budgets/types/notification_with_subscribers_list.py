"""Generated from Smithy shape ``com.amazonaws.budgets#NotificationWithSubscribersList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_budgets.types.notification_with_subscribers

NotificationWithSubscribersList: TypeAlias = list[
    "capo_budgets.types.notification_with_subscribers.NotificationWithSubscribers"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NotificationWithSubscribersList) -> list:
    import capo_budgets.types.notification_with_subscribers

    out: list = []
    for item in value:
        out.append(
            capo_budgets.types.notification_with_subscribers.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> NotificationWithSubscribersList:
    import capo_budgets.types.notification_with_subscribers

    out: NotificationWithSubscribersList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_budgets.types.notification_with_subscribers.deserialize_aws_json_1_1(
                item
            )
        )
    return out


def redact_sensitive(value: NotificationWithSubscribersList) -> list[Any]:
    import capo_budgets.types.notification_with_subscribers

    return [
        capo_budgets.types.notification_with_subscribers.redact_sensitive(item)
        for item in value
    ]
