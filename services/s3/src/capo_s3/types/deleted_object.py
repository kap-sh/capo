"""Generated from Smithy shape ``com.amazonaws.s3#DeletedObject``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3.types.delete_marker
    import capo_s3.types.delete_marker_version_id
    import capo_s3.types.object_key
    import capo_s3.types.object_version_id


class DeletedObject(TypedDict, closed=True):
    key: NotRequired["capo_s3.types.object_key.ObjectKey"]
    """<p>The name of the deleted object.</p>"""
    version_id: NotRequired["capo_s3.types.object_version_id.ObjectVersionId"]
    """<p>The version ID of the deleted object.</p> <note> <p>This functionality is not supported for directory buckets.</p> </note>"""
    delete_marker: NotRequired["capo_s3.types.delete_marker.DeleteMarker"]
    """<p>Indicates whether the specified object version that was permanently deleted was (true) or was not (false) a delete marker before deletion. In a simple DELETE, this header indicates whether (true) or not (false) the current version of the object is a delete marker. To learn more about delete markers, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/DeleteMarker.html">Working with delete markers</a>.</p> <note> <p>This functionality is not supported for directory buckets.</p> </note>"""
    delete_marker_version_id: NotRequired[
        "capo_s3.types.delete_marker_version_id.DeleteMarkerVersionId"
    ]
    """<p>The version ID of the delete marker created as a result of the DELETE operation. If you delete a specific object version, the value returned by this header is the version ID of the object version deleted.</p> <note> <p>This functionality is not supported for directory buckets.</p> </note>"""


# --- restXml ser/de ---
def serialize_xml(value: DeletedObject, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "key" in value:
        SubElement(el, "Key").text = str(value["key"])
    if "version_id" in value:
        SubElement(el, "VersionId").text = str(value["version_id"])
    if "delete_marker" in value:
        SubElement(el, "DeleteMarker").text = (
            "true" if value["delete_marker"] else "false"
        )
    if "delete_marker_version_id" in value:
        SubElement(el, "DeleteMarkerVersionId").text = str(
            value["delete_marker_version_id"]
        )


def deserialize_xml(el: Element) -> DeletedObject:
    out: DeletedObject = {}  # type: ignore[typeddict-item]
    child_key = el.find("Key")
    if child_key is not None:
        out["key"] = str(child_key.text or "")
    child_version_id = el.find("VersionId")
    if child_version_id is not None:
        out["version_id"] = str(child_version_id.text or "")
    child_delete_marker = el.find("DeleteMarker")
    if child_delete_marker is not None:
        out["delete_marker"] = (child_delete_marker.text or "").lower() == "true"
    child_delete_marker_version_id = el.find("DeleteMarkerVersionId")
    if child_delete_marker_version_id is not None:
        out["delete_marker_version_id"] = str(child_delete_marker_version_id.text or "")
    return out
