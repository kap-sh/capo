"""Generated from Smithy shape ``com.amazonaws.s3#PutBucketLoggingRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3._protocol.xml import Element, SubElement
from capo_s3.errors import DeserializationError

if TYPE_CHECKING:
    import capo_s3.types.account_id
    import capo_s3.types.bucket_logging_status
    import capo_s3.types.bucket_name
    import capo_s3.types.checksum_algorithm
    import capo_s3.types.content_md5


class PutBucketLoggingRequest(TypedDict, closed=True):
    bucket: "capo_s3.types.bucket_name.BucketName"
    """<p>The name of the bucket for which to set the logging parameters.</p>"""
    bucket_logging_status: "capo_s3.types.bucket_logging_status.BucketLoggingStatus"
    """<p>Container for logging status information.</p>"""
    content_md5: NotRequired["capo_s3.types.content_md5.ContentMD5"]
    """<p>The MD5 hash of the <code>PutBucketLogging</code> request body.</p> <p>For requests made using the Amazon Web Services Command Line Interface (CLI) or Amazon Web Services SDKs, this field is calculated automatically.</p>"""
    checksum_algorithm: NotRequired[
        "capo_s3.types.checksum_algorithm.ChecksumAlgorithm"
    ]
    """<p>Indicates the algorithm used to create the checksum for the request when you use the SDK. This header will not provide any additional functionality if you don't use the SDK. When you send this header, there must be a corresponding <code>x-amz-checksum</code> or <code>x-amz-trailer</code> header sent. Otherwise, Amazon S3 fails the request with the HTTP status code <code>400 Bad Request</code>. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html">Checking object integrity</a> in the <i>Amazon S3 User Guide</i>.</p> <p>If you provide an individual checksum, Amazon S3 ignores any provided <code>ChecksumAlgorithm</code> parameter.</p>"""
    expected_bucket_owner: NotRequired["capo_s3.types.account_id.AccountId"]
    """<p>The account ID of the expected bucket owner. If the account ID that you provide does not match the actual owner of the bucket, the request fails with the HTTP status code <code>403 Forbidden</code> (access denied).</p>"""


# --- restXml ser/de ---
def serialize_xml(value: PutBucketLoggingRequest, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    import capo_s3.types.bucket_logging_status

    capo_s3.types.bucket_logging_status.serialize_xml(
        value["bucket_logging_status"], el, "BucketLoggingStatus"
    )


def deserialize_xml(el: Element) -> PutBucketLoggingRequest:
    out: PutBucketLoggingRequest = {}  # type: ignore[typeddict-item]
    child_bucket_logging_status = el.find("BucketLoggingStatus")
    if child_bucket_logging_status is not None:
        import capo_s3.types.bucket_logging_status

        out["bucket_logging_status"] = (
            capo_s3.types.bucket_logging_status.deserialize_xml(
                child_bucket_logging_status
            )
        )
    else:
        raise DeserializationError(
            "PutBucketLoggingRequest.bucket_logging_status required"
        )
    return out
