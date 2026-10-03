"""Generated from Smithy shape ``com.amazonaws.ssoadmin#DescribeApplicationAssignmentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_sso_admin.errors import DeserializationError

if TYPE_CHECKING:
    import capo_sso_admin.types.application_arn
    import capo_sso_admin.types.principal_id
    import capo_sso_admin.types.principal_type


class DescribeApplicationAssignmentRequest(TypedDict, closed=True):
    application_arn: "capo_sso_admin.types.application_arn.ApplicationArn"
    """<p>Specifies the ARN of the application. For more information about ARNs, see <a href="/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Names (ARNs) and Amazon Web Services Service Namespaces</a> in the <i>Amazon Web Services General Reference</i>.</p>"""
    principal_id: "capo_sso_admin.types.principal_id.PrincipalId"
    """<p>An identifier for an object in IAM Identity Center, such as a user or group. PrincipalIds are GUIDs (For example, f81d4fae-7dec-11d0-a765-00a0c91e6bf6). For more information about PrincipalIds in IAM Identity Center, see the <a href="https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/welcome.html">IAM Identity Center Identity Store API Reference</a>.</p>"""
    principal_type: "capo_sso_admin.types.principal_type.PrincipalType"
    """<p>The entity type for which the assignment will be created.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeApplicationAssignmentRequest) -> dict:
    out: dict = {}
    out["ApplicationArn"] = value["application_arn"]
    out["PrincipalId"] = value["principal_id"]
    import capo_sso_admin.types.principal_type

    out["PrincipalType"] = capo_sso_admin.types.principal_type.serialize_aws_json_1_1(
        value["principal_type"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeApplicationAssignmentRequest:
    out: DescribeApplicationAssignmentRequest = {}  # type: ignore[typeddict-item]
    if data.get("ApplicationArn") is not None:
        out["application_arn"] = data["ApplicationArn"]
    else:
        raise DeserializationError(
            "DescribeApplicationAssignmentRequest.application_arn required"
        )
    if data.get("PrincipalId") is not None:
        out["principal_id"] = data["PrincipalId"]
    else:
        raise DeserializationError(
            "DescribeApplicationAssignmentRequest.principal_id required"
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
            "DescribeApplicationAssignmentRequest.principal_type required"
        )
    return out
