"""Generated from Smithy shape ``com.amazonaws.s3#ObjectIdentifier``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3._protocol.xml import Element, SubElement
from capo_s3.errors import DeserializationError

if TYPE_CHECKING:
    import capo_s3.types.e_tag
    import capo_s3.types.last_modified_time
    import capo_s3.types.object_key
    import capo_s3.types.object_version_id
    import capo_s3.types.size


class ObjectIdentifier(TypedDict, closed=True):
    key: "capo_s3.types.object_key.ObjectKey"
    """<p>Key name of the object.</p> <important> <p>Replacement must be made for object keys containing special characters (such as carriage returns) when using XML requests. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-keys.html#object-key-xml-related-constraints"> XML related object key constraints</a>.</p> </important>"""
    version_id: NotRequired["capo_s3.types.object_version_id.ObjectVersionId"]
    """<p>Version ID for the specific version of the object to delete.</p> <note> <p>This functionality is not supported for directory buckets.</p> </note>"""
    e_tag: NotRequired["capo_s3.types.e_tag.ETag"]
    """<p>An entity tag (ETag) is an identifier assigned by a web server to a specific version of a resource found at a URL. This header field makes the request method conditional on <code>ETags</code>. </p> <note> <p>Entity tags (ETags) for S3 Express One Zone are random alphanumeric strings unique to the object. </p> </note>"""
    last_modified_time: NotRequired["capo_s3.types.last_modified_time.LastModifiedTime"]
    """<p>If present, the objects are deleted only if its modification times matches the provided <code>Timestamp</code>. </p> <note> <p>This functionality is only supported for directory buckets.</p> </note>"""
    size: NotRequired["capo_s3.types.size.Size"]
    """<p>If present, the objects are deleted only if its size matches the provided size in bytes. </p> <note> <p>This functionality is only supported for directory buckets.</p> </note>"""


# --- restXml ser/de ---
def serialize_xml(value: ObjectIdentifier, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "Key").text = str(value["key"])
    if "version_id" in value:
        SubElement(el, "VersionId").text = str(value["version_id"])
    if "e_tag" in value:
        SubElement(el, "ETag").text = str(value["e_tag"])
    if "last_modified_time" in value:
        import capo_s3.types.last_modified_time

        capo_s3.types.last_modified_time.serialize_xml(
            value["last_modified_time"], el, "LastModifiedTime"
        )
    if "size" in value:
        SubElement(el, "Size").text = str(value["size"])


def deserialize_xml(el: Element) -> ObjectIdentifier:
    out: ObjectIdentifier = {}  # type: ignore[typeddict-item]
    child_key = el.find("Key")
    if child_key is not None:
        out["key"] = str(child_key.text or "")
    else:
        raise DeserializationError("ObjectIdentifier.key required")
    child_version_id = el.find("VersionId")
    if child_version_id is not None:
        out["version_id"] = str(child_version_id.text or "")
    child_e_tag = el.find("ETag")
    if child_e_tag is not None:
        out["e_tag"] = str(child_e_tag.text or "")
    child_last_modified_time = el.find("LastModifiedTime")
    if child_last_modified_time is not None:
        import capo_s3.types.last_modified_time

        out["last_modified_time"] = capo_s3.types.last_modified_time.deserialize_xml(
            child_last_modified_time
        )
    child_size = el.find("Size")
    if child_size is not None:
        out["size"] = int(child_size.text or "")
    return out
