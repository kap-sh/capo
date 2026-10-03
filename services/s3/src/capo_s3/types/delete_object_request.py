"""Generated from Smithy shape ``com.amazonaws.s3#DeleteObjectRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3.types.account_id
    import capo_s3.types.bucket_name
    import capo_s3.types.bypass_governance_retention
    import capo_s3.types.if_match
    import capo_s3.types.if_match_last_modified_time
    import capo_s3.types.if_match_size
    import capo_s3.types.mfa
    import capo_s3.types.object_key
    import capo_s3.types.object_version_id
    import capo_s3.types.request_payer


class DeleteObjectRequest(TypedDict, closed=True):
    bucket: "capo_s3.types.bucket_name.BucketName"
    """<p>The bucket name of the bucket containing the object. </p> <p> <b>Directory buckets</b> - When you use this operation with a directory bucket, you must use virtual-hosted-style requests in the format <code> <i>Bucket-name</i>.s3express-<i>zone-id</i>.<i>region-code</i>.amazonaws.com</code>. Path-style requests are not supported. Directory bucket names must be unique in the chosen Zone (Availability Zone or Local Zone). Bucket names must follow the format <code> <i>bucket-base-name</i>--<i>zone-id</i>--x-s3</code> (for example, <code> <i>amzn-s3-demo-bucket</i>--<i>usw2-az1</i>--x-s3</code>). For information about bucket naming restrictions, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/directory-bucket-naming-rules.html">Directory bucket naming rules</a> in the <i>Amazon S3 User Guide</i>.</p> <p> <b>Access points</b> - When you use this action with an access point for general purpose buckets, you must provide the alias of the access point in place of the bucket name or specify the access point ARN. When you use this action with an access point for directory buckets, you must provide the access point name in place of the bucket name. When using the access point ARN, you must direct requests to the access point hostname. The access point hostname takes the form <i>AccessPointName</i>-<i>AccountId</i>.s3-accesspoint.<i>Region</i>.amazonaws.com. When using this action with an access point through the Amazon Web Services SDKs, you provide the access point ARN in place of the bucket name. For more information about access point ARNs, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-access-points.html">Using access points</a> in the <i>Amazon S3 User Guide</i>.</p> <note> <p>Object Lambda access points are not supported by directory buckets.</p> </note> <p> <b>S3 on Outposts</b> - When you use this action with S3 on Outposts, you must direct requests to the S3 on Outposts hostname. The S3 on Outposts hostname takes the form <code> <i>AccessPointName</i>-<i>AccountId</i>.<i>outpostID</i>.s3-outposts.<i>Region</i>.amazonaws.com</code>. When you use this action with S3 on Outposts, the destination bucket must be the Outposts access point ARN or the access point alias. For more information about S3 on Outposts, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/S3onOutposts.html">What is S3 on Outposts?</a> in the <i>Amazon S3 User Guide</i>.</p>"""
    key: "capo_s3.types.object_key.ObjectKey"
    """<p>Key name of the object to delete.</p>"""
    mfa: NotRequired["capo_s3.types.mfa.MFA"]
    """<p>The concatenation of the authentication device's serial number, a space, and the value that is displayed on your authentication device. Required to permanently delete a versioned object if versioning is configured with MFA delete enabled.</p> <note> <p>This functionality is not supported for directory buckets.</p> </note>"""
    version_id: NotRequired["capo_s3.types.object_version_id.ObjectVersionId"]
    """<p>Version ID used to reference a specific version of the object.</p> <note> <p>For directory buckets in this API operation, only the <code>null</code> value of the version ID is supported.</p> </note>"""
    request_payer: NotRequired["capo_s3.types.request_payer.RequestPayer"]
    bypass_governance_retention: NotRequired[
        "capo_s3.types.bypass_governance_retention.BypassGovernanceRetention"
    ]
    """<p>Indicates whether S3 Object Lock should bypass Governance-mode restrictions to process this operation. To use this header, you must have the <code>s3:BypassGovernanceRetention</code> permission.</p> <note> <p>This functionality is not supported for directory buckets.</p> </note>"""
    expected_bucket_owner: NotRequired["capo_s3.types.account_id.AccountId"]
    """<p>The account ID of the expected bucket owner. If the account ID that you provide does not match the actual owner of the bucket, the request fails with the HTTP status code <code>403 Forbidden</code> (access denied).</p>"""
    if_match: NotRequired["capo_s3.types.if_match.IfMatch"]
    """<p>Deletes the object if the ETag (entity tag) value provided during the delete operation matches the ETag of the object in S3. If the ETag values do not match, the operation returns a <code>412 Precondition Failed</code> error.</p> <p>Expects the ETag value as a string. <code>If-Match</code> does accept a string value of an '*' (asterisk) character to denote a match of any ETag.</p> <p>For more information about conditional requests, see <a href="https://tools.ietf.org/html/rfc7232">RFC 7232</a>.</p>"""
    if_match_last_modified_time: NotRequired[
        "capo_s3.types.if_match_last_modified_time.IfMatchLastModifiedTime"
    ]
    """<p>If present, the object is deleted only if its modification times matches the provided <code>Timestamp</code>. If the <code>Timestamp</code> values do not match, the operation returns a <code>412 Precondition Failed</code> error. If the <code>Timestamp</code> matches or if the object doesn’t exist, the operation returns a <code>204 Success (No Content)</code> response.</p> <note> <p>This functionality is only supported for directory buckets.</p> </note>"""
    if_match_size: NotRequired["capo_s3.types.if_match_size.IfMatchSize"]
    """<p>If present, the object is deleted only if its size matches the provided size in bytes. If the <code>Size</code> value does not match, the operation returns a <code>412 Precondition Failed</code> error. If the <code>Size</code> matches or if the object doesn’t exist, the operation returns a <code>204 Success (No Content)</code> response.</p> <note> <p>This functionality is only supported for directory buckets.</p> </note> <important> <p>You can use the <code>If-Match</code>, <code>x-amz-if-match-last-modified-time</code> and <code>x-amz-if-match-size</code> conditional headers in conjunction with each-other or individually.</p> </important>"""


# --- restXml ser/de ---
def serialize_xml(value: DeleteObjectRequest, parent: Element, tag: str) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> DeleteObjectRequest:
    out: DeleteObjectRequest = {}  # type: ignore[typeddict-item]
    return out
