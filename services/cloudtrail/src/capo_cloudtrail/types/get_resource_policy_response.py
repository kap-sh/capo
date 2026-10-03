"""Generated from Smithy shape ``com.amazonaws.cloudtrail#GetResourcePolicyResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudtrail.types.resource_arn
    import capo_cloudtrail.types.resource_policy


class GetResourcePolicyResponse(TypedDict, closed=True):
    resource_arn: NotRequired["capo_cloudtrail.types.resource_arn.ResourceArn"]
    """<p> The Amazon Resource Name (ARN) of the CloudTrail event data store, dashboard, or channel attached to resource-based policy. </p> <p>Example event data store ARN format: <code>arn:aws:cloudtrail:us-east-2:123456789012:eventdatastore/EXAMPLE-f852-4e8f-8bd1-bcf6cEXAMPLE</code> </p> <p>Example dashboard ARN format: <code>arn:aws:cloudtrail:us-east-1:123456789012:dashboard/exampleDash</code> </p> <p>Example channel ARN format: <code>arn:aws:cloudtrail:us-east-2:123456789012:channel/01234567890</code> </p>"""
    resource_policy: NotRequired["capo_cloudtrail.types.resource_policy.ResourcePolicy"]
    """<p> A JSON-formatted string that contains the resource-based policy attached to the CloudTrail event data store, dashboard, or channel. </p>"""
    delegated_admin_resource_policy: NotRequired[
        "capo_cloudtrail.types.resource_policy.ResourcePolicy"
    ]
    """<p> The default resource-based policy that is automatically generated for the delegated administrator of an Organizations organization. This policy will be evaluated in tandem with any policy you submit for the resource. For more information about this policy, see <a href="https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-lake-organizations.html#cloudtrail-lake-organizations-eds-rbp">Default resource policy for delegated administrators</a>. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetResourcePolicyResponse) -> dict:
    out: dict = {}
    if "resource_arn" in value:
        out["ResourceArn"] = value["resource_arn"]
    if "resource_policy" in value:
        out["ResourcePolicy"] = value["resource_policy"]
    if "delegated_admin_resource_policy" in value:
        out["DelegatedAdminResourcePolicy"] = value["delegated_admin_resource_policy"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetResourcePolicyResponse:
    out: GetResourcePolicyResponse = {}  # type: ignore[typeddict-item]
    if data.get("ResourceArn") is not None:
        out["resource_arn"] = data["ResourceArn"]
    if data.get("ResourcePolicy") is not None:
        out["resource_policy"] = data["ResourcePolicy"]
    if data.get("DelegatedAdminResourcePolicy") is not None:
        out["delegated_admin_resource_policy"] = data["DelegatedAdminResourcePolicy"]
    return out
