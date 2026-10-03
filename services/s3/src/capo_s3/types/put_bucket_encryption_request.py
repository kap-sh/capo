"""Generated from Smithy shape ``com.amazonaws.s3#PutBucketEncryptionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3._protocol.xml import Element, SubElement
from capo_s3.errors import DeserializationError

if TYPE_CHECKING:
    import capo_s3.types.account_id
    import capo_s3.types.bucket_name
    import capo_s3.types.checksum_algorithm
    import capo_s3.types.content_md5
    import capo_s3.types.server_side_encryption_configuration


class PutBucketEncryptionRequest(TypedDict, closed=True):
    bucket: "capo_s3.types.bucket_name.BucketName"
    """<p>Specifies default encryption for a bucket using server-side encryption with different key options.</p> <p> <b>Directory buckets </b> - When you use this operation with a directory bucket, you must use path-style requests in the format <code>https://s3express-control.<i>region-code</i>.amazonaws.com/<i>bucket-name</i> </code>. Virtual-hosted-style requests aren't supported. Directory bucket names must be unique in the chosen Zone (Availability Zone or Local Zone). Bucket names must also follow the format <code> <i>bucket-base-name</i>--<i>zone-id</i>--x-s3</code> (for example, <code> <i>DOC-EXAMPLE-BUCKET</i>--<i>usw2-az1</i>--x-s3</code>). For information about bucket naming restrictions, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/directory-bucket-naming-rules.html">Directory bucket naming rules</a> in the <i>Amazon S3 User Guide</i> </p>"""
    content_md5: NotRequired["capo_s3.types.content_md5.ContentMD5"]
    """<p>The Base64 encoded 128-bit <code>MD5</code> digest of the server-side encryption configuration.</p> <p>For requests made using the Amazon Web Services Command Line Interface (CLI) or Amazon Web Services SDKs, this field is calculated automatically.</p> <note> <p>This functionality is not supported for directory buckets.</p> </note>"""
    checksum_algorithm: NotRequired[
        "capo_s3.types.checksum_algorithm.ChecksumAlgorithm"
    ]
    """<p>Indicates the algorithm used to create the checksum for the request when you use the SDK. This header will not provide any additional functionality if you don't use the SDK. When you send this header, there must be a corresponding <code>x-amz-checksum</code> or <code>x-amz-trailer</code> header sent. Otherwise, Amazon S3 fails the request with the HTTP status code <code>400 Bad Request</code>. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html">Checking object integrity</a> in the <i>Amazon S3 User Guide</i>.</p> <p>If you provide an individual checksum, Amazon S3 ignores any provided <code>ChecksumAlgorithm</code> parameter.</p> <note> <p>For directory buckets, when you use Amazon Web Services SDKs, <code>CRC32</code> is the default checksum algorithm that's used for performance.</p> </note>"""
    server_side_encryption_configuration: "capo_s3.types.server_side_encryption_configuration.ServerSideEncryptionConfiguration"
    expected_bucket_owner: NotRequired["capo_s3.types.account_id.AccountId"]
    """<p>The account ID of the expected bucket owner. If the account ID that you provide does not match the actual owner of the bucket, the request fails with the HTTP status code <code>403 Forbidden</code> (access denied).</p> <note> <p>For directory buckets, this header is not supported in this API operation. If you specify this header, the request fails with the HTTP status code <code>501 Not Implemented</code>.</p> </note>"""


# --- restXml ser/de ---
def serialize_xml(value: PutBucketEncryptionRequest, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    import capo_s3.types.server_side_encryption_configuration

    capo_s3.types.server_side_encryption_configuration.serialize_xml(
        value["server_side_encryption_configuration"],
        el,
        "ServerSideEncryptionConfiguration",
    )


def deserialize_xml(el: Element) -> PutBucketEncryptionRequest:
    out: PutBucketEncryptionRequest = {}  # type: ignore[typeddict-item]
    child_server_side_encryption_configuration = el.find(
        "ServerSideEncryptionConfiguration"
    )
    if child_server_side_encryption_configuration is not None:
        import capo_s3.types.server_side_encryption_configuration

        out["server_side_encryption_configuration"] = (
            capo_s3.types.server_side_encryption_configuration.deserialize_xml(
                child_server_side_encryption_configuration
            )
        )
    else:
        raise DeserializationError(
            "PutBucketEncryptionRequest.server_side_encryption_configuration required"
        )
    return out
