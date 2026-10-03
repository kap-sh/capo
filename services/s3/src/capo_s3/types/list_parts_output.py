"""Generated from Smithy shape ``com.amazonaws.s3#ListPartsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3.types.abort_date
    import capo_s3.types.abort_rule_id
    import capo_s3.types.bucket_name
    import capo_s3.types.checksum_algorithm
    import capo_s3.types.checksum_type
    import capo_s3.types.initiator
    import capo_s3.types.is_truncated
    import capo_s3.types.max_parts
    import capo_s3.types.multipart_upload_id
    import capo_s3.types.next_part_number_marker
    import capo_s3.types.object_key
    import capo_s3.types.owner
    import capo_s3.types.part_number_marker
    import capo_s3.types.parts
    import capo_s3.types.request_charged
    import capo_s3.types.storage_class


class ListPartsOutput(TypedDict, closed=True):
    abort_date: NotRequired["capo_s3.types.abort_date.AbortDate"]
    """<p>If the bucket has a lifecycle rule configured with an action to abort incomplete multipart uploads and the prefix in the lifecycle rule matches the object name in the request, then the response includes this header indicating when the initiated multipart upload will become eligible for abort operation. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/mpuoverview.html#mpu-abort-incomplete-mpu-lifecycle-config">Aborting Incomplete Multipart Uploads Using a Bucket Lifecycle Configuration</a>.</p> <p>The response will also include the <code>x-amz-abort-rule-id</code> header that will provide the ID of the lifecycle configuration rule that defines this action.</p> <note> <p>This functionality is not supported for directory buckets.</p> </note>"""
    abort_rule_id: NotRequired["capo_s3.types.abort_rule_id.AbortRuleId"]
    """<p>This header is returned along with the <code>x-amz-abort-date</code> header. It identifies applicable lifecycle configuration rule that defines the action to abort incomplete multipart uploads.</p> <note> <p>This functionality is not supported for directory buckets.</p> </note>"""
    bucket: NotRequired["capo_s3.types.bucket_name.BucketName"]
    """<p>The name of the bucket to which the multipart upload was initiated. Does not return the access point ARN or access point alias if used.</p>"""
    key: NotRequired["capo_s3.types.object_key.ObjectKey"]
    """<p>Object key for which the multipart upload was initiated.</p>"""
    upload_id: NotRequired["capo_s3.types.multipart_upload_id.MultipartUploadId"]
    """<p>Upload ID identifying the multipart upload whose parts are being listed.</p>"""
    part_number_marker: NotRequired["capo_s3.types.part_number_marker.PartNumberMarker"]
    """<p>Specifies the part after which listing should begin. Only parts with higher part numbers will be listed.</p>"""
    next_part_number_marker: NotRequired[
        "capo_s3.types.next_part_number_marker.NextPartNumberMarker"
    ]
    """<p>When a list is truncated, this element specifies the last part in the list, as well as the value to use for the <code>part-number-marker</code> request parameter in a subsequent request.</p>"""
    max_parts: NotRequired["capo_s3.types.max_parts.MaxParts"]
    """<p>Maximum number of parts that were allowed in the response.</p>"""
    is_truncated: NotRequired["capo_s3.types.is_truncated.IsTruncated"]
    """<p> Indicates whether the returned list of parts is truncated. A true value indicates that the list was truncated. A list can be truncated if the number of parts exceeds the limit returned in the MaxParts element.</p>"""
    parts: NotRequired["capo_s3.types.parts.Parts"]
    """<p>Container for elements related to a particular part. A response can contain zero or more <code>Part</code> elements.</p>"""
    initiator: NotRequired["capo_s3.types.initiator.Initiator"]
    """<p>Container element that identifies who initiated the multipart upload. If the initiator is an Amazon Web Services account, this element provides the same information as the <code>Owner</code> element. If the initiator is an IAM User, this element provides the user ARN.</p>"""
    owner: NotRequired["capo_s3.types.owner.Owner"]
    """<p>Container element that identifies the object owner, after the object is created. If multipart upload is initiated by an IAM user, this element provides the parent account ID.</p> <note> <p> <b>Directory buckets</b> - The bucket owner is returned as the object owner for all the parts.</p> </note>"""
    storage_class: NotRequired["capo_s3.types.storage_class.StorageClass"]
    """<p>The class of storage used to store the uploaded object.</p> <note> <p> <b>Directory buckets</b> - Directory buckets only support <code>EXPRESS_ONEZONE</code> (the S3 Express One Zone storage class) in Availability Zones and <code>ONEZONE_IA</code> (the S3 One Zone-Infrequent Access storage class) in Dedicated Local Zones.</p> </note>"""
    request_charged: NotRequired["capo_s3.types.request_charged.RequestCharged"]
    checksum_algorithm: NotRequired[
        "capo_s3.types.checksum_algorithm.ChecksumAlgorithm"
    ]
    """<p>The algorithm that was used to create a checksum of the object.</p>"""
    checksum_type: NotRequired["capo_s3.types.checksum_type.ChecksumType"]
    """<p>The checksum type, which determines how part-level checksums are combined to create an object-level checksum for multipart objects. You can use this header response to verify that the checksum type that is received is the same checksum type that was specified in <code>CreateMultipartUpload</code> request. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html">Checking object integrity in the Amazon S3 User Guide</a>.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: ListPartsOutput, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "bucket" in value:
        SubElement(el, "Bucket").text = str(value["bucket"])
    if "key" in value:
        SubElement(el, "Key").text = str(value["key"])
    if "upload_id" in value:
        SubElement(el, "UploadId").text = str(value["upload_id"])
    if "part_number_marker" in value:
        SubElement(el, "PartNumberMarker").text = str(value["part_number_marker"])
    if "next_part_number_marker" in value:
        SubElement(el, "NextPartNumberMarker").text = str(
            value["next_part_number_marker"]
        )
    if "max_parts" in value:
        SubElement(el, "MaxParts").text = str(value["max_parts"])
    if "is_truncated" in value:
        SubElement(el, "IsTruncated").text = (
            "true" if value["is_truncated"] else "false"
        )
    if "parts" in value:
        import capo_s3.types.parts

        capo_s3.types.parts.serialize_xml_flat(value["parts"], el, "Part")
    if "initiator" in value:
        import capo_s3.types.initiator

        capo_s3.types.initiator.serialize_xml(value["initiator"], el, "Initiator")
    if "owner" in value:
        import capo_s3.types.owner

        capo_s3.types.owner.serialize_xml(value["owner"], el, "Owner")
    if "storage_class" in value:
        import capo_s3.types.storage_class

        capo_s3.types.storage_class.serialize_xml(
            value["storage_class"], el, "StorageClass"
        )
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


def deserialize_xml(el: Element) -> ListPartsOutput:
    out: ListPartsOutput = {}  # type: ignore[typeddict-item]
    child_bucket = el.find("Bucket")
    if child_bucket is not None:
        out["bucket"] = str(child_bucket.text or "")
    child_key = el.find("Key")
    if child_key is not None:
        out["key"] = str(child_key.text or "")
    child_upload_id = el.find("UploadId")
    if child_upload_id is not None:
        out["upload_id"] = str(child_upload_id.text or "")
    child_part_number_marker = el.find("PartNumberMarker")
    if child_part_number_marker is not None:
        out["part_number_marker"] = str(child_part_number_marker.text or "")
    child_next_part_number_marker = el.find("NextPartNumberMarker")
    if child_next_part_number_marker is not None:
        out["next_part_number_marker"] = str(child_next_part_number_marker.text or "")
    child_max_parts = el.find("MaxParts")
    if child_max_parts is not None:
        out["max_parts"] = int(child_max_parts.text or "")
    child_is_truncated = el.find("IsTruncated")
    if child_is_truncated is not None:
        out["is_truncated"] = (child_is_truncated.text or "").lower() == "true"
    if el.find("Part") is not None:
        import capo_s3.types.parts

        out["parts"] = capo_s3.types.parts.deserialize_xml_flat(el, "Part")
    child_initiator = el.find("Initiator")
    if child_initiator is not None:
        import capo_s3.types.initiator

        out["initiator"] = capo_s3.types.initiator.deserialize_xml(child_initiator)
    child_owner = el.find("Owner")
    if child_owner is not None:
        import capo_s3.types.owner

        out["owner"] = capo_s3.types.owner.deserialize_xml(child_owner)
    child_storage_class = el.find("StorageClass")
    if child_storage_class is not None:
        import capo_s3.types.storage_class

        out["storage_class"] = capo_s3.types.storage_class.deserialize_xml(
            child_storage_class
        )
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
