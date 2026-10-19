"""Generated from Smithy shape ``com.amazonaws.ssoadmin#ApplicationAssignment``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_sso_admin.types.application_arn
    import capo_sso_admin.types.principal_id
    import capo_sso_admin.types.principal_type


class ApplicationAssignment(TypedDict, closed=True):
    application_arn: "capo_sso_admin.types.application_arn.ApplicationArn"
    """<p>The ARN of the application that has principals assigned.</p>"""
    principal_id: "capo_sso_admin.types.principal_id.PrincipalId"
    """<p>The unique identifier of the principal assigned to the application.</p>"""
    principal_type: "capo_sso_admin.types.principal_type.PrincipalType"
    """<p>The type of the principal assigned to the application.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ApplicationAssignment) -> dict:
    out: dict = {}
    out["ApplicationArn"] = value["application_arn"]
    out["PrincipalId"] = value["principal_id"]
    import capo_sso_admin.types.principal_type

    out["PrincipalType"] = capo_sso_admin.types.principal_type.serialize_aws_json_1_1(
        value["principal_type"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> ApplicationAssignment:
    out: ApplicationAssignment = {}  # type: ignore[typeddict-item]
    if data.get("ApplicationArn") is not None:
        out["application_arn"] = data["ApplicationArn"]
    else:
        out["application_arn"] = ""
    if data.get("PrincipalId") is not None:
        out["principal_id"] = data["PrincipalId"]
    else:
        out["principal_id"] = ""
    if data.get("PrincipalType") is not None:
        import capo_sso_admin.types.principal_type

        out["principal_type"] = (
            capo_sso_admin.types.principal_type.deserialize_aws_json_1_1(
                data["PrincipalType"]
            )
        )
    else:
        import typing

        out["principal_type"] = typing.cast(
            "capo_sso_admin.types.principal_type.PrincipalType", ""
        )
    return out
