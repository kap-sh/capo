"""Generated from Smithy shape ``com.amazonaws.s3control#ExistingObjectReplication``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3_control.types.existing_object_replication_status


class ExistingObjectReplication(TypedDict, closed=True):
    status: "capo_s3_control.types.existing_object_replication_status.ExistingObjectReplicationStatus"
    """<p>Specifies whether Amazon S3 replicates existing source bucket objects. </p>"""


# --- restXml ser/de ---
def serialize_xml(value: ExistingObjectReplication, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    import capo_s3_control.types.existing_object_replication_status

    capo_s3_control.types.existing_object_replication_status.serialize_xml(
        value["status"], el, "Status"
    )


def deserialize_xml(el: Element) -> ExistingObjectReplication:
    out: ExistingObjectReplication = {}  # type: ignore[typeddict-item]
    child_status = el.find("Status")
    if child_status is not None:
        import capo_s3_control.types.existing_object_replication_status

        out["status"] = (
            capo_s3_control.types.existing_object_replication_status.deserialize_xml(
                child_status
            )
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_s3_control.types.existing_object_replication_status.ExistingObjectReplicationStatus",
            "",
        )
    return out
