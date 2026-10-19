"""Generated from Smithy shape ``com.amazonaws.s3control#PutBucketPolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3_control._protocol.xml import Element, SubElement
from capo_s3_control.errors import DeserializationError

if TYPE_CHECKING:
    import capo_s3_control.types.account_id
    import capo_s3_control.types.bucket_name
    import capo_s3_control.types.confirm_remove_self_bucket_access
    import capo_s3_control.types.policy


class PutBucketPolicyRequest(TypedDict, closed=True):
    account_id: "capo_s3_control.types.account_id.AccountId"
    """<p>The Amazon Web Services account ID of the Outposts bucket.</p>"""
    bucket: "capo_s3_control.types.bucket_name.BucketName"
    """<p>Specifies the bucket.</p> <p>For using this parameter with Amazon S3 on Outposts with the REST API, you must specify the name and the x-amz-outpost-id as well.</p> <p>For using this parameter with S3 on Outposts with the Amazon Web Services SDK and CLI, you must specify the ARN of the bucket accessed in the format <code>arn:aws:s3-outposts:<Region>:<account-id>:outpost/<outpost-id>/bucket/<my-bucket-name></code>. For example, to access the bucket <code>reports</code> through Outpost <code>my-outpost</code> owned by account <code>123456789012</code> in Region <code>us-west-2</code>, use the URL encoding of <code>arn:aws:s3-outposts:us-west-2:123456789012:outpost/my-outpost/bucket/reports</code>. The value must be URL encoded. </p>"""
    confirm_remove_self_bucket_access: NotRequired[
        "capo_s3_control.types.confirm_remove_self_bucket_access.ConfirmRemoveSelfBucketAccess"
    ]
    """<p>Set this parameter to true to confirm that you want to remove your permissions to change this bucket policy in the future.</p> <note> <p>This is not supported by Amazon S3 on Outposts buckets.</p> </note>"""
    policy: "capo_s3_control.types.policy.Policy"
    """<p>The bucket policy as a JSON document.</p>"""


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
