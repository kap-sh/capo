"""Generated from Smithy shape ``com.amazonaws.dataexchange#SendDataSetNotificationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_dataexchange.types.__string_min0_max4096
    import capo_dataexchange.types.client_token
    import capo_dataexchange.types.id
    import capo_dataexchange.types.notification_details
    import capo_dataexchange.types.notification_type
    import capo_dataexchange.types.scope_details


class SendDataSetNotificationRequest(TypedDict, closed=True):
    scope: NotRequired["capo_dataexchange.types.scope_details.ScopeDetails"]
    """<p>Affected scope of this notification such as the underlying resources affected by the notification event.</p>"""
    client_token: NotRequired["capo_dataexchange.types.client_token.ClientToken"]
    """<p>Idempotency key for the notification, this key allows us to deduplicate notifications that are sent in quick succession erroneously.</p>"""
    comment: NotRequired[
        "capo_dataexchange.types.__string_min0_max4096.__stringMin0Max4096"
    ]
    """<p>Free-form text field for providers to add information about their notifications.</p>"""
    data_set_id: "capo_dataexchange.types.id.Id"
    """<p>Affected data set of the notification.</p>"""
    details: NotRequired[
        "capo_dataexchange.types.notification_details.NotificationDetails"
    ]
    """<p>Extra details specific to this notification type.</p>"""
    type: "capo_dataexchange.types.notification_type.NotificationType"
    """<p>The type of the notification. Describing the kind of event the notification is alerting you to.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SendDataSetNotificationRequest) -> dict:
    out: dict = {}
    if "scope" in value:
        import capo_dataexchange.types.scope_details

        out["Scope"] = capo_dataexchange.types.scope_details.serialize_json(
            value["scope"]
        )
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    if "comment" in value:
        out["Comment"] = value["comment"]
    if "details" in value:
        import capo_dataexchange.types.notification_details

        out["Details"] = capo_dataexchange.types.notification_details.serialize_json(
            value["details"]
        )
    out["Type"] = value["type"]
    return out


def deserialize_json(data: dict) -> SendDataSetNotificationRequest:
    out: SendDataSetNotificationRequest = {}  # type: ignore[typeddict-item]
    if data.get("Scope") is not None:
        import capo_dataexchange.types.scope_details

        out["scope"] = capo_dataexchange.types.scope_details.deserialize_json(
            data["Scope"]
        )
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    if data.get("Comment") is not None:
        out["comment"] = data["Comment"]
    if data.get("Details") is not None:
        import capo_dataexchange.types.notification_details

        out["details"] = capo_dataexchange.types.notification_details.deserialize_json(
            data["Details"]
        )
    if data.get("Type") is not None:
        out["type"] = data["Type"]
    else:
        out["type"] = ""
    return out
