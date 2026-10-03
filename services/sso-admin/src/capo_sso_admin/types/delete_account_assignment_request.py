"""Generated from Smithy shape ``com.amazonaws.ssoadmin#DeleteAccountAssignmentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_sso_admin.errors import DeserializationError

if TYPE_CHECKING:
    import capo_sso_admin.types.instance_arn
    import capo_sso_admin.types.permission_set_arn
    import capo_sso_admin.types.principal_id
    import capo_sso_admin.types.principal_type
    import capo_sso_admin.types.target_id
    import capo_sso_admin.types.target_type


class DeleteAccountAssignmentRequest(TypedDict, closed=True):
    instance_arn: "capo_sso_admin.types.instance_arn.InstanceArn"
    """<p>The ARN of the IAM Identity Center instance under which the operation will be executed. For more information about ARNs, see <a href="/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Names (ARNs) and Amazon Web Services Service Namespaces</a> in the <i>Amazon Web Services General Reference</i>.</p>"""
    target_id: "capo_sso_admin.types.target_id.TargetId"
    """<p>TargetID is an Amazon Web Services account identifier, (For example, 123456789012).</p>"""
    target_type: "capo_sso_admin.types.target_type.TargetType"
    """<p>The entity type for which the assignment will be deleted.</p>"""
    permission_set_arn: "capo_sso_admin.types.permission_set_arn.PermissionSetArn"
    """<p>The ARN of the permission set that will be used to remove access.</p>"""
    principal_type: "capo_sso_admin.types.principal_type.PrincipalType"
    """<p>The entity type for which the assignment will be deleted.</p>"""
    principal_id: "capo_sso_admin.types.principal_id.PrincipalId"
    """<p>An identifier for an object in IAM Identity Center, such as a user or group. PrincipalIds are GUIDs (For example, f81d4fae-7dec-11d0-a765-00a0c91e6bf6). For more information about PrincipalIds in IAM Identity Center, see the <a href="/singlesignon/latest/IdentityStoreAPIReference/welcome.html">IAM Identity Center Identity Store API Reference</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteAccountAssignmentRequest) -> dict:
    out: dict = {}
    out["InstanceArn"] = value["instance_arn"]
    out["TargetId"] = value["target_id"]
    import capo_sso_admin.types.target_type

    out["TargetType"] = capo_sso_admin.types.target_type.serialize_aws_json_1_1(
        value["target_type"]
    )
    out["PermissionSetArn"] = value["permission_set_arn"]
    import capo_sso_admin.types.principal_type

    out["PrincipalType"] = capo_sso_admin.types.principal_type.serialize_aws_json_1_1(
        value["principal_type"]
    )
    out["PrincipalId"] = value["principal_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteAccountAssignmentRequest:
    out: DeleteAccountAssignmentRequest = {}  # type: ignore[typeddict-item]
    if data.get("InstanceArn") is not None:
        out["instance_arn"] = data["InstanceArn"]
    else:
        raise DeserializationError(
            "DeleteAccountAssignmentRequest.instance_arn required"
        )
    if data.get("TargetId") is not None:
        out["target_id"] = data["TargetId"]
    else:
        raise DeserializationError("DeleteAccountAssignmentRequest.target_id required")
    if data.get("TargetType") is not None:
        import capo_sso_admin.types.target_type

        out["target_type"] = capo_sso_admin.types.target_type.deserialize_aws_json_1_1(
            data["TargetType"]
        )
    else:
        raise DeserializationError(
            "DeleteAccountAssignmentRequest.target_type required"
        )
    if data.get("PermissionSetArn") is not None:
        out["permission_set_arn"] = data["PermissionSetArn"]
    else:
        raise DeserializationError(
            "DeleteAccountAssignmentRequest.permission_set_arn required"
        )
    if data.get("PrincipalType") is not None:
        import capo_sso_admin.types.principal_type

        out["principal_type"] = (
            capo_sso_admin.types.principal_type.deserialize_aws_json_1_1(
                data["PrincipalType"]
            )
        )
    else:
        raise DeserializationError(
            "DeleteAccountAssignmentRequest.principal_type required"
        )
    if data.get("PrincipalId") is not None:
        out["principal_id"] = data["PrincipalId"]
    else:
        raise DeserializationError(
            "DeleteAccountAssignmentRequest.principal_id required"
        )
    return out
