"""Generated from Smithy shape ``com.amazonaws.budgets#NotificationWithSubscribers``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_budgets.errors import DeserializationError

if TYPE_CHECKING:
    import capo_budgets.types.notification
    import capo_budgets.types.subscribers


class NotificationWithSubscribers(TypedDict, closed=True):
    notification: "capo_budgets.types.notification.Notification"
    """<p>The notification that's associated with a budget.</p>"""
    subscribers: "capo_budgets.types.subscribers.Subscribers"
    """<p>A list of subscribers who are subscribed to this notification.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NotificationWithSubscribers) -> dict:
    out: dict = {}
    import capo_budgets.types.notification

    out["Notification"] = capo_budgets.types.notification.serialize_aws_json_1_1(
        value["notification"]
    )
    import capo_budgets.types.subscribers

    out["Subscribers"] = capo_budgets.types.subscribers.serialize_aws_json_1_1(
        value["subscribers"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> NotificationWithSubscribers:
    out: NotificationWithSubscribers = {}  # type: ignore[typeddict-item]
    if data.get("Notification") is not None:
        import capo_budgets.types.notification

        out["notification"] = capo_budgets.types.notification.deserialize_aws_json_1_1(
            data["Notification"]
        )
    else:
        raise DeserializationError("NotificationWithSubscribers.notification required")
    if data.get("Subscribers") is not None:
        import capo_budgets.types.subscribers

        out["subscribers"] = capo_budgets.types.subscribers.deserialize_aws_json_1_1(
            data["Subscribers"]
        )
    else:
        raise DeserializationError("NotificationWithSubscribers.subscribers required")
    return out


def redact_sensitive(value: NotificationWithSubscribers) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "subscribers" in value:
        import capo_budgets.types.subscribers

        out["subscribers"] = capo_budgets.types.subscribers.redact_sensitive(
            value["subscribers"]
        )
    return out
