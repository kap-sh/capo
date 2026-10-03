"""Generated from Smithy shape ``com.amazonaws.s3#PutObjectLegalHoldRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3.types.account_id
    import capo_s3.types.bucket_name
    import capo_s3.types.checksum_algorithm
    import capo_s3.types.content_md5
    import capo_s3.types.object_key
    import capo_s3.types.object_lock_legal_hold
    import capo_s3.types.object_version_id
    import capo_s3.types.request_payer


class PutObjectLegalHoldRequest(TypedDict, closed=True):
    bucket: "capo_s3.types.bucket_name.BucketName"
    """<p>The bucket name containing the object that you want to place a legal hold on. </p> <p> <b>Access points</b> - When you use this action with an access point for general purpose buckets, you must provide the alias of the access point in place of the bucket name or specify the access point ARN. When you use this action with an access point for directory buckets, you must provide the access point name in place of the bucket name. When using the access point ARN, you must direct requests to the access point hostname. The access point hostname takes the form <i>AccessPointName</i>-<i>AccountId</i>.s3-accesspoint.<i>Region</i>.amazonaws.com. When using this action with an access point through the Amazon Web Services SDKs, you provide the access point ARN in place of the bucket name. For more information about access point ARNs, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-access-points.html">Using access points</a> in the <i>Amazon S3 User Guide</i>.</p>"""
    key: "capo_s3.types.object_key.ObjectKey"
    """<p>The key name for the object that you want to place a legal hold on.</p>"""
    legal_hold: NotRequired["capo_s3.types.object_lock_legal_hold.ObjectLockLegalHold"]
    """<p>Container element for the legal hold configuration you want to apply to the specified object.</p>"""
    request_payer: NotRequired["capo_s3.types.request_payer.RequestPayer"]
    version_id: NotRequired["capo_s3.types.object_version_id.ObjectVersionId"]
    """<p>The version ID of the object that you want to place a legal hold on.</p>"""
    content_md5: NotRequired["capo_s3.types.content_md5.ContentMD5"]
    """<p>The MD5 hash for the request body.</p> <p>For requests made using the Amazon Web Services Command Line Interface (CLI) or Amazon Web Services SDKs, this field is calculated automatically.</p>"""
    checksum_algorithm: NotRequired[
        "capo_s3.types.checksum_algorithm.ChecksumAlgorithm"
    ]
    """<p>Indicates the algorithm used to create the checksum for the object when you use the SDK. This header will not provide any additional functionality if you don't use the SDK. When you send this header, there must be a corresponding <code>x-amz-checksum</code> or <code>x-amz-trailer</code> header sent. Otherwise, Amazon S3 fails the request with the HTTP status code <code>400 Bad Request</code>. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html">Checking object integrity</a> in the <i>Amazon S3 User Guide</i>.</p> <p>If you provide an individual checksum, Amazon S3 ignores any provided <code>ChecksumAlgorithm</code> parameter.</p>"""
    expected_bucket_owner: NotRequired["capo_s3.types.account_id.AccountId"]
    """<p>The account ID of the expected bucket owner. If the account ID that you provide does not match the actual owner of the bucket, the request fails with the HTTP status code <code>403 Forbidden</code> (access denied).</p>"""


# --- restXml ser/de ---
def serialize_xml(value: PutObjectLegalHoldRequest, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "legal_hold" in value:
        import capo_s3.types.object_lock_legal_hold

        capo_s3.types.object_lock_legal_hold.serialize_xml(
            value["legal_hold"], el, "LegalHold"
        )


def deserialize_xml(el: Element) -> PutObjectLegalHoldRequest:
    out: PutObjectLegalHoldRequest = {}  # type: ignore[typeddict-item]
    child_legal_hold = el.find("LegalHold")
    if child_legal_hold is not None:
        import capo_s3.types.object_lock_legal_hold

        out["legal_hold"] = capo_s3.types.object_lock_legal_hold.deserialize_xml(
            child_legal_hold
        )
    return out
