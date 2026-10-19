"""Generated from Smithy shape ``com.amazonaws.qbusiness#CreateSubscriptionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qbusiness.types.application_id
    import capo_qbusiness.types.client_token
    import capo_qbusiness.types.subscription_principal
    import capo_qbusiness.types.subscription_type


class CreateSubscriptionRequest(TypedDict, closed=True):
    application_id: "capo_qbusiness.types.application_id.ApplicationId"
    """<p>The identifier of the Amazon Q Business application the subscription should be added to.</p>"""
    principal: "capo_qbusiness.types.subscription_principal.SubscriptionPrincipal"
    """<p>The IAM Identity Center <code>UserId</code> or <code>GroupId</code> of a user or group in the IAM Identity Center instance connected to the Amazon Q Business application.</p>"""
    type: "capo_qbusiness.types.subscription_type.SubscriptionType"
    """<p>The type of Amazon Q Business subscription you want to create.</p>"""
    client_token: NotRequired["capo_qbusiness.types.client_token.ClientToken"]
    """<p>A token that you provide to identify the request to create a subscription for your Amazon Q Business application.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateSubscriptionRequest) -> dict:
    out: dict = {}
    import capo_qbusiness.types.subscription_principal

    out["principal"] = capo_qbusiness.types.subscription_principal.serialize_json(
        value["principal"]
    )
    import capo_qbusiness.types.subscription_type

    out["type"] = capo_qbusiness.types.subscription_type.serialize_json(value["type"])
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> CreateSubscriptionRequest:
    out: CreateSubscriptionRequest = {}  # type: ignore[typeddict-item]
    if data.get("principal") is not None:
        import capo_qbusiness.types.subscription_principal

        out["principal"] = capo_qbusiness.types.subscription_principal.deserialize_json(
            data["principal"]
        )
    else:
        import capo_qbusiness.types._unknown

        out["principal"] = capo_qbusiness.types._unknown.UnknownUnionMember("")
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
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out
