"""Generated from Smithy shape ``com.amazonaws.s3control#PutAccessPointPolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_s3_control._protocol.xml import Element, SubElement
from capo_s3_control.errors import DeserializationError

if TYPE_CHECKING:
    import capo_s3_control.types.access_point_name
    import capo_s3_control.types.account_id
    import capo_s3_control.types.policy


class PutAccessPointPolicyRequest(TypedDict, closed=True):
    account_id: "capo_s3_control.types.account_id.AccountId"
    """<p>The Amazon Web Services account ID for owner of the bucket associated with the specified access point.</p>"""
    name: "capo_s3_control.types.access_point_name.AccessPointName"
    """<p>The name of the access point that you want to associate with the specified policy.</p> <p>For using this parameter with Amazon S3 on Outposts with the REST API, you must specify the name and the x-amz-outpost-id as well.</p> <p>For using this parameter with S3 on Outposts with the Amazon Web Services SDK and CLI, you must specify the ARN of the access point accessed in the format <code>arn:aws:s3-outposts:<Region>:<account-id>:outpost/<outpost-id>/accesspoint/<my-accesspoint-name></code>. For example, to access the access point <code>reports-ap</code> through Outpost <code>my-outpost</code> owned by account <code>123456789012</code> in Region <code>us-west-2</code>, use the URL encoding of <code>arn:aws:s3-outposts:us-west-2:123456789012:outpost/my-outpost/accesspoint/reports-ap</code>. The value must be URL encoded. </p>"""
    policy: "capo_s3_control.types.policy.Policy"
    """<p>The policy that you want to apply to the specified access point. For more information about access point policies, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-points.html">Managing data access with Amazon S3 access points</a> or <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-points-directory-buckets.html">Managing access to shared datasets in directory buckets with access points</a> in the <i>Amazon S3 User Guide</i>.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: PutAccessPointPolicyRequest, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "Policy").text = str(value["policy"])


def deserialize_xml(el: Element) -> PutAccessPointPolicyRequest:
    out: PutAccessPointPolicyRequest = {}  # type: ignore[typeddict-item]
    child_policy = el.find("Policy")
    if child_policy is not None:
        out["policy"] = str(child_policy.text or "")
    else:
        raise DeserializationError("PutAccessPointPolicyRequest.policy required")
    return out
