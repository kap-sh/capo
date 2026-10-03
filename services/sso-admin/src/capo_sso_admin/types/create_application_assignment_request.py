"""Generated from Smithy shape ``com.amazonaws.ssoadmin#CreateApplicationAssignmentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_sso_admin.errors import DeserializationError

if TYPE_CHECKING:
    import capo_sso_admin.types.application_arn
    import capo_sso_admin.types.principal_id
    import capo_sso_admin.types.principal_type


class CreateApplicationAssignmentRequest(TypedDict, closed=True):
    application_arn: "capo_sso_admin.types.application_arn.ApplicationArn"
    """<p>The ARN of the application for which the assignment is created.</p>"""
    principal_id: "capo_sso_admin.types.principal_id.PrincipalId"
    """<p>An identifier for an object in IAM Identity Center, such as a user or group. PrincipalIds are GUIDs (For example, f81d4fae-7dec-11d0-a765-00a0c91e6bf6). For more information about PrincipalIds in IAM Identity Center, see the <a href="https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/welcome.html">IAM Identity Center Identity Store API Reference</a>.</p>"""
    principal_type: "capo_sso_admin.types.principal_type.PrincipalType"
    """<p>The entity type for which the assignment will be created.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateApplicationAssignmentRequest) -> dict:
    out: dict = {}
    out["ApplicationArn"] = value["application_arn"]
    out["PrincipalId"] = value["principal_id"]
    import capo_sso_admin.types.principal_type

    out["PrincipalType"] = capo_sso_admin.types.principal_type.serialize_aws_json_1_1(
        value["principal_type"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateApplicationAssignmentRequest:
    out: CreateApplicationAssignmentRequest = {}  # type: ignore[typeddict-item]
    if data.get("ApplicationArn") is not None:
        out["application_arn"] = data["ApplicationArn"]
    else:
        raise DeserializationError(
            "CreateApplicationAssignmentRequest.application_arn required"
        )
    if data.get("PrincipalId") is not None:
        out["principal_id"] = data["PrincipalId"]
    else:
        raise DeserializationError(
            "CreateApplicationAssignmentRequest.principal_id required"
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
            "CreateApplicationAssignmentRequest.principal_type required"
        )
    return out
