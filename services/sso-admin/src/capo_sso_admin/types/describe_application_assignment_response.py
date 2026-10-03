"""Generated from Smithy shape ``com.amazonaws.ssoadmin#DescribeApplicationAssignmentResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sso_admin.types.application_arn
    import capo_sso_admin.types.principal_id
    import capo_sso_admin.types.principal_type


class DescribeApplicationAssignmentResponse(TypedDict, closed=True):
    principal_type: NotRequired["capo_sso_admin.types.principal_type.PrincipalType"]
    """<p>The entity type for which the assignment will be created.</p>"""
    principal_id: NotRequired["capo_sso_admin.types.principal_id.PrincipalId"]
    """<p>An identifier for an object in IAM Identity Center, such as a user or group. PrincipalIds are GUIDs (For example, f81d4fae-7dec-11d0-a765-00a0c91e6bf6). For more information about PrincipalIds in IAM Identity Center, see the <a href="https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/welcome.html">IAM Identity Center Identity Store API Reference</a>.</p>"""
    application_arn: NotRequired["capo_sso_admin.types.application_arn.ApplicationArn"]
    """<p>Specifies the ARN of the application. For more information about ARNs, see <a href="/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Names (ARNs) and Amazon Web Services Service Namespaces</a> in the <i>Amazon Web Services General Reference</i>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeApplicationAssignmentResponse) -> dict:
    out: dict = {}
    if "principal_type" in value:
        import capo_sso_admin.types.principal_type

        out["PrincipalType"] = (
            capo_sso_admin.types.principal_type.serialize_aws_json_1_1(
                value["principal_type"]
            )
        )
    if "principal_id" in value:
        out["PrincipalId"] = value["principal_id"]
    if "application_arn" in value:
        out["ApplicationArn"] = value["application_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeApplicationAssignmentResponse:
    out: DescribeApplicationAssignmentResponse = {}  # type: ignore[typeddict-item]
    if data.get("PrincipalType") is not None:
        import capo_sso_admin.types.principal_type

        out["principal_type"] = (
            capo_sso_admin.types.principal_type.deserialize_aws_json_1_1(
                data["PrincipalType"]
            )
        )
    if data.get("PrincipalId") is not None:
        out["principal_id"] = data["PrincipalId"]
    if data.get("ApplicationArn") is not None:
        out["application_arn"] = data["ApplicationArn"]
    return out
