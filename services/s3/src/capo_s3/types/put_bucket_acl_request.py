"""Generated from Smithy shape ``com.amazonaws.s3#PutBucketAclRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3.types.access_control_policy
    import capo_s3.types.account_id
    import capo_s3.types.bucket_canned_acl
    import capo_s3.types.bucket_name
    import capo_s3.types.checksum_algorithm
    import capo_s3.types.content_md5
    import capo_s3.types.grant_full_control
    import capo_s3.types.grant_read
    import capo_s3.types.grant_read_acp
    import capo_s3.types.grant_write
    import capo_s3.types.grant_write_acp


class PutBucketAclRequest(TypedDict, closed=True):
    acl: NotRequired["capo_s3.types.bucket_canned_acl.BucketCannedACL"]
    """<p>The canned ACL to apply to the bucket.</p>"""
    access_control_policy: NotRequired[
        "capo_s3.types.access_control_policy.AccessControlPolicy"
    ]
    """<p>Contains the elements that set the ACL permissions for an object per grantee.</p>"""
    bucket: "capo_s3.types.bucket_name.BucketName"
    """<p>The bucket to which to apply the ACL.</p>"""
    content_md5: NotRequired["capo_s3.types.content_md5.ContentMD5"]
    """<p>The Base64 encoded 128-bit <code>MD5</code> digest of the data. This header must be used as a message integrity check to verify that the request body was not corrupted in transit. For more information, go to <a href="http://www.ietf.org/rfc/rfc1864.txt">RFC 1864.</a> </p> <p>For requests made using the Amazon Web Services Command Line Interface (CLI) or Amazon Web Services SDKs, this field is calculated automatically.</p>"""
    checksum_algorithm: NotRequired[
        "capo_s3.types.checksum_algorithm.ChecksumAlgorithm"
    ]
    """<p>Indicates the algorithm used to create the checksum for the request when you use the SDK. This header will not provide any additional functionality if you don't use the SDK. When you send this header, there must be a corresponding <code>x-amz-checksum</code> or <code>x-amz-trailer</code> header sent. Otherwise, Amazon S3 fails the request with the HTTP status code <code>400 Bad Request</code>. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html">Checking object integrity</a> in the <i>Amazon S3 User Guide</i>.</p> <p>If you provide an individual checksum, Amazon S3 ignores any provided <code>ChecksumAlgorithm</code> parameter.</p>"""
    grant_full_control: NotRequired["capo_s3.types.grant_full_control.GrantFullControl"]
    """<p>Allows grantee the read, write, read ACP, and write ACP permissions on the bucket.</p>"""
    grant_read: NotRequired["capo_s3.types.grant_read.GrantRead"]
    """<p>Allows grantee to list the objects in the bucket.</p>"""
    grant_read_acp: NotRequired["capo_s3.types.grant_read_acp.GrantReadACP"]
    """<p>Allows grantee to read the bucket ACL.</p>"""
    grant_write: NotRequired["capo_s3.types.grant_write.GrantWrite"]
    """<p>Allows grantee to create new objects in the bucket.</p> <p>For the bucket and object owners of existing objects, also allows deletions and overwrites of those objects.</p>"""
    grant_write_acp: NotRequired["capo_s3.types.grant_write_acp.GrantWriteACP"]
    """<p>Allows grantee to write the ACL for the applicable bucket.</p>"""
    expected_bucket_owner: NotRequired["capo_s3.types.account_id.AccountId"]
    """<p>The account ID of the expected bucket owner. If the account ID that you provide does not match the actual owner of the bucket, the request fails with the HTTP status code <code>403 Forbidden</code> (access denied).</p>"""


# --- restXml ser/de ---
def serialize_xml(value: PutBucketAclRequest, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "access_control_policy" in value:
        import capo_s3.types.access_control_policy

        capo_s3.types.access_control_policy.serialize_xml(
            value["access_control_policy"], el, "AccessControlPolicy"
        )


def deserialize_xml(el: Element) -> PutBucketAclRequest:
    out: PutBucketAclRequest = {}  # type: ignore[typeddict-item]
    child_access_control_policy = el.find("AccessControlPolicy")
    if child_access_control_policy is not None:
        import capo_s3.types.access_control_policy

        out["access_control_policy"] = (
            capo_s3.types.access_control_policy.deserialize_xml(
                child_access_control_policy
            )
        )
    return out
