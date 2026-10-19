"""Generated from Smithy shape ``com.amazonaws.ssoadmin#PutPermissionsBoundaryToPermissionSetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_sso_admin.errors import DeserializationError

if TYPE_CHECKING:
    import capo_sso_admin.types.instance_arn
    import capo_sso_admin.types.permission_set_arn
    import capo_sso_admin.types.permissions_boundary


class PutPermissionsBoundaryToPermissionSetRequest(TypedDict, closed=True):
    instance_arn: "capo_sso_admin.types.instance_arn.InstanceArn"
    """<p>The ARN of the IAM Identity Center instance under which the operation will be executed. </p>"""
    permission_set_arn: "capo_sso_admin.types.permission_set_arn.PermissionSetArn"
    """<p>The ARN of the <code>PermissionSet</code>.</p>"""
    permissions_boundary: (
        "capo_sso_admin.types.permissions_boundary.PermissionsBoundary"
    )
    """<p>The permissions boundary that you want to attach to a <code>PermissionSet</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutPermissionsBoundaryToPermissionSetRequest) -> dict:
    out: dict = {}
    out["InstanceArn"] = value["instance_arn"]
    out["PermissionSetArn"] = value["permission_set_arn"]
    import capo_sso_admin.types.permissions_boundary

    out["PermissionsBoundary"] = (
        capo_sso_admin.types.permissions_boundary.serialize_aws_json_1_1(
            value["permissions_boundary"]
        )
    )
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> PutPermissionsBoundaryToPermissionSetRequest:
    out: PutPermissionsBoundaryToPermissionSetRequest = {}  # type: ignore[typeddict-item]
    if data.get("InstanceArn") is not None:
        out["instance_arn"] = data["InstanceArn"]
    else:
        out["instance_arn"] = ""
    if data.get("PermissionSetArn") is not None:
        out["permission_set_arn"] = data["PermissionSetArn"]
    else:
        out["permission_set_arn"] = ""
    if data.get("PermissionsBoundary") is not None:
        import capo_sso_admin.types.permissions_boundary

        out["permissions_boundary"] = (
            capo_sso_admin.types.permissions_boundary.deserialize_aws_json_1_1(
                data["PermissionsBoundary"]
            )
        )
    else:
        raise DeserializationError(
            "PutPermissionsBoundaryToPermissionSetRequest.permissions_boundary required"
        )
    return out
