"""Generated from Smithy shape ``com.amazonaws.s3control#ReplicationTime``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_s3_control._protocol.xml import Element, SubElement
from capo_s3_control.errors import DeserializationError

if TYPE_CHECKING:
    import capo_s3_control.types.replication_time_status
    import capo_s3_control.types.replication_time_value


class ReplicationTime(TypedDict, closed=True):
    status: "capo_s3_control.types.replication_time_status.ReplicationTimeStatus"
    """<p>Specifies whether S3 Replication Time Control (S3 RTC) is enabled. </p>"""
    time: "capo_s3_control.types.replication_time_value.ReplicationTimeValue"
    """<p>A container that specifies the time by which replication should be complete for all objects and operations on objects. </p>"""


# --- restXml ser/de ---
def serialize_xml(value: ReplicationTime, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    import capo_s3_control.types.replication_time_status

    capo_s3_control.types.replication_time_status.serialize_xml(
        value["status"], el, "Status"
    )
    import capo_s3_control.types.replication_time_value

    capo_s3_control.types.replication_time_value.serialize_xml(
        value["time"], el, "Time"
    )


def deserialize_xml(el: Element) -> ReplicationTime:
    out: ReplicationTime = {}  # type: ignore[typeddict-item]
    child_status = el.find("Status")
    if child_status is not None:
        import capo_s3_control.types.replication_time_status

        out["status"] = capo_s3_control.types.replication_time_status.deserialize_xml(
            child_status
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_s3_control.types.replication_time_status.ReplicationTimeStatus", ""
        )
    child_time = el.find("Time")
    if child_time is not None:
        import capo_s3_control.types.replication_time_value

        out["time"] = capo_s3_control.types.replication_time_value.deserialize_xml(
            child_time
        )
    else:
        raise DeserializationError("ReplicationTime.time required")
    return out
