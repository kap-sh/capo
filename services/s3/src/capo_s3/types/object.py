"""Generated from Smithy shape ``com.amazonaws.s3#Object``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3.types.checksum_algorithm_list
    import capo_s3.types.checksum_type
    import capo_s3.types.e_tag
    import capo_s3.types.last_modified
    import capo_s3.types.object_key
    import capo_s3.types.object_storage_class
    import capo_s3.types.owner
    import capo_s3.types.restore_status
    import capo_s3.types.size


class Object(TypedDict, closed=True):
    key: NotRequired["capo_s3.types.object_key.ObjectKey"]
    """<p>The name that you assign to an object. You use the object key to retrieve the object.</p>"""
    last_modified: NotRequired["capo_s3.types.last_modified.LastModified"]
    """<p>Creation date of the object.</p>"""
    e_tag: NotRequired["capo_s3.types.e_tag.ETag"]
    """<p>The entity tag is a hash of the object. The ETag reflects changes only to the contents of an object, not its metadata. The ETag may or may not be an MD5 digest of the object data. Whether or not it is depends on how the object was created and how it is encrypted as described below:</p> <ul> <li> <p>Objects created by the PUT Object, POST Object, or Copy operation, or through the Amazon Web Services Management Console, and are encrypted by SSE-S3 or plaintext, have ETags that are an MD5 digest of their object data.</p> </li> <li> <p>Objects created by the PUT Object, POST Object, or Copy operation, or through the Amazon Web Services Management Console, and are encrypted by SSE-C or SSE-KMS, have ETags that are not an MD5 digest of their object data.</p> </li> <li> <p>If an object is created by either the Multipart Upload or Part Copy operation, the ETag is not an MD5 digest, regardless of the method of encryption. If an object is larger than 16 MB, the Amazon Web Services Management Console will upload or copy that object as a Multipart Upload, and therefore the ETag will not be an MD5 digest.</p> </li> </ul> <note> <p> <b>Directory buckets</b> - MD5 is not supported by directory buckets.</p> </note>"""
    checksum_algorithm: NotRequired[
        "capo_s3.types.checksum_algorithm_list.ChecksumAlgorithmList"
    ]
    """<p>The algorithm that was used to create a checksum of the object.</p>"""
    checksum_type: NotRequired["capo_s3.types.checksum_type.ChecksumType"]
    """<p>The checksum type that is used to calculate the object’s checksum value. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html">Checking object integrity</a> in the <i>Amazon S3 User Guide</i>.</p>"""
    size: NotRequired["capo_s3.types.size.Size"]
    """<p>Size in bytes of the object</p>"""
    storage_class: NotRequired["capo_s3.types.object_storage_class.ObjectStorageClass"]
    """<p>The class of storage used to store the object.</p> <note> <p> <b>Directory buckets</b> - Directory buckets only support <code>EXPRESS_ONEZONE</code> (the S3 Express One Zone storage class) in Availability Zones and <code>ONEZONE_IA</code> (the S3 One Zone-Infrequent Access storage class) in Dedicated Local Zones.</p> </note>"""
    owner: NotRequired["capo_s3.types.owner.Owner"]
    """<p>The owner of the object</p> <note> <p> <b>Directory buckets</b> - The bucket owner is returned as the object owner.</p> </note>"""
    restore_status: NotRequired["capo_s3.types.restore_status.RestoreStatus"]
    """<p>Specifies the restoration status of an object. Objects in certain storage classes must be restored before they can be retrieved. For more information about these storage classes and how to work with archived objects, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/archived-objects.html"> Working with archived objects</a> in the <i>Amazon S3 User Guide</i>.</p> <note> <p>This functionality is not supported for directory buckets. Directory buckets only support <code>EXPRESS_ONEZONE</code> (the S3 Express One Zone storage class) in Availability Zones and <code>ONEZONE_IA</code> (the S3 One Zone-Infrequent Access storage class) in Dedicated Local Zones.</p> </note>"""


# --- restXml ser/de ---
def serialize_xml(value: Object, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "key" in value:
        SubElement(el, "Key").text = str(value["key"])
    if "last_modified" in value:
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
    if "checksum_type" in value:
        import capo_s3.types.checksum_type

        capo_s3.types.checksum_type.serialize_xml(
            value["checksum_type"], el, "ChecksumType"
        )
    if "size" in value:
        SubElement(el, "Size").text = str(value["size"])
    if "storage_class" in value:
        import capo_s3.types.object_storage_class

        capo_s3.types.object_storage_class.serialize_xml(
            value["storage_class"], el, "StorageClass"
        )
    if "owner" in value:
        import capo_s3.types.owner

        capo_s3.types.owner.serialize_xml(value["owner"], el, "Owner")
    if "restore_status" in value:
        import capo_s3.types.restore_status

        capo_s3.types.restore_status.serialize_xml(
            value["restore_status"], el, "RestoreStatus"
        )


def deserialize_xml(el: Element) -> Object:
    out: Object = {}  # type: ignore[typeddict-item]
    child_key = el.find("Key")
    if child_key is not None:
        out["key"] = str(child_key.text or "")
    child_last_modified = el.find("LastModified")
    if child_last_modified is not None:
        import capo_s3.types.last_modified

        out["last_modified"] = capo_s3.types.last_modified.deserialize_xml(
            child_last_modified
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
    child_checksum_type = el.find("ChecksumType")
    if child_checksum_type is not None:
        import capo_s3.types.checksum_type

        out["checksum_type"] = capo_s3.types.checksum_type.deserialize_xml(
            child_checksum_type
        )
    child_size = el.find("Size")
    if child_size is not None:
        out["size"] = int(child_size.text or "")
    child_storage_class = el.find("StorageClass")
    if child_storage_class is not None:
        import capo_s3.types.object_storage_class

        out["storage_class"] = capo_s3.types.object_storage_class.deserialize_xml(
            child_storage_class
        )
    child_owner = el.find("Owner")
    if child_owner is not None:
        import capo_s3.types.owner

        out["owner"] = capo_s3.types.owner.deserialize_xml(child_owner)
    child_restore_status = el.find("RestoreStatus")
    if child_restore_status is not None:
        import capo_s3.types.restore_status

        out["restore_status"] = capo_s3.types.restore_status.deserialize_xml(
            child_restore_status
        )
    return out
