"""Generated from Smithy shape ``com.amazonaws.workdocs#CreateNotificationSubscriptionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_workdocs.types.id_type
    import capo_workdocs.types.subscription_end_point_type
    import capo_workdocs.types.subscription_protocol_type
    import capo_workdocs.types.subscription_type


class CreateNotificationSubscriptionRequest(TypedDict, closed=True):
    organization_id: "capo_workdocs.types.id_type.IdType"
    """<p>The ID of the organization.</p>"""
    endpoint: "capo_workdocs.types.subscription_end_point_type.SubscriptionEndPointType"
    """<p>The endpoint to receive the notifications. If the protocol is HTTPS, the endpoint is a URL that begins with <code>https</code>.</p>"""
    protocol: "capo_workdocs.types.subscription_protocol_type.SubscriptionProtocolType"
    """<p>The protocol to use. The supported value is https, which delivers JSON-encoded messages using HTTPS POST.</p>"""
    subscription_type: "capo_workdocs.types.subscription_type.SubscriptionType"
    """<p>The notification type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateNotificationSubscriptionRequest) -> dict:
    out: dict = {}
    out["Endpoint"] = value["endpoint"]
    import capo_workdocs.types.subscription_protocol_type

    out["Protocol"] = capo_workdocs.types.subscription_protocol_type.serialize_json(
        value["protocol"]
    )
    import capo_workdocs.types.subscription_type

    out["SubscriptionType"] = capo_workdocs.types.subscription_type.serialize_json(
        value["subscription_type"]
    )
    return out


def deserialize_json(data: dict) -> CreateNotificationSubscriptionRequest:
    out: CreateNotificationSubscriptionRequest = {}  # type: ignore[typeddict-item]
    if data.get("Endpoint") is not None:
        out["endpoint"] = data["Endpoint"]
    else:
        out["endpoint"] = ""
    if data.get("Protocol") is not None:
        import capo_workdocs.types.subscription_protocol_type

        out["protocol"] = (
            capo_workdocs.types.subscription_protocol_type.deserialize_json(
                data["Protocol"]
            )
        )
    else:
        import typing

        out["protocol"] = typing.cast(
            "capo_workdocs.types.subscription_protocol_type.SubscriptionProtocolType",
            "",
        )
    if data.get("SubscriptionType") is not None:
        import capo_workdocs.types.subscription_type

        out["subscription_type"] = (
            capo_workdocs.types.subscription_type.deserialize_json(
                data["SubscriptionType"]
            )
        )
    else:
        import typing

        out["subscription_type"] = typing.cast(
            "capo_workdocs.types.subscription_type.SubscriptionType", ""
        )
    return out
