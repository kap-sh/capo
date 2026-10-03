"""Generated from Smithy shape ``com.amazonaws.s3#PutBucketVersioningRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3._protocol.xml import Element, SubElement
from capo_s3.errors import DeserializationError

if TYPE_CHECKING:
    import capo_s3.types.account_id
    import capo_s3.types.bucket_name
    import capo_s3.types.checksum_algorithm
    import capo_s3.types.content_md5
    import capo_s3.types.mfa
    import capo_s3.types.versioning_configuration


class PutBucketVersioningRequest(TypedDict, closed=True):
    bucket: "capo_s3.types.bucket_name.BucketName"
    """<p>The bucket name.</p>"""
    content_md5: NotRequired["capo_s3.types.content_md5.ContentMD5"]
    """<p>>The Base64 encoded 128-bit <code>MD5</code> digest of the data. You must use this header as a message integrity check to verify that the request body was not corrupted in transit. For more information, see <a href="http://www.ietf.org/rfc/rfc1864.txt">RFC 1864</a>.</p> <p>For requests made using the Amazon Web Services Command Line Interface (CLI) or Amazon Web Services SDKs, this field is calculated automatically.</p>"""
    checksum_algorithm: NotRequired[
        "capo_s3.types.checksum_algorithm.ChecksumAlgorithm"
    ]
    """<p>Indicates the algorithm used to create the checksum for the request when you use the SDK. This header will not provide any additional functionality if you don't use the SDK. When you send this header, there must be a corresponding <code>x-amz-checksum</code> or <code>x-amz-trailer</code> header sent. Otherwise, Amazon S3 fails the request with the HTTP status code <code>400 Bad Request</code>. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html">Checking object integrity</a> in the <i>Amazon S3 User Guide</i>.</p> <p>If you provide an individual checksum, Amazon S3 ignores any provided <code>ChecksumAlgorithm</code> parameter.</p>"""
    mfa: NotRequired["capo_s3.types.mfa.MFA"]
    """<p>The concatenation of the authentication device's serial number, a space, and the value that is displayed on your authentication device. The serial number is the number that uniquely identifies the MFA device. For physical MFA devices, this is the unique serial number that's provided with the device. For virtual MFA devices, the serial number is the device ARN. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/manage-versioning-examples.html">Enabling versioning on buckets</a> and <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/MultiFactorAuthenticationDelete.html">Configuring MFA delete</a> in the <i>Amazon Simple Storage Service User Guide</i>.</p>"""
    versioning_configuration: (
        "capo_s3.types.versioning_configuration.VersioningConfiguration"
    )
    """<p>Container for setting the versioning state.</p>"""
    expected_bucket_owner: NotRequired["capo_s3.types.account_id.AccountId"]
    """<p>The account ID of the expected bucket owner. If the account ID that you provide does not match the actual owner of the bucket, the request fails with the HTTP status code <code>403 Forbidden</code> (access denied).</p>"""


# --- restXml ser/de ---
def serialize_xml(value: PutBucketVersioningRequest, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    import capo_s3.types.versioning_configuration

    capo_s3.types.versioning_configuration.serialize_xml(
        value["versioning_configuration"], el, "VersioningConfiguration"
    )


def deserialize_xml(el: Element) -> PutBucketVersioningRequest:
    out: PutBucketVersioningRequest = {}  # type: ignore[typeddict-item]
    child_versioning_configuration = el.find("VersioningConfiguration")
    if child_versioning_configuration is not None:
        import capo_s3.types.versioning_configuration

        out["versioning_configuration"] = (
            capo_s3.types.versioning_configuration.deserialize_xml(
                child_versioning_configuration
            )
        )
    else:
        raise DeserializationError(
            "PutBucketVersioningRequest.versioning_configuration required"
        )
    return out
