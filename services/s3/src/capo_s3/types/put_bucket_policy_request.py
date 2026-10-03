"""Generated from Smithy shape ``com.amazonaws.s3#PutBucketPolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3._protocol.xml import Element, SubElement
from capo_s3.errors import DeserializationError

if TYPE_CHECKING:
    import capo_s3.types.account_id
    import capo_s3.types.bucket_name
    import capo_s3.types.checksum_algorithm
    import capo_s3.types.confirm_remove_self_bucket_access
    import capo_s3.types.content_md5
    import capo_s3.types.policy


class PutBucketPolicyRequest(TypedDict, closed=True):
    bucket: "capo_s3.types.bucket_name.BucketName"
    """<p>The name of the bucket.</p> <p> <b>Directory buckets </b> - When you use this operation with a directory bucket, you must use path-style requests in the format <code>https://s3express-control.<i>region-code</i>.amazonaws.com/<i>bucket-name</i> </code>. Virtual-hosted-style requests aren't supported. Directory bucket names must be unique in the chosen Zone (Availability Zone or Local Zone). Bucket names must also follow the format <code> <i>bucket-base-name</i>--<i>zone-id</i>--x-s3</code> (for example, <code> <i>DOC-EXAMPLE-BUCKET</i>--<i>usw2-az1</i>--x-s3</code>). For information about bucket naming restrictions, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/directory-bucket-naming-rules.html">Directory bucket naming rules</a> in the <i>Amazon S3 User Guide</i> </p>"""
    content_md5: NotRequired["capo_s3.types.content_md5.ContentMD5"]
    """<p>The MD5 hash of the request body.</p> <p>For requests made using the Amazon Web Services Command Line Interface (CLI) or Amazon Web Services SDKs, this field is calculated automatically.</p> <note> <p>This functionality is not supported for directory buckets.</p> </note>"""
    checksum_algorithm: NotRequired[
        "capo_s3.types.checksum_algorithm.ChecksumAlgorithm"
    ]
    """<p>Indicates the algorithm used to create the checksum for the request when you use the SDK. This header will not provide any additional functionality if you don't use the SDK. When you send this header, there must be a corresponding <code>x-amz-checksum-<i>algorithm</i> </code> or <code>x-amz-trailer</code> header sent. Otherwise, Amazon S3 fails the request with the HTTP status code <code>400 Bad Request</code>.</p> <p>For the <code>x-amz-checksum-<i>algorithm</i> </code> header, replace <code> <i>algorithm</i> </code> with the supported algorithm from the following list: </p> <ul> <li> <p> <code>CRC32</code> </p> </li> <li> <p> <code>CRC32C</code> </p> </li> <li> <p> <code>CRC64NVME</code> </p> </li> <li> <p> <code>MD5</code> </p> </li> <li> <p> <code>SHA1</code> </p> </li> <li> <p> <code>SHA256</code> </p> </li> <li> <p> <code>SHA512</code> </p> </li> <li> <p> <code>XXHASH3</code> </p> </li> <li> <p> <code>XXHASH64</code> </p> </li> <li> <p> <code>XXHASH128</code> </p> </li> </ul> <p>For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html">Checking object integrity</a> in the <i>Amazon S3 User Guide</i>.</p> <p>If the individual checksum value you provide through <code>x-amz-checksum-<i>algorithm</i> </code> doesn't match the checksum algorithm you set through <code>x-amz-sdk-checksum-algorithm</code>, Amazon S3 fails the request with a <code>BadDigest</code> error.</p> <note> <p>For directory buckets, when you use Amazon Web Services SDKs, <code>CRC32</code> is the default checksum algorithm that's used for performance.</p> </note>"""
    confirm_remove_self_bucket_access: NotRequired[
        "capo_s3.types.confirm_remove_self_bucket_access.ConfirmRemoveSelfBucketAccess"
    ]
    """<p>Set this parameter to true to confirm that you want to remove your permissions to change this bucket policy in the future.</p> <note> <p>This functionality is not supported for directory buckets.</p> </note>"""
    policy: "capo_s3.types.policy.Policy"
    """<p>The bucket policy as a JSON document.</p> <p>For directory buckets, the only IAM action supported in the bucket policy is <code>s3express:CreateSession</code>.</p>"""
    expected_bucket_owner: NotRequired["capo_s3.types.account_id.AccountId"]
    """<p>The account ID of the expected bucket owner. If the account ID that you provide does not match the actual owner of the bucket, the request fails with the HTTP status code <code>403 Forbidden</code> (access denied).</p> <note> <p>For directory buckets, this header is not supported in this API operation. If you specify this header, the request fails with the HTTP status code <code>501 Not Implemented</code>.</p> </note>"""


# --- restXml ser/de ---
def serialize_xml(value: PutBucketPolicyRequest, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "Policy").text = str(value["policy"])


def deserialize_xml(el: Element) -> PutBucketPolicyRequest:
    out: PutBucketPolicyRequest = {}  # type: ignore[typeddict-item]
    child_policy = el.find("Policy")
    if child_policy is not None:
        out["policy"] = str(child_policy.text or "")
    else:
        raise DeserializationError("PutBucketPolicyRequest.policy required")
    return out
