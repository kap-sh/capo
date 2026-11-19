"""Generated from Smithy shape ``com.amazonaws.s3#AbortMultipartUploadOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3.types.object_version_id
    import capo_s3.types.request_charged


class AbortMultipartUploadOutput(TypedDict, closed=True):
    request_charged: NotRequired["capo_s3.types.request_charged.RequestCharged"]
    version_id: NotRequired["capo_s3.types.object_version_id.ObjectVersionId"]
    """<p>Version ID of the object.</p> <p>Returns the Version ID of the object for the aborted multipart upload, if bucket versioning is enabled.</p> <note> <p>This functionality is not supported for directory buckets.</p> </note>"""


# --- restXml ser/de ---
def serialize_xml(value: AbortMultipartUploadOutput, parent: Element, tag: str) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> AbortMultipartUploadOutput:
    out: AbortMultipartUploadOutput = {}  # type: ignore[typeddict-item]
    return out
