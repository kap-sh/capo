"""Generated from Smithy shape ``com.amazonaws.s3#S3Location``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_s3._protocol.xml import Element, SubElement
from capo_s3.errors import DeserializationError

if TYPE_CHECKING:
    import capo_s3.types.bucket_name
    import capo_s3.types.encryption
    import capo_s3.types.grants
    import capo_s3.types.location_prefix
    import capo_s3.types.object_canned_acl
    import capo_s3.types.storage_class
    import capo_s3.types.tagging
    import capo_s3.types.user_metadata


class S3Location(TypedDict, closed=True):
    bucket_name: "capo_s3.types.bucket_name.BucketName"
    """<p>The name of the bucket where the restore results will be placed.</p>"""
    prefix: "capo_s3.types.location_prefix.LocationPrefix"
    """<p>The prefix that is prepended to the restore results for this request.</p>"""
    encryption: NotRequired["capo_s3.types.encryption.Encryption"]
    canned_acl: NotRequired["capo_s3.types.object_canned_acl.ObjectCannedACL"]
    """<p>The canned ACL to apply to the restore results.</p>"""
    access_control_list: NotRequired["capo_s3.types.grants.Grants"]
    """<p>A list of grants that control access to the staged results.</p>"""
    tagging: NotRequired["capo_s3.types.tagging.Tagging"]
    """<p>The tag-set that is applied to the restore results.</p>"""
    user_metadata: NotRequired["capo_s3.types.user_metadata.UserMetadata"]
    """<p>A list of metadata to store with the restore results in S3.</p>"""
    storage_class: NotRequired["capo_s3.types.storage_class.StorageClass"]
    """<p>The class of storage used to store the restore results.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: S3Location, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "BucketName").text = str(value["bucket_name"])
    SubElement(el, "Prefix").text = str(value["prefix"])
    if "encryption" in value:
        import capo_s3.types.encryption

        capo_s3.types.encryption.serialize_xml(value["encryption"], el, "Encryption")
    if "canned_acl" in value:
        import capo_s3.types.object_canned_acl

        capo_s3.types.object_canned_acl.serialize_xml(
            value["canned_acl"], el, "CannedACL"
        )
    if "access_control_list" in value:
        import capo_s3.types.grants

        capo_s3.types.grants.serialize_xml(
            value["access_control_list"], el, "AccessControlList"
        )
    if "tagging" in value:
        import capo_s3.types.tagging

        capo_s3.types.tagging.serialize_xml(value["tagging"], el, "Tagging")
    if "user_metadata" in value:
        import capo_s3.types.user_metadata

        capo_s3.types.user_metadata.serialize_xml(
            value["user_metadata"], el, "UserMetadata"
        )
    if "storage_class" in value:
        import capo_s3.types.storage_class

        capo_s3.types.storage_class.serialize_xml(
            value["storage_class"], el, "StorageClass"
        )


def deserialize_xml(el: Element) -> S3Location:
    out: S3Location = {}  # type: ignore[typeddict-item]
    child_bucket_name = el.find("BucketName")
    if child_bucket_name is not None:
        out["bucket_name"] = str(child_bucket_name.text or "")
    else:
        raise DeserializationError("S3Location.bucket_name required")
    child_prefix = el.find("Prefix")
    if child_prefix is not None:
        out["prefix"] = str(child_prefix.text or "")
    else:
        raise DeserializationError("S3Location.prefix required")
    child_encryption = el.find("Encryption")
    if child_encryption is not None:
        import capo_s3.types.encryption

        out["encryption"] = capo_s3.types.encryption.deserialize_xml(child_encryption)
    child_canned_acl = el.find("CannedACL")
    if child_canned_acl is not None:
        import capo_s3.types.object_canned_acl

        out["canned_acl"] = capo_s3.types.object_canned_acl.deserialize_xml(
            child_canned_acl
        )
    child_access_control_list = el.find("AccessControlList")
    if child_access_control_list is not None:
        import capo_s3.types.grants

        out["access_control_list"] = capo_s3.types.grants.deserialize_xml(
            child_access_control_list
        )
    child_tagging = el.find("Tagging")
    if child_tagging is not None:
        import capo_s3.types.tagging

        out["tagging"] = capo_s3.types.tagging.deserialize_xml(child_tagging)
    child_user_metadata = el.find("UserMetadata")
    if child_user_metadata is not None:
        import capo_s3.types.user_metadata

        out["user_metadata"] = capo_s3.types.user_metadata.deserialize_xml(
            child_user_metadata
        )
    child_storage_class = el.find("StorageClass")
    if child_storage_class is not None:
        import capo_s3.types.storage_class

        out["storage_class"] = capo_s3.types.storage_class.deserialize_xml(
            child_storage_class
        )
    return out


def redact_sensitive(value: S3Location) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "encryption" in value:
        import capo_s3.types.encryption

        out["encryption"] = capo_s3.types.encryption.redact_sensitive(
            value["encryption"]
        )
    return out
