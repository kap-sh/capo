"""Generated from Smithy shape ``com.amazonaws.s3control#JobManifestLocation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3_control._protocol.xml import Element, SubElement
from capo_s3_control.errors import DeserializationError

if TYPE_CHECKING:
    import capo_s3_control.types.non_empty_max_length1024_string
    import capo_s3_control.types.s3_key_arn_string
    import capo_s3_control.types.s3_object_version_id


class JobManifestLocation(TypedDict, closed=True):
    object_arn: "capo_s3_control.types.s3_key_arn_string.S3KeyArnString"
    """<p>The Amazon Resource Name (ARN) for a manifest object.</p> <important> <p>When you're using XML requests, you must replace special characters (such as carriage returns) in object keys with their equivalent XML entity codes. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-keys.html#object-key-xml-related-constraints"> XML-related object key constraints</a> in the <i>Amazon S3 User Guide</i>.</p> </important>"""
    object_version_id: NotRequired[
        "capo_s3_control.types.s3_object_version_id.S3ObjectVersionId"
    ]
    """<p>The optional version ID to identify a specific version of the manifest object.</p>"""
    e_tag: "capo_s3_control.types.non_empty_max_length1024_string.NonEmptyMaxLength1024String"
    """<p>The ETag for the specified manifest object.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: JobManifestLocation, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "ObjectArn").text = str(value["object_arn"])
    if "object_version_id" in value:
        SubElement(el, "ObjectVersionId").text = str(value["object_version_id"])
    SubElement(el, "ETag").text = str(value["e_tag"])


def deserialize_xml(el: Element) -> JobManifestLocation:
    out: JobManifestLocation = {}  # type: ignore[typeddict-item]
    child_object_arn = el.find("ObjectArn")
    if child_object_arn is not None:
        out["object_arn"] = str(child_object_arn.text or "")
    else:
        raise DeserializationError("JobManifestLocation.object_arn required")
    child_object_version_id = el.find("ObjectVersionId")
    if child_object_version_id is not None:
        out["object_version_id"] = str(child_object_version_id.text or "")
    child_e_tag = el.find("ETag")
    if child_e_tag is not None:
        out["e_tag"] = str(child_e_tag.text or "")
    else:
        raise DeserializationError("JobManifestLocation.e_tag required")
    return out
