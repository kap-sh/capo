"""Generated from Smithy shape ``com.amazonaws.ssoadmin#ProvisionPermissionSetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_sso_admin.errors import DeserializationError

if TYPE_CHECKING:
    import capo_sso_admin.types.instance_arn
    import capo_sso_admin.types.permission_set_arn
    import capo_sso_admin.types.provision_target_type
    import capo_sso_admin.types.target_id


class ProvisionPermissionSetRequest(TypedDict, closed=True):
    instance_arn: "capo_sso_admin.types.instance_arn.InstanceArn"
    """<p>The ARN of the IAM Identity Center instance under which the operation will be executed. For more information about ARNs, see <a href="/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Names (ARNs) and Amazon Web Services Service Namespaces</a> in the <i>Amazon Web Services General Reference</i>.</p>"""
    permission_set_arn: "capo_sso_admin.types.permission_set_arn.PermissionSetArn"
    """<p>The ARN of the permission set.</p>"""
    target_id: NotRequired["capo_sso_admin.types.target_id.TargetId"]
    """<p>TargetID is an Amazon Web Services account identifier, (For example, 123456789012).</p>"""
    target_type: "capo_sso_admin.types.provision_target_type.ProvisionTargetType"
    """<p>The entity type for which the assignment will be created.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProvisionPermissionSetRequest) -> dict:
    out: dict = {}
    out["InstanceArn"] = value["instance_arn"]
    out["PermissionSetArn"] = value["permission_set_arn"]
    if "target_id" in value:
        out["TargetId"] = value["target_id"]
    import capo_sso_admin.types.provision_target_type

    out["TargetType"] = (
        capo_sso_admin.types.provision_target_type.serialize_aws_json_1_1(
            value["target_type"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> ProvisionPermissionSetRequest:
    out: ProvisionPermissionSetRequest = {}  # type: ignore[typeddict-item]
    if data.get("InstanceArn") is not None:
        out["instance_arn"] = data["InstanceArn"]
    else:
        raise DeserializationError(
            "ProvisionPermissionSetRequest.instance_arn required"
        )
    if data.get("PermissionSetArn") is not None:
        out["permission_set_arn"] = data["PermissionSetArn"]
    else:
        raise DeserializationError(
            "ProvisionPermissionSetRequest.permission_set_arn required"
        )
    if data.get("TargetId") is not None:
        out["target_id"] = data["TargetId"]
    if data.get("TargetType") is not None:
        import capo_sso_admin.types.provision_target_type

        out["target_type"] = (
            capo_sso_admin.types.provision_target_type.deserialize_aws_json_1_1(
                data["TargetType"]
            )
        )
    else:
        raise DeserializationError("ProvisionPermissionSetRequest.target_type required")
    return out
