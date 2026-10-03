"""Generated from Smithy shape ``com.amazonaws.cloudtrail#PutResourcePolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cloudtrail.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cloudtrail.types.resource_arn
    import capo_cloudtrail.types.resource_policy


class PutResourcePolicyRequest(TypedDict, closed=True):
    resource_arn: "capo_cloudtrail.types.resource_arn.ResourceArn"
    """<p> The Amazon Resource Name (ARN) of the CloudTrail event data store, dashboard, or channel attached to the resource-based policy.</p> <p>Example event data store ARN format: <code>arn:aws:cloudtrail:us-east-2:123456789012:eventdatastore/EXAMPLE-f852-4e8f-8bd1-bcf6cEXAMPLE</code> </p> <p>Example dashboard ARN format: <code>arn:aws:cloudtrail:us-east-1:123456789012:dashboard/exampleDash</code> </p> <p>Example channel ARN format: <code>arn:aws:cloudtrail:us-east-2:123456789012:channel/01234567890</code> </p>"""
    resource_policy: "capo_cloudtrail.types.resource_policy.ResourcePolicy"
    """<p> A JSON-formatted string for an Amazon Web Services resource-based policy. </p> <p> For example resource-based policies, see <a href="https://docs.aws.amazon.com/awscloudtrail/latest/userguide/security_iam_resource-based-policy-examples.html">CloudTrail resource-based policy examples</a> in the <i>CloudTrail User Guide</i>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutResourcePolicyRequest) -> dict:
    out: dict = {}
    out["ResourceArn"] = value["resource_arn"]
    out["ResourcePolicy"] = value["resource_policy"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PutResourcePolicyRequest:
    out: PutResourcePolicyRequest = {}  # type: ignore[typeddict-item]
    if data.get("ResourceArn") is not None:
        out["resource_arn"] = data["ResourceArn"]
    else:
        raise DeserializationError("PutResourcePolicyRequest.resource_arn required")
    if data.get("ResourcePolicy") is not None:
        out["resource_policy"] = data["ResourcePolicy"]
    else:
        raise DeserializationError("PutResourcePolicyRequest.resource_policy required")
    return out
