"""Generated from Smithy shape ``com.amazonaws.qbusiness#UpdateSubscriptionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_qbusiness.types.application_id
    import capo_qbusiness.types.subscription_id
    import capo_qbusiness.types.subscription_type


class UpdateSubscriptionRequest(TypedDict, closed=True):
    application_id: "capo_qbusiness.types.application_id.ApplicationId"
    """<p>The identifier of the Amazon Q Business application where the subscription update should take effect.</p>"""
    subscription_id: "capo_qbusiness.types.subscription_id.SubscriptionId"
    """<p>The identifier of the Amazon Q Business subscription to be updated.</p>"""
    type: "capo_qbusiness.types.subscription_type.SubscriptionType"
    """<p>The type of the Amazon Q Business subscription to be updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateSubscriptionRequest) -> dict:
    out: dict = {}
    import capo_qbusiness.types.subscription_type

    out["type"] = capo_qbusiness.types.subscription_type.serialize_json(value["type"])
    return out


def deserialize_json(data: dict) -> UpdateSubscriptionRequest:
    out: UpdateSubscriptionRequest = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        import capo_qbusiness.types.subscription_type

        out["type"] = capo_qbusiness.types.subscription_type.deserialize_json(
            data["type"]
        )
    else:
        import typing

        out["type"] = typing.cast(
            "capo_qbusiness.types.subscription_type.SubscriptionType", ""
        )
    return out
