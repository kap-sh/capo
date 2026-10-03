"""Generated from Smithy shape ``com.amazonaws.connect#SendOutboundWebNotificationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_connect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connect.types.client_token
    import capo_connect.types.instance_id
    import capo_connect.types.timestamp
    import capo_connect.types.web_browser_id
    import capo_connect.types.web_notification_content
    import capo_connect.types.web_notification_source
    import capo_connect.types.web_session_id
    import capo_connect.types.widget_destination


class SendOutboundWebNotificationRequest(TypedDict, closed=True):
    instance_id: "capo_connect.types.instance_id.InstanceId"
    """<p>The identifier of the Connect Customer instance. You can <a href="https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    client_token: NotRequired["capo_connect.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services SDK populates this field. For more information about idempotency, see <a href="https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/">Making retries safe with idempotent APIs</a>.</p>"""
    browser_id: "capo_connect.types.web_browser_id.WebBrowserId"
    """<p>A unique identifier for the customer's web browser instance to which the notification is being sent.</p>"""
    session_id: "capo_connect.types.web_session_id.WebSessionId"
    """<p>A unique identifier for the customer's web session to which the notification is being sent.</p>"""
    expires_at: "capo_connect.types.timestamp.Timestamp"
    """<p>The timestamp, in Unix epoch time format, at which the web notification expires. After this time, the notification is no longer delivered to the customer's browser.</p>"""
    source: "capo_connect.types.web_notification_source.WebNotificationSource"
    """<p>The source of the web notification. A <code>SourceCampaign</code> object identifies the campaign and outbound request that triggered this notification.</p>"""
    destination: "capo_connect.types.widget_destination.WidgetDestination"
    """<p>The destination for the web notification, specifying the communication widget that delivers the notification and the customer profile of the recipient.</p>"""
    content: "capo_connect.types.web_notification_content.WebNotificationContent"
    """<p>The content of the web notification, including the notification type, the view to render, and any optional attributes used to populate it.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SendOutboundWebNotificationRequest) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    out["BrowserId"] = value["browser_id"]
    out["SessionId"] = value["session_id"]
    import capo_connect.types.timestamp

    out["ExpiresAt"] = capo_connect.types.timestamp.serialize_json(value["expires_at"])
    import capo_connect.types.web_notification_source

    out["Source"] = capo_connect.types.web_notification_source.serialize_json(
        value["source"]
    )
    import capo_connect.types.widget_destination

    out["Destination"] = capo_connect.types.widget_destination.serialize_json(
        value["destination"]
    )
    import capo_connect.types.web_notification_content

    out["Content"] = capo_connect.types.web_notification_content.serialize_json(
        value["content"]
    )
    return out


def deserialize_json(data: dict) -> SendOutboundWebNotificationRequest:
    out: SendOutboundWebNotificationRequest = {}  # type: ignore[typeddict-item]
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    if data.get("BrowserId") is not None:
        out["browser_id"] = data["BrowserId"]
    else:
        raise DeserializationError(
            "SendOutboundWebNotificationRequest.browser_id required"
        )
    if data.get("SessionId") is not None:
        out["session_id"] = data["SessionId"]
    else:
        raise DeserializationError(
            "SendOutboundWebNotificationRequest.session_id required"
        )
    if data.get("ExpiresAt") is not None:
        import capo_connect.types.timestamp

        out["expires_at"] = capo_connect.types.timestamp.deserialize_json(
            data["ExpiresAt"]
        )
    else:
        raise DeserializationError(
            "SendOutboundWebNotificationRequest.expires_at required"
        )
    if data.get("Source") is not None:
        import capo_connect.types.web_notification_source

        out["source"] = capo_connect.types.web_notification_source.deserialize_json(
            data["Source"]
        )
    else:
        raise DeserializationError("SendOutboundWebNotificationRequest.source required")
    if data.get("Destination") is not None:
        import capo_connect.types.widget_destination

        out["destination"] = capo_connect.types.widget_destination.deserialize_json(
            data["Destination"]
        )
    else:
        raise DeserializationError(
            "SendOutboundWebNotificationRequest.destination required"
        )
    if data.get("Content") is not None:
        import capo_connect.types.web_notification_content

        out["content"] = capo_connect.types.web_notification_content.deserialize_json(
            data["Content"]
        )
    else:
        raise DeserializationError(
            "SendOutboundWebNotificationRequest.content required"
        )
    return out
