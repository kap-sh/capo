"""Generated from Smithy shape ``com.amazonaws.s3#PutObjectLockConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3.types.account_id
    import capo_s3.types.bucket_name
    import capo_s3.types.checksum_algorithm
    import capo_s3.types.content_md5
    import capo_s3.types.object_lock_configuration
    import capo_s3.types.object_lock_token
    import capo_s3.types.request_payer


class PutObjectLockConfigurationRequest(TypedDict, closed=True):
    bucket: "capo_s3.types.bucket_name.BucketName"
    """<p>The bucket whose Object Lock configuration you want to create or replace.</p>"""
    object_lock_configuration: NotRequired[
        "capo_s3.types.object_lock_configuration.ObjectLockConfiguration"
    ]
    """<p>The Object Lock configuration that you want to apply to the specified bucket.</p>"""
    request_payer: NotRequired["capo_s3.types.request_payer.RequestPayer"]
    token: NotRequired["capo_s3.types.object_lock_token.ObjectLockToken"]
    """<p>A token to allow Object Lock to be enabled for an existing bucket.</p>"""
    content_md5: NotRequired["capo_s3.types.content_md5.ContentMD5"]
    """<p>The MD5 hash for the request body.</p> <p>For requests made using the Amazon Web Services Command Line Interface (CLI) or Amazon Web Services SDKs, this field is calculated automatically.</p>"""
    checksum_algorithm: NotRequired[
        "capo_s3.types.checksum_algorithm.ChecksumAlgorithm"
    ]
    """<p>Indicates the algorithm used to create the checksum for the object when you use the SDK. This header will not provide any additional functionality if you don't use the SDK. When you send this header, there must be a corresponding <code>x-amz-checksum</code> or <code>x-amz-trailer</code> header sent. Otherwise, Amazon S3 fails the request with the HTTP status code <code>400 Bad Request</code>. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html">Checking object integrity</a> in the <i>Amazon S3 User Guide</i>.</p> <p>If you provide an individual checksum, Amazon S3 ignores any provided <code>ChecksumAlgorithm</code> parameter.</p>"""
    expected_bucket_owner: NotRequired["capo_s3.types.account_id.AccountId"]
    """<p>The account ID of the expected bucket owner. If the account ID that you provide does not match the actual owner of the bucket, the request fails with the HTTP status code <code>403 Forbidden</code> (access denied).</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: PutObjectLockConfigurationRequest, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    if "object_lock_configuration" in value:
        import capo_s3.types.object_lock_configuration

        capo_s3.types.object_lock_configuration.serialize_xml(
            value["object_lock_configuration"], el, "ObjectLockConfiguration"
        )


def deserialize_xml(el: Element) -> PutObjectLockConfigurationRequest:
    out: PutObjectLockConfigurationRequest = {}  # type: ignore[typeddict-item]
    child_object_lock_configuration = el.find("ObjectLockConfiguration")
    if child_object_lock_configuration is not None:
        import capo_s3.types.object_lock_configuration

        out["object_lock_configuration"] = (
            capo_s3.types.object_lock_configuration.deserialize_xml(
                child_object_lock_configuration
            )
        )
    return out
