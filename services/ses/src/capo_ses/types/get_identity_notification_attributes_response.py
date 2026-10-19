"""Generated from Smithy shape ``com.amazonaws.ses#GetIdentityNotificationAttributesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_ses._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ses.types.notification_attributes


class GetIdentityNotificationAttributesResponse(TypedDict, closed=True):
    notification_attributes: (
        "capo_ses.types.notification_attributes.NotificationAttributes"
    )
    """<p>A map of Identity to IdentityNotificationAttributes.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: GetIdentityNotificationAttributesResponse,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    import capo_ses.types.notification_attributes

    capo_ses.types.notification_attributes.serialize_query(
        value["notification_attributes"], pairs, f"{key_prefix}NotificationAttributes"
    )


def deserialize_query(el: Element) -> GetIdentityNotificationAttributesResponse:
    out: GetIdentityNotificationAttributesResponse = {}  # type: ignore[typeddict-item]
    child_notification_attributes = el.find("NotificationAttributes")
    if child_notification_attributes is not None:
        import capo_ses.types.notification_attributes

        out["notification_attributes"] = (
            capo_ses.types.notification_attributes.deserialize_query(
                child_notification_attributes
            )
        )
    else:
        out["notification_attributes"] = {}
    return out
