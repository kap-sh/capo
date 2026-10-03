"""Generated from Smithy shape ``com.amazonaws.s3#UpdateObjectEncryptionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3._protocol.xml import Element, SubElement
from capo_s3.errors import DeserializationError

if TYPE_CHECKING:
    import capo_s3.types.account_id
    import capo_s3.types.bucket_name
    import capo_s3.types.checksum_algorithm
    import capo_s3.types.content_md5
    import capo_s3.types.object_encryption
    import capo_s3.types.object_key
    import capo_s3.types.object_version_id
    import capo_s3.types.request_payer


class UpdateObjectEncryptionRequest(TypedDict, closed=True):
    bucket: "capo_s3.types.bucket_name.BucketName"
    """<p> The name of the general purpose bucket that contains the specified object key name. </p> <p>When you use this operation with an access point attached to a general purpose bucket, you must either provide the alias of the access point in place of the bucket name or you must specify the access point Amazon Resource Name (ARN). When using the access point ARN, you must direct requests to the access point hostname. The access point hostname takes the form <code> <i>AccessPointName</i>-<i>AccountId</i>.s3-accesspoint.<i>Region</i>.amazonaws.com</code>. When using this operation with an access point through the Amazon Web Services SDKs, you provide the access point ARN in place of the bucket name. For more information about access point ARNs, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-points-naming.html"> Referencing access points</a> in the <i>Amazon S3 User Guide</i>.</p>"""
    key: "capo_s3.types.object_key.ObjectKey"
    """<p> The key name of the object that you want to update the server-side encryption type for. </p>"""
    version_id: NotRequired["capo_s3.types.object_version_id.ObjectVersionId"]
    """<p> The version ID of the object that you want to update the server-side encryption type for. </p>"""
    object_encryption: "capo_s3.types.object_encryption.ObjectEncryption"
    """<p> The updated server-side encryption type for this object. The <code>UpdateObjectEncryption</code> operation supports the SSE-S3 and SSE-KMS encryption types. </p> <p>Valid Values: <code>SSES3</code> | <code>SSEKMS</code> </p>"""
    request_payer: NotRequired["capo_s3.types.request_payer.RequestPayer"]
    expected_bucket_owner: NotRequired["capo_s3.types.account_id.AccountId"]
    """<p> The account ID of the expected bucket owner. If the account ID that you provide doesn't match the actual owner of the bucket, the request fails with the HTTP status code <code>403 Forbidden</code> (access denied). </p>"""
    content_md5: NotRequired["capo_s3.types.content_md5.ContentMD5"]
    """<p> The MD5 hash for the request body. For requests made using the Amazon Web Services Command Line Interface (CLI) or Amazon Web Services SDKs, this field is calculated automatically. </p>"""
    checksum_algorithm: NotRequired[
        "capo_s3.types.checksum_algorithm.ChecksumAlgorithm"
    ]
    """<p> Indicates the algorithm used to create the checksum for the object when you use an Amazon Web Services SDK. This header doesn't provide any additional functionality if you don't use the SDK. When you send this header, there must be a corresponding <code>x-amz-checksum</code> or <code>x-amz-trailer</code> header sent. Otherwise, Amazon S3 fails the request with the HTTP status code <code>400 Bad Request</code>. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html"> Checking object integrity </a> in the <i>Amazon S3 User Guide</i>. </p> <p>If you provide an individual checksum, Amazon S3 ignores any provided <code>ChecksumAlgorithm</code> parameter.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: UpdateObjectEncryptionRequest, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    import capo_s3.types.object_encryption

    capo_s3.types.object_encryption.serialize_xml(
        value["object_encryption"], el, "ObjectEncryption"
    )


def deserialize_xml(el: Element) -> UpdateObjectEncryptionRequest:
    out: UpdateObjectEncryptionRequest = {}  # type: ignore[typeddict-item]
    child_object_encryption = el.find("ObjectEncryption")
    if child_object_encryption is not None:
        import capo_s3.types.object_encryption

        out["object_encryption"] = capo_s3.types.object_encryption.deserialize_xml(
            child_object_encryption
        )
    else:
        raise DeserializationError(
            "UpdateObjectEncryptionRequest.object_encryption required"
        )
    return out
