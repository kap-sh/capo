"""Generated from Smithy shape ``com.amazonaws.resiliencehub#PermissionModel``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_resiliencehub.types.iam_role_arn_list
    import capo_resiliencehub.types.iam_role_name
    import capo_resiliencehub.types.permission_model_type


class PermissionModel(TypedDict, closed=True):
    type: "capo_resiliencehub.types.permission_model_type.PermissionModelType"
    """<p>Defines how Resilience Hub scans your resources. It can scan for the resources by using a pre-existing role in your Amazon Web Services account, or by using the credentials of the current IAM user.</p>"""
    invoker_role_name: NotRequired["capo_resiliencehub.types.iam_role_name.IamRoleName"]
    """<p>Existing Amazon Web Services IAM role name in the primary Amazon Web Services account that will be assumed by Resilience Hub Service Principle to obtain a read-only access to your application resources while running an assessment. </p> <p>If your IAM role includes a path, you must include the path in the <code>invokerRoleName</code> parameter. For example, if your IAM role's ARN is <code>arn:aws:iam:123456789012:role/my-path/role-name</code>, you should pass <code>my-path/role-name</code>. </p> <note> <ul> <li> <p>You must have <code>iam:passRole</code> permission for this role while creating or updating the application.</p> </li> <li> <p>Currently, <code>invokerRoleName</code> accepts only <code>[A-Za-z0-9_+=,.@-]</code> characters.</p> </li> </ul> </note>"""
    cross_account_role_arns: NotRequired[
        "capo_resiliencehub.types.iam_role_arn_list.IamRoleArnList"
    ]
    """<p>Defines a list of role Amazon Resource Names (ARNs) to be used in other accounts. These ARNs are used for querying purposes while importing resources and assessing your application.</p> <note> <ul> <li> <p>These ARNs are required only when your resources are in other accounts and you have different role name in these accounts. Else, the invoker role name will be used in the other accounts.</p> </li> <li> <p>These roles must have a trust policy with <code>iam:AssumeRole</code> permission to the invoker role in the primary account.</p> </li> </ul> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: PermissionModel) -> dict:
    out: dict = {}
    import capo_resiliencehub.types.permission_model_type

    out["type"] = capo_resiliencehub.types.permission_model_type.serialize_json(
        value["type"]
    )
    if "invoker_role_name" in value:
        out["invokerRoleName"] = value["invoker_role_name"]
    if "cross_account_role_arns" in value:
        import capo_resiliencehub.types.iam_role_arn_list

        out["crossAccountRoleArns"] = (
            capo_resiliencehub.types.iam_role_arn_list.serialize_json(
                value["cross_account_role_arns"]
            )
        )
    return out


def deserialize_json(data: dict) -> PermissionModel:
    out: PermissionModel = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        import capo_resiliencehub.types.permission_model_type

        out["type"] = capo_resiliencehub.types.permission_model_type.deserialize_json(
            data["type"]
        )
    else:
        import typing

        out["type"] = typing.cast(
            "capo_resiliencehub.types.permission_model_type.PermissionModelType", ""
        )
    if data.get("invokerRoleName") is not None:
        out["invoker_role_name"] = data["invokerRoleName"]
    if data.get("crossAccountRoleArns") is not None:
        import capo_resiliencehub.types.iam_role_arn_list

        out["cross_account_role_arns"] = (
            capo_resiliencehub.types.iam_role_arn_list.deserialize_json(
                data["crossAccountRoleArns"]
            )
        )
    return out
