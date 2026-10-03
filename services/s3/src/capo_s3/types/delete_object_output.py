"""Generated from Smithy shape ``com.amazonaws.s3#DeleteObjectOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3.types.delete_marker
    import capo_s3.types.object_version_id
    import capo_s3.types.request_charged


class DeleteObjectOutput(TypedDict, closed=True):
    delete_marker: NotRequired["capo_s3.types.delete_marker.DeleteMarker"]
    """<p>Indicates whether the specified object version that was permanently deleted was (true) or was not (false) a delete marker before deletion. In a simple DELETE, this header indicates whether (true) or not (false) the current version of the object is a delete marker. To learn more about delete markers, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/DeleteMarker.html">Working with delete markers</a>.</p> <note> <p>This functionality is not supported for directory buckets.</p> </note>"""
    version_id: NotRequired["capo_s3.types.object_version_id.ObjectVersionId"]
    """<p>Returns the version ID of the delete marker created as a result of the DELETE operation.</p> <note> <p>This functionality is not supported for directory buckets.</p> </note>"""
    request_charged: NotRequired["capo_s3.types.request_charged.RequestCharged"]


# --- restXml ser/de ---
def serialize_xml(value: DeleteObjectOutput, parent: Element, tag: str) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> DeleteObjectOutput:
    out: DeleteObjectOutput = {}  # type: ignore[typeddict-item]
    return out
