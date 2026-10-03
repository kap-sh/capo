"""Generated from Smithy shape ``com.amazonaws.ssm#UpdateManagedInstanceRoleRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_ssm.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ssm.types.iam_role
    import capo_ssm.types.managed_instance_id


class UpdateManagedInstanceRoleRequest(TypedDict, closed=True):
    instance_id: "capo_ssm.types.managed_instance_id.ManagedInstanceId"
    """<p>The ID of the managed node where you want to update the role.</p>"""
    iam_role: "capo_ssm.types.iam_role.IamRole"
    """<p>The name of the Identity and Access Management (IAM) role that you want to assign to the managed node. This IAM role must provide AssumeRole permissions for the Amazon Web Services Systems Manager service principal <code>ssm.amazonaws.com</code>. For more information, see <a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/hybrid-multicloud-service-role.html">Create the IAM service role required for Systems Manager in hybrid and multicloud environments</a> in the <i>Amazon Web Services Systems Manager User Guide</i>.</p> <note> <p>You can't specify an IAM service-linked role for this parameter. You must create a unique role.</p> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateManagedInstanceRoleRequest) -> dict:
    out: dict = {}
    out["InstanceId"] = value["instance_id"]
    out["IamRole"] = value["iam_role"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateManagedInstanceRoleRequest:
    out: UpdateManagedInstanceRoleRequest = {}  # type: ignore[typeddict-item]
    if data.get("InstanceId") is not None:
        out["instance_id"] = data["InstanceId"]
    else:
        raise DeserializationError(
            "UpdateManagedInstanceRoleRequest.instance_id required"
        )
    if data.get("IamRole") is not None:
        out["iam_role"] = data["IamRole"]
    else:
        raise DeserializationError("UpdateManagedInstanceRoleRequest.iam_role required")
    return out
