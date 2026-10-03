"""Generated from Smithy shape ``com.amazonaws.ssoadmin#AccountAssignment``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sso_admin.types.account_id
    import capo_sso_admin.types.permission_set_arn
    import capo_sso_admin.types.principal_id
    import capo_sso_admin.types.principal_type


class AccountAssignment(TypedDict, closed=True):
    account_id: NotRequired["capo_sso_admin.types.account_id.AccountId"]
    """<p>The identifier of the Amazon Web Services account.</p>"""
    permission_set_arn: NotRequired[
        "capo_sso_admin.types.permission_set_arn.PermissionSetArn"
    ]
    """<p>The ARN of the permission set. For more information about ARNs, see <a href="/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Names (ARNs) and Amazon Web Services Service Namespaces</a> in the <i>Amazon Web Services General Reference</i>.</p>"""
    principal_type: NotRequired["capo_sso_admin.types.principal_type.PrincipalType"]
    """<p>The entity type for which the assignment will be created.</p>"""
    principal_id: NotRequired["capo_sso_admin.types.principal_id.PrincipalId"]
    """<p>An identifier for an object in IAM Identity Center, such as a user or group. PrincipalIds are GUIDs (For example, f81d4fae-7dec-11d0-a765-00a0c91e6bf6). For more information about PrincipalIds in IAM Identity Center, see the <a href="/singlesignon/latest/IdentityStoreAPIReference/welcome.html">IAM Identity Center Identity Store API Reference</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AccountAssignment) -> dict:
    out: dict = {}
    if "account_id" in value:
        out["AccountId"] = value["account_id"]
    if "permission_set_arn" in value:
        out["PermissionSetArn"] = value["permission_set_arn"]
    if "principal_type" in value:
        import capo_sso_admin.types.principal_type

        out["PrincipalType"] = (
            capo_sso_admin.types.principal_type.serialize_aws_json_1_1(
                value["principal_type"]
            )
        )
    if "principal_id" in value:
        out["PrincipalId"] = value["principal_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AccountAssignment:
    out: AccountAssignment = {}  # type: ignore[typeddict-item]
    if data.get("AccountId") is not None:
        out["account_id"] = data["AccountId"]
    if data.get("PermissionSetArn") is not None:
        out["permission_set_arn"] = data["PermissionSetArn"]
    if data.get("PrincipalType") is not None:
        import capo_sso_admin.types.principal_type

        out["principal_type"] = (
            capo_sso_admin.types.principal_type.deserialize_aws_json_1_1(
                data["PrincipalType"]
            )
        )
    if data.get("PrincipalId") is not None:
        out["principal_id"] = data["PrincipalId"]
    return out
