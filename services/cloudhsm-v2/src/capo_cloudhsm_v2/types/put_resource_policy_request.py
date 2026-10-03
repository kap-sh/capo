"""Generated from Smithy shape ``com.amazonaws.cloudhsmv2#PutResourcePolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudhsm_v2.types.cloud_hsm_arn
    import capo_cloudhsm_v2.types.resource_policy


class PutResourcePolicyRequest(TypedDict, closed=True):
    resource_arn: NotRequired["capo_cloudhsm_v2.types.cloud_hsm_arn.CloudHsmArn"]
    """<p>Amazon Resource Name (ARN) of the resource to which you want to attach a policy. </p>"""
    policy: NotRequired["capo_cloudhsm_v2.types.resource_policy.ResourcePolicy"]
    """<p>The policy you want to associate with a resource. </p> <p>For an example policy, see <a href="https://docs.aws.amazon.com/cloudhsm/latest/userguide/sharing.html"> Working with shared backups</a> in the CloudHSM User Guide</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutResourcePolicyRequest) -> dict:
    out: dict = {}
    if "resource_arn" in value:
        out["ResourceArn"] = value["resource_arn"]
    if "policy" in value:
        out["Policy"] = value["policy"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PutResourcePolicyRequest:
    out: PutResourcePolicyRequest = {}  # type: ignore[typeddict-item]
    if data.get("ResourceArn") is not None:
        out["resource_arn"] = data["ResourceArn"]
    if data.get("Policy") is not None:
        out["policy"] = data["Policy"]
    return out
