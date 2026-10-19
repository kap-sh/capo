"""Generated from Smithy shape ``com.amazonaws.s3#ReplicaModifications``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3.types.replica_modifications_status


class ReplicaModifications(TypedDict, closed=True):
    status: "capo_s3.types.replica_modifications_status.ReplicaModificationsStatus"
    """<p>Specifies whether Amazon S3 replicates modifications on replicas.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: ReplicaModifications, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    import capo_s3.types.replica_modifications_status

    capo_s3.types.replica_modifications_status.serialize_xml(
        value["status"], el, "Status"
    )


def deserialize_xml(el: Element) -> ReplicaModifications:
    out: ReplicaModifications = {}  # type: ignore[typeddict-item]
    child_status = el.find("Status")
    if child_status is not None:
        import capo_s3.types.replica_modifications_status

        out["status"] = capo_s3.types.replica_modifications_status.deserialize_xml(
            child_status
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_s3.types.replica_modifications_status.ReplicaModificationsStatus", ""
        )
    return out
