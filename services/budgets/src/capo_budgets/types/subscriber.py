"""Generated from Smithy shape ``com.amazonaws.budgets#Subscriber``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_budgets.types.subscriber_address
    import capo_budgets.types.subscription_type


class Subscriber(TypedDict, closed=True):
    subscription_type: "capo_budgets.types.subscription_type.SubscriptionType"
    """<p>The type of notification that Amazon Web Services sends to a subscriber.</p>"""
    address: "capo_budgets.types.subscriber_address.SubscriberAddress"
    """<p>The address that Amazon Web Services sends budget notifications to, either an SNS topic or an email.</p> <p>When you create a subscriber, the value of <code>Address</code> can't contain line breaks.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Subscriber) -> dict:
    out: dict = {}
    import capo_budgets.types.subscription_type

    out["SubscriptionType"] = (
        capo_budgets.types.subscription_type.serialize_aws_json_1_1(
            value["subscription_type"]
        )
    )
    out["Address"] = value["address"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Subscriber:
    out: Subscriber = {}  # type: ignore[typeddict-item]
    if data.get("SubscriptionType") is not None:
        import capo_budgets.types.subscription_type

        out["subscription_type"] = (
            capo_budgets.types.subscription_type.deserialize_aws_json_1_1(
                data["SubscriptionType"]
            )
        )
    else:
        import typing

        out["subscription_type"] = typing.cast(
            "capo_budgets.types.subscription_type.SubscriptionType", ""
        )
    if data.get("Address") is not None:
        out["address"] = data["Address"]
    else:
        out["address"] = ""
    return out


def redact_sensitive(value: Subscriber) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "address" in value:
        out["address"] = "*** Sensitive Data Redacted ***"
    return out
