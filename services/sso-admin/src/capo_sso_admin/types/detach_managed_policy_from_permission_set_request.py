"""Generated from Smithy shape ``com.amazonaws.ssoadmin#DetachManagedPolicyFromPermissionSetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_sso_admin.errors import DeserializationError

if TYPE_CHECKING:
    import capo_sso_admin.types.instance_arn
    import capo_sso_admin.types.managed_policy_arn
    import capo_sso_admin.types.permission_set_arn


class DetachManagedPolicyFromPermissionSetRequest(TypedDict, closed=True):
    instance_arn: "capo_sso_admin.types.instance_arn.InstanceArn"
    """<p>The ARN of the IAM Identity Center instance under which the operation will be executed. For more information about ARNs, see <a href="/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Names (ARNs) and Amazon Web Services Service Namespaces</a> in the <i>Amazon Web Services General Reference</i>.</p>"""
    permission_set_arn: "capo_sso_admin.types.permission_set_arn.PermissionSetArn"
    """<p>The ARN of the <a>PermissionSet</a> from which the policy should be detached.</p>"""
    managed_policy_arn: "capo_sso_admin.types.managed_policy_arn.ManagedPolicyArn"
    """<p>The Amazon Web Services managed policy ARN to be detached from a permission set.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DetachManagedPolicyFromPermissionSetRequest) -> dict:
    out: dict = {}
    out["InstanceArn"] = value["instance_arn"]
    out["PermissionSetArn"] = value["permission_set_arn"]
    out["ManagedPolicyArn"] = value["managed_policy_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DetachManagedPolicyFromPermissionSetRequest:
    out: DetachManagedPolicyFromPermissionSetRequest = {}  # type: ignore[typeddict-item]
    if data.get("InstanceArn") is not None:
        out["instance_arn"] = data["InstanceArn"]
    else:
        raise DeserializationError(
            "DetachManagedPolicyFromPermissionSetRequest.instance_arn required"
        )
    if data.get("PermissionSetArn") is not None:
        out["permission_set_arn"] = data["PermissionSetArn"]
    else:
        raise DeserializationError(
            "DetachManagedPolicyFromPermissionSetRequest.permission_set_arn required"
        )
    if data.get("ManagedPolicyArn") is not None:
        out["managed_policy_arn"] = data["ManagedPolicyArn"]
    else:
        raise DeserializationError(
            "DetachManagedPolicyFromPermissionSetRequest.managed_policy_arn required"
        )
    return out
