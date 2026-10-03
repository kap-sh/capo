"""Generated from Smithy shape ``com.amazonaws.sesv2#EventDestination``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_sesv2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_sesv2.types.cloud_watch_destination
    import capo_sesv2.types.enabled
    import capo_sesv2.types.event_bridge_destination
    import capo_sesv2.types.event_destination_name
    import capo_sesv2.types.event_types
    import capo_sesv2.types.kinesis_firehose_destination
    import capo_sesv2.types.pinpoint_destination
    import capo_sesv2.types.sns_destination


class EventDestination(TypedDict, closed=True):
    name: "capo_sesv2.types.event_destination_name.EventDestinationName"
    """<p>A name that identifies the event destination.</p>"""
    enabled: "capo_sesv2.types.enabled.Enabled"
    """<p>If <code>true</code>, the event destination is enabled. When the event destination is enabled, the specified event types are sent to the destinations in this <code>EventDestinationDefinition</code>.</p> <p>If <code>false</code>, the event destination is disabled. When the event destination is disabled, events aren't sent to the specified destinations.</p>"""
    matching_event_types: "capo_sesv2.types.event_types.EventTypes"
    """<p>The types of events that Amazon SES sends to the specified event destinations.</p> <ul> <li> <p> <code>SEND</code> - The send request was successful and SES will attempt to deliver the message to the recipient’s mail server. (If account-level or global suppression is being used, SES will still count it as a send, but delivery is suppressed.)</p> </li> <li> <p> <code>REJECT</code> - SES accepted the email, but determined that it contained a virus and didn’t attempt to deliver it to the recipient’s mail server.</p> </li> <li> <p> <code>BOUNCE</code> - (<i>Hard bounce</i>) The recipient's mail server permanently rejected the email. (<i>Soft bounces</i> are only included when SES fails to deliver the email after retrying for a period of time.)</p> </li> <li> <p> <code>COMPLAINT</code> - The email was successfully delivered to the recipient’s mail server, but the recipient marked it as spam.</p> </li> <li> <p> <code>DELIVERY</code> - SES successfully delivered the email to the recipient's mail server.</p> </li> <li> <p> <code>OPEN</code> - The recipient received the message and opened it in their email client.</p> </li> <li> <p> <code>CLICK</code> - The recipient clicked one or more links in the email.</p> </li> <li> <p> <code>RENDERING_FAILURE</code> - The email wasn't sent because of a template rendering issue. This event type can occur when template data is missing, or when there is a mismatch between template parameters and data. (This event type only occurs when you send email using the <a href="https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_SendEmail.html"> <code>SendEmail</code> </a> or <a href="https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_SendBulkEmail.html"> <code>SendBulkEmail</code> </a> API operations.) </p> </li> <li> <p> <code>DELIVERY_DELAY</code> - The email couldn't be delivered to the recipient’s mail server because a temporary issue occurred. Delivery delays can occur, for example, when the recipient's inbox is full, or when the receiving email server experiences a transient issue.</p> </li> <li> <p> <code>SUBSCRIPTION</code> - The email was successfully delivered, but the recipient updated their subscription preferences by clicking on an <i>unsubscribe</i> link as part of your <a href="https://docs.aws.amazon.com/ses/latest/dg/sending-email-subscription-management.html">subscription management</a>.</p> </li> </ul>"""
    kinesis_firehose_destination: NotRequired[
        "capo_sesv2.types.kinesis_firehose_destination.KinesisFirehoseDestination"
    ]
    """<p>An object that defines an Amazon Kinesis Data Firehose destination for email events. You can use Amazon Kinesis Data Firehose to stream data to other services, such as Amazon S3 and Amazon Redshift.</p>"""
    cloud_watch_destination: NotRequired[
        "capo_sesv2.types.cloud_watch_destination.CloudWatchDestination"
    ]
    """<p>An object that defines an Amazon CloudWatch destination for email events. You can use Amazon CloudWatch to monitor and gain insights on your email sending metrics.</p>"""
    sns_destination: NotRequired["capo_sesv2.types.sns_destination.SnsDestination"]
    """<p>An object that defines an Amazon SNS destination for email events. You can use Amazon SNS to send notifications when certain email events occur.</p>"""
    event_bridge_destination: NotRequired[
        "capo_sesv2.types.event_bridge_destination.EventBridgeDestination"
    ]
    """<p>An object that defines an Amazon EventBridge destination for email events. You can use Amazon EventBridge to send notifications when certain email events occur.</p>"""
    pinpoint_destination: NotRequired[
        "capo_sesv2.types.pinpoint_destination.PinpointDestination"
    ]
    """<p>An object that defines an Amazon Pinpoint project destination for email events. You can send email event data to a Amazon Pinpoint project to view metrics using the Transactional Messaging dashboards that are built in to Amazon Pinpoint. For more information, see <a href="https://docs.aws.amazon.com/pinpoint/latest/userguide/analytics-transactional-messages.html">Transactional Messaging Charts</a> in the <i>Amazon Pinpoint User Guide</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EventDestination) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    out["Enabled"] = value.get("enabled", False)
    import capo_sesv2.types.event_types

    out["MatchingEventTypes"] = capo_sesv2.types.event_types.serialize_json(
        value["matching_event_types"]
    )
    if "kinesis_firehose_destination" in value:
        import capo_sesv2.types.kinesis_firehose_destination

        out["KinesisFirehoseDestination"] = (
            capo_sesv2.types.kinesis_firehose_destination.serialize_json(
                value["kinesis_firehose_destination"]
            )
        )
    if "cloud_watch_destination" in value:
        import capo_sesv2.types.cloud_watch_destination

        out["CloudWatchDestination"] = (
            capo_sesv2.types.cloud_watch_destination.serialize_json(
                value["cloud_watch_destination"]
            )
        )
    if "sns_destination" in value:
        import capo_sesv2.types.sns_destination

        out["SnsDestination"] = capo_sesv2.types.sns_destination.serialize_json(
            value["sns_destination"]
        )
    if "event_bridge_destination" in value:
        import capo_sesv2.types.event_bridge_destination

        out["EventBridgeDestination"] = (
            capo_sesv2.types.event_bridge_destination.serialize_json(
                value["event_bridge_destination"]
            )
        )
    if "pinpoint_destination" in value:
        import capo_sesv2.types.pinpoint_destination

        out["PinpointDestination"] = (
            capo_sesv2.types.pinpoint_destination.serialize_json(
                value["pinpoint_destination"]
            )
        )
    return out


def deserialize_json(data: dict) -> EventDestination:
    out: EventDestination = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("EventDestination.name required")
    if data.get("Enabled") is not None:
        out["enabled"] = data["Enabled"]
    else:
        out["enabled"] = False
    if data.get("MatchingEventTypes") is not None:
        import capo_sesv2.types.event_types

        out["matching_event_types"] = capo_sesv2.types.event_types.deserialize_json(
            data["MatchingEventTypes"]
        )
    else:
        raise DeserializationError("EventDestination.matching_event_types required")
    if data.get("KinesisFirehoseDestination") is not None:
        import capo_sesv2.types.kinesis_firehose_destination

        out["kinesis_firehose_destination"] = (
            capo_sesv2.types.kinesis_firehose_destination.deserialize_json(
                data["KinesisFirehoseDestination"]
            )
        )
    if data.get("CloudWatchDestination") is not None:
        import capo_sesv2.types.cloud_watch_destination

        out["cloud_watch_destination"] = (
            capo_sesv2.types.cloud_watch_destination.deserialize_json(
                data["CloudWatchDestination"]
            )
        )
    if data.get("SnsDestination") is not None:
        import capo_sesv2.types.sns_destination

        out["sns_destination"] = capo_sesv2.types.sns_destination.deserialize_json(
            data["SnsDestination"]
        )
    if data.get("EventBridgeDestination") is not None:
        import capo_sesv2.types.event_bridge_destination

        out["event_bridge_destination"] = (
            capo_sesv2.types.event_bridge_destination.deserialize_json(
                data["EventBridgeDestination"]
            )
        )
    if data.get("PinpointDestination") is not None:
        import capo_sesv2.types.pinpoint_destination

        out["pinpoint_destination"] = (
            capo_sesv2.types.pinpoint_destination.deserialize_json(
                data["PinpointDestination"]
            )
        )
    return out
