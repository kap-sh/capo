"""Generated from Smithy shape ``com.amazonaws.qbusiness#AutoSubscriptionConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qbusiness.types.auto_subscription_status
    import capo_qbusiness.types.subscription_type


class AutoSubscriptionConfiguration(TypedDict, closed=True):
    auto_subscribe: (
        "capo_qbusiness.types.auto_subscription_status.AutoSubscriptionStatus"
    )
    """<p>Describes whether automatic subscriptions are enabled for an Amazon Q Business application using IAM identity federation for user management.</p>"""
    default_subscription_type: NotRequired[
        "capo_qbusiness.types.subscription_type.SubscriptionType"
    ]
    """<p>Describes the default subscription type assigned to an Amazon Q Business application using IAM identity federation for user management. If the value for <code>autoSubscribe</code> is set to <code>ENABLED</code> you must select a value for this field.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AutoSubscriptionConfiguration) -> dict:
    out: dict = {}
    import capo_qbusiness.types.auto_subscription_status

    out["autoSubscribe"] = capo_qbusiness.types.auto_subscription_status.serialize_json(
        value["auto_subscribe"]
    )
    if "default_subscription_type" in value:
        import capo_qbusiness.types.subscription_type

        out["defaultSubscriptionType"] = (
            capo_qbusiness.types.subscription_type.serialize_json(
                value["default_subscription_type"]
            )
        )
    return out


def deserialize_json(data: dict) -> AutoSubscriptionConfiguration:
    out: AutoSubscriptionConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("autoSubscribe") is not None:
        import capo_qbusiness.types.auto_subscription_status

        out["auto_subscribe"] = (
            capo_qbusiness.types.auto_subscription_status.deserialize_json(
                data["autoSubscribe"]
            )
        )
    else:
        import typing

        out["auto_subscribe"] = typing.cast(
            "capo_qbusiness.types.auto_subscription_status.AutoSubscriptionStatus", ""
        )
    if data.get("defaultSubscriptionType") is not None:
        import capo_qbusiness.types.subscription_type

        out["default_subscription_type"] = (
            capo_qbusiness.types.subscription_type.deserialize_json(
                data["defaultSubscriptionType"]
            )
        )
    return out
