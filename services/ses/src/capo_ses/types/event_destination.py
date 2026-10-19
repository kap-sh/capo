"""Generated from Smithy shape ``com.amazonaws.ses#EventDestination``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ses._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ses.types.cloud_watch_destination
    import capo_ses.types.enabled
    import capo_ses.types.event_destination_name
    import capo_ses.types.event_types
    import capo_ses.types.kinesis_firehose_destination
    import capo_ses.types.sns_destination


class EventDestination(TypedDict, closed=True):
    name: "capo_ses.types.event_destination_name.EventDestinationName"
    """<p>The name of the event destination. The name must meet the following requirements:</p> <ul> <li> <p>Contain only ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), or dashes (-).</p> </li> <li> <p>Contain 64 characters or fewer.</p> </li> </ul>"""
    enabled: "capo_ses.types.enabled.Enabled"
    """<p>Sets whether Amazon SES publishes events to this destination when you send an email with the associated configuration set. Set to <code>true</code> to enable publishing to this destination; set to <code>false</code> to prevent publishing to this destination. The default value is <code>false</code>.</p>"""
    matching_event_types: "capo_ses.types.event_types.EventTypes"
    """<p>The type of email sending events to publish to the event destination.</p> <ul> <li> <p> <code>send</code> - The call was successful and Amazon SES is attempting to deliver the email.</p> </li> <li> <p> <code>reject</code> - Amazon SES determined that the email contained a virus and rejected it.</p> </li> <li> <p> <code>bounce</code> - The recipient's mail server permanently rejected the email. This corresponds to a hard bounce.</p> </li> <li> <p> <code>complaint</code> - The recipient marked the email as spam.</p> </li> <li> <p> <code>delivery</code> - Amazon SES successfully delivered the email to the recipient's mail server.</p> </li> <li> <p> <code>open</code> - The recipient received the email and opened it in their email client.</p> </li> <li> <p> <code>click</code> - The recipient clicked one or more links in the email.</p> </li> <li> <p> <code>renderingFailure</code> - Amazon SES did not send the email because of a template rendering issue.</p> </li> </ul>"""
    kinesis_firehose_destination: NotRequired[
        "capo_ses.types.kinesis_firehose_destination.KinesisFirehoseDestination"
    ]
    """<p>An object that contains the delivery stream ARN and the IAM role ARN associated with an Amazon Kinesis Firehose event destination.</p>"""
    cloud_watch_destination: NotRequired[
        "capo_ses.types.cloud_watch_destination.CloudWatchDestination"
    ]
    """<p>An object that contains the names, default values, and sources of the dimensions associated with an Amazon CloudWatch event destination.</p>"""
    sns_destination: NotRequired["capo_ses.types.sns_destination.SNSDestination"]
    """<p>An object that contains the topic ARN associated with an Amazon Simple Notification Service (Amazon SNS) event destination.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: EventDestination, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    pairs.append((f"{key_prefix}Name", str(value["name"])))
    pairs.append(
        (f"{key_prefix}Enabled", "true" if value.get("enabled", False) else "false")
    )
    import capo_ses.types.event_types

    capo_ses.types.event_types.serialize_query(
        value["matching_event_types"], pairs, f"{key_prefix}MatchingEventTypes"
    )
    if "kinesis_firehose_destination" in value:
        import capo_ses.types.kinesis_firehose_destination

        capo_ses.types.kinesis_firehose_destination.serialize_query(
            value["kinesis_firehose_destination"],
            pairs,
            f"{key_prefix}KinesisFirehoseDestination",
        )
    if "cloud_watch_destination" in value:
        import capo_ses.types.cloud_watch_destination

        capo_ses.types.cloud_watch_destination.serialize_query(
            value["cloud_watch_destination"],
            pairs,
            f"{key_prefix}CloudWatchDestination",
        )
    if "sns_destination" in value:
        import capo_ses.types.sns_destination

        capo_ses.types.sns_destination.serialize_query(
            value["sns_destination"], pairs, f"{key_prefix}SNSDestination"
        )


def deserialize_query(el: Element) -> EventDestination:
    out: EventDestination = {}  # type: ignore[typeddict-item]
    child_name = el.find("Name")
    if child_name is not None:
        out["name"] = str(child_name.text or "")
    else:
        out["name"] = ""
    child_enabled = el.find("Enabled")
    if child_enabled is not None:
        out["enabled"] = (child_enabled.text or "").lower() == "true"
    else:
        out["enabled"] = False
    child_matching_event_types = el.find("MatchingEventTypes")
    if child_matching_event_types is not None:
        import capo_ses.types.event_types

        out["matching_event_types"] = capo_ses.types.event_types.deserialize_query(
            child_matching_event_types
        )
    else:
        out["matching_event_types"] = []
    child_kinesis_firehose_destination = el.find("KinesisFirehoseDestination")
    if child_kinesis_firehose_destination is not None:
        import capo_ses.types.kinesis_firehose_destination

        out["kinesis_firehose_destination"] = (
            capo_ses.types.kinesis_firehose_destination.deserialize_query(
                child_kinesis_firehose_destination
            )
        )
    child_cloud_watch_destination = el.find("CloudWatchDestination")
    if child_cloud_watch_destination is not None:
        import capo_ses.types.cloud_watch_destination

        out["cloud_watch_destination"] = (
            capo_ses.types.cloud_watch_destination.deserialize_query(
                child_cloud_watch_destination
            )
        )
    child_sns_destination = el.find("SNSDestination")
    if child_sns_destination is not None:
        import capo_ses.types.sns_destination

        out["sns_destination"] = capo_ses.types.sns_destination.deserialize_query(
            child_sns_destination
        )
    return out
