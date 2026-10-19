"""Generated from Smithy shape ``com.amazonaws.ssoadmin#DeleteApplicationGrantRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_sso_admin.types.application_arn
    import capo_sso_admin.types.grant_type


class DeleteApplicationGrantRequest(TypedDict, closed=True):
    application_arn: "capo_sso_admin.types.application_arn.ApplicationArn"
    """<p>Specifies the ARN of the application with the grant to delete.</p>"""
    grant_type: "capo_sso_admin.types.grant_type.GrantType"
    """<p>Specifies the type of grant to delete from the application.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteApplicationGrantRequest) -> dict:
    out: dict = {}
    out["ApplicationArn"] = value["application_arn"]
    import capo_sso_admin.types.grant_type

    out["GrantType"] = capo_sso_admin.types.grant_type.serialize_aws_json_1_1(
        value["grant_type"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteApplicationGrantRequest:
    out: DeleteApplicationGrantRequest = {}  # type: ignore[typeddict-item]
    if data.get("ApplicationArn") is not None:
        out["application_arn"] = data["ApplicationArn"]
    else:
        out["application_arn"] = ""
    if data.get("GrantType") is not None:
        import capo_sso_admin.types.grant_type

        out["grant_type"] = capo_sso_admin.types.grant_type.deserialize_aws_json_1_1(
            data["GrantType"]
        )
    else:
        import typing

        out["grant_type"] = typing.cast("capo_sso_admin.types.grant_type.GrantType", "")
    return out
