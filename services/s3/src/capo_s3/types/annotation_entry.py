"""Generated from Smithy shape ``com.amazonaws.s3#AnnotationEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3.types.annotation_name
    import capo_s3.types.checksum_algorithm_list
    import capo_s3.types.e_tag
    import capo_s3.types.last_modified
    import capo_s3.types.replication_status
    import capo_s3.types.size


class AnnotationEntry(TypedDict, closed=True):
    annotation_name: "capo_s3.types.annotation_name.AnnotationName"
    """<p>The name of the annotation.</p>"""
    last_modified: "capo_s3.types.last_modified.LastModified"
    """<p>The date and time the annotation was last modified.</p>"""
    e_tag: NotRequired["capo_s3.types.e_tag.ETag"]
    """<p>The entity tag of the annotation.</p>"""
    checksum_algorithm: NotRequired[
        "capo_s3.types.checksum_algorithm_list.ChecksumAlgorithmList"
    ]
    """<p>The checksum algorithm used for the annotation.</p>"""
    size: "capo_s3.types.size.Size"
    """<p>The size of the annotation payload, in bytes.</p>"""
    replication_status: NotRequired[
        "capo_s3.types.replication_status.ReplicationStatus"
    ]
    """<p>The replication status of the annotation.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: AnnotationEntry, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "AnnotationName").text = str(value["annotation_name"])
    import capo_s3.types.last_modified

    capo_s3.types.last_modified.serialize_xml(
        value["last_modified"], el, "LastModified"
    )
    if "e_tag" in value:
        SubElement(el, "ETag").text = str(value["e_tag"])
    if "checksum_algorithm" in value:
        import capo_s3.types.checksum_algorithm_list

        capo_s3.types.checksum_algorithm_list.serialize_xml_flat(
            value["checksum_algorithm"], el, "ChecksumAlgorithm"
        )
    SubElement(el, "Size").text = str(value["size"])
    if "replication_status" in value:
        import capo_s3.types.replication_status

        capo_s3.types.replication_status.serialize_xml(
            value["replication_status"], el, "ReplicationStatus"
        )


def deserialize_xml(el: Element) -> AnnotationEntry:
    out: AnnotationEntry = {}  # type: ignore[typeddict-item]
    child_annotation_name = el.find("AnnotationName")
    if child_annotation_name is not None:
        out["annotation_name"] = str(child_annotation_name.text or "")
    else:
        out["annotation_name"] = ""
    child_last_modified = el.find("LastModified")
    if child_last_modified is not None:
        import capo_s3.types.last_modified

        out["last_modified"] = capo_s3.types.last_modified.deserialize_xml(
            child_last_modified
        )
    else:
        import datetime

        out["last_modified"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    child_e_tag = el.find("ETag")
    if child_e_tag is not None:
        out["e_tag"] = str(child_e_tag.text or "")
    if el.find("ChecksumAlgorithm") is not None:
        import capo_s3.types.checksum_algorithm_list

        out["checksum_algorithm"] = (
            capo_s3.types.checksum_algorithm_list.deserialize_xml_flat(
                el, "ChecksumAlgorithm"
            )
        )
    child_size = el.find("Size")
    if child_size is not None:
        out["size"] = int(child_size.text or "")
    else:
        out["size"] = 0
    child_replication_status = el.find("ReplicationStatus")
    if child_replication_status is not None:
        import capo_s3.types.replication_status

        out["replication_status"] = capo_s3.types.replication_status.deserialize_xml(
            child_replication_status
        )
    return out
