"""Generated from Smithy shape ``com.amazonaws.s3#MultipartUpload``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3.types.checksum_algorithm
    import capo_s3.types.checksum_type
    import capo_s3.types.initiated
    import capo_s3.types.initiator
    import capo_s3.types.multipart_upload_id
    import capo_s3.types.object_key
    import capo_s3.types.owner
    import capo_s3.types.storage_class


class MultipartUpload(TypedDict, closed=True):
    upload_id: NotRequired["capo_s3.types.multipart_upload_id.MultipartUploadId"]
    """<p>Upload ID that identifies the multipart upload.</p>"""
    key: NotRequired["capo_s3.types.object_key.ObjectKey"]
    """<p>Key of the object for which the multipart upload was initiated.</p>"""
    initiated: NotRequired["capo_s3.types.initiated.Initiated"]
    """<p>Date and time at which the multipart upload was initiated.</p>"""
    storage_class: NotRequired["capo_s3.types.storage_class.StorageClass"]
    """<p>The class of storage used to store the object.</p> <note> <p> <b>Directory buckets</b> - Directory buckets only support <code>EXPRESS_ONEZONE</code> (the S3 Express One Zone storage class) in Availability Zones and <code>ONEZONE_IA</code> (the S3 One Zone-Infrequent Access storage class) in Dedicated Local Zones.</p> </note>"""
    owner: NotRequired["capo_s3.types.owner.Owner"]
    """<p>Specifies the owner of the object that is part of the multipart upload. </p> <note> <p> <b>Directory buckets</b> - The bucket owner is returned as the object owner for all the objects.</p> </note>"""
    initiator: NotRequired["capo_s3.types.initiator.Initiator"]
    """<p>Identifies who initiated the multipart upload.</p>"""
    checksum_algorithm: NotRequired[
        "capo_s3.types.checksum_algorithm.ChecksumAlgorithm"
    ]
    """<p>The algorithm that was used to create a checksum of the object.</p>"""
    checksum_type: NotRequired["capo_s3.types.checksum_type.ChecksumType"]
    """<p>The checksum type that is used to calculate the object’s checksum value. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html">Checking object integrity</a> in the <i>Amazon S3 User Guide</i>.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: MultipartUpload, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "upload_id" in value:
        SubElement(el, "UploadId").text = str(value["upload_id"])
    if "key" in value:
        SubElement(el, "Key").text = str(value["key"])
    if "initiated" in value:
        import capo_s3.types.initiated

        capo_s3.types.initiated.serialize_xml(value["initiated"], el, "Initiated")
    if "storage_class" in value:
        import capo_s3.types.storage_class

        capo_s3.types.storage_class.serialize_xml(
            value["storage_class"], el, "StorageClass"
        )
    if "owner" in value:
        import capo_s3.types.owner

        capo_s3.types.owner.serialize_xml(value["owner"], el, "Owner")
    if "initiator" in value:
        import capo_s3.types.initiator

        capo_s3.types.initiator.serialize_xml(value["initiator"], el, "Initiator")
    if "checksum_algorithm" in value:
        import capo_s3.types.checksum_algorithm

        capo_s3.types.checksum_algorithm.serialize_xml(
            value["checksum_algorithm"], el, "ChecksumAlgorithm"
        )
    if "checksum_type" in value:
        import capo_s3.types.checksum_type

        capo_s3.types.checksum_type.serialize_xml(
            value["checksum_type"], el, "ChecksumType"
        )


def deserialize_xml(el: Element) -> MultipartUpload:
    out: MultipartUpload = {}  # type: ignore[typeddict-item]
    child_upload_id = el.find("UploadId")
    if child_upload_id is not None:
        out["upload_id"] = str(child_upload_id.text or "")
    child_key = el.find("Key")
    if child_key is not None:
        out["key"] = str(child_key.text or "")
    child_initiated = el.find("Initiated")
    if child_initiated is not None:
        import capo_s3.types.initiated

        out["initiated"] = capo_s3.types.initiated.deserialize_xml(child_initiated)
    child_storage_class = el.find("StorageClass")
    if child_storage_class is not None:
        import capo_s3.types.storage_class

        out["storage_class"] = capo_s3.types.storage_class.deserialize_xml(
            child_storage_class
        )
    child_owner = el.find("Owner")
    if child_owner is not None:
        import capo_s3.types.owner

        out["owner"] = capo_s3.types.owner.deserialize_xml(child_owner)
    child_initiator = el.find("Initiator")
    if child_initiator is not None:
        import capo_s3.types.initiator

        out["initiator"] = capo_s3.types.initiator.deserialize_xml(child_initiator)
    child_checksum_algorithm = el.find("ChecksumAlgorithm")
    if child_checksum_algorithm is not None:
        import capo_s3.types.checksum_algorithm

        out["checksum_algorithm"] = capo_s3.types.checksum_algorithm.deserialize_xml(
            child_checksum_algorithm
        )
    child_checksum_type = el.find("ChecksumType")
    if child_checksum_type is not None:
        import capo_s3.types.checksum_type

        out["checksum_type"] = capo_s3.types.checksum_type.deserialize_xml(
            child_checksum_type
        )
    return out
