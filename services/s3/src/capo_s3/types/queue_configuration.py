"""Generated from Smithy shape ``com.amazonaws.s3#QueueConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3.types.event_list
    import capo_s3.types.notification_configuration_filter
    import capo_s3.types.notification_id
    import capo_s3.types.queue_arn


class QueueConfiguration(TypedDict, closed=True):
    id: NotRequired["capo_s3.types.notification_id.NotificationId"]
    queue_arn: "capo_s3.types.queue_arn.QueueArn"
    """<p>The Amazon Resource Name (ARN) of the Amazon SQS queue to which Amazon S3 publishes a message when it detects events of the specified type.</p>"""
    events: "capo_s3.types.event_list.EventList"
    """<p>A collection of bucket events for which to send notifications</p>"""
    filter: NotRequired[
        "capo_s3.types.notification_configuration_filter.NotificationConfigurationFilter"
    ]


# --- restXml ser/de ---
def serialize_xml(value: QueueConfiguration, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "id" in value:
        SubElement(el, "Id").text = str(value["id"])
    SubElement(el, "Queue").text = str(value["queue_arn"])
    import capo_s3.types.event_list

    capo_s3.types.event_list.serialize_xml_flat(value["events"], el, "Event")
    if "filter" in value:
        import capo_s3.types.notification_configuration_filter

        capo_s3.types.notification_configuration_filter.serialize_xml(
            value["filter"], el, "Filter"
        )


def deserialize_xml(el: Element) -> QueueConfiguration:
    out: QueueConfiguration = {}  # type: ignore[typeddict-item]
    child_id = el.find("Id")
    if child_id is not None:
        out["id"] = str(child_id.text or "")
    child_queue_arn = el.find("Queue")
    if child_queue_arn is not None:
        out["queue_arn"] = str(child_queue_arn.text or "")
    else:
        out["queue_arn"] = ""
    if el.find("Event") is not None:
        import capo_s3.types.event_list

        out["events"] = capo_s3.types.event_list.deserialize_xml_flat(el, "Event")
    else:
        out["events"] = []
    child_filter = el.find("Filter")
    if child_filter is not None:
        import capo_s3.types.notification_configuration_filter

        out["filter"] = capo_s3.types.notification_configuration_filter.deserialize_xml(
            child_filter
        )
    return out
