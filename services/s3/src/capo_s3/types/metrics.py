"""Generated from Smithy shape ``com.amazonaws.s3#Metrics``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3.types.metrics_status
    import capo_s3.types.replication_time_value


class Metrics(TypedDict, closed=True):
    status: "capo_s3.types.metrics_status.MetricsStatus"
    """<p> Specifies whether the replication metrics are enabled. </p>"""
    event_threshold: NotRequired[
        "capo_s3.types.replication_time_value.ReplicationTimeValue"
    ]
    """<p> A container specifying the time threshold for emitting the <code>s3:Replication:OperationMissedThreshold</code> event. </p>"""


# --- restXml ser/de ---
def serialize_xml(value: Metrics, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    import capo_s3.types.metrics_status

    capo_s3.types.metrics_status.serialize_xml(value["status"], el, "Status")
    if "event_threshold" in value:
        import capo_s3.types.replication_time_value

        capo_s3.types.replication_time_value.serialize_xml(
            value["event_threshold"], el, "EventThreshold"
        )


def deserialize_xml(el: Element) -> Metrics:
    out: Metrics = {}  # type: ignore[typeddict-item]
    child_status = el.find("Status")
    if child_status is not None:
        import capo_s3.types.metrics_status

        out["status"] = capo_s3.types.metrics_status.deserialize_xml(child_status)
    else:
        import typing

        out["status"] = typing.cast("capo_s3.types.metrics_status.MetricsStatus", "")
    child_event_threshold = el.find("EventThreshold")
    if child_event_threshold is not None:
        import capo_s3.types.replication_time_value

        out["event_threshold"] = capo_s3.types.replication_time_value.deserialize_xml(
            child_event_threshold
        )
    return out
