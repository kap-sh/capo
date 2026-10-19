"""Generated from Smithy shape ``com.amazonaws.ssoadmin#GetApplicationGrantRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_sso_admin.types.application_arn
    import capo_sso_admin.types.grant_type


class GetApplicationGrantRequest(TypedDict, closed=True):
    application_arn: "capo_sso_admin.types.application_arn.ApplicationArn"
    """<p>Specifies the ARN of the application that contains the grant.</p>"""
    grant_type: "capo_sso_admin.types.grant_type.GrantType"
    """<p>Specifies the type of grant.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetApplicationGrantRequest) -> dict:
    out: dict = {}
    out["ApplicationArn"] = value["application_arn"]
    import capo_sso_admin.types.grant_type

    out["GrantType"] = capo_sso_admin.types.grant_type.serialize_aws_json_1_1(
        value["grant_type"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetApplicationGrantRequest:
    out: GetApplicationGrantRequest = {}  # type: ignore[typeddict-item]
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
