"""Generated from Smithy shape ``com.amazonaws.ssoadmin#PutApplicationGrantRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_sso_admin.types.application_arn
    import capo_sso_admin.types.grant
    import capo_sso_admin.types.grant_type


class PutApplicationGrantRequest(TypedDict, closed=True):
    application_arn: "capo_sso_admin.types.application_arn.ApplicationArn"
    """<p>Specifies the ARN of the application to update.</p>"""
    grant_type: "capo_sso_admin.types.grant_type.GrantType"
    """<p>Specifies the type of grant to update.</p>"""
    grant: "capo_sso_admin.types.grant.Grant"
    """<p>Specifies a structure that describes the grant to update.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutApplicationGrantRequest) -> dict:
    out: dict = {}
    out["ApplicationArn"] = value["application_arn"]
    import capo_sso_admin.types.grant_type

    out["GrantType"] = capo_sso_admin.types.grant_type.serialize_aws_json_1_1(
        value["grant_type"]
    )
    import capo_sso_admin.types.grant

    out["Grant"] = capo_sso_admin.types.grant.serialize_aws_json_1_1(value["grant"])
    return out


def deserialize_aws_json_1_1(data: dict) -> PutApplicationGrantRequest:
    out: PutApplicationGrantRequest = {}  # type: ignore[typeddict-item]
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
    if data.get("Grant") is not None:
        import capo_sso_admin.types.grant

        out["grant"] = capo_sso_admin.types.grant.deserialize_aws_json_1_1(
            data["Grant"]
        )
    else:
        import capo_sso_admin.types._unknown

        out["grant"] = capo_sso_admin.types._unknown.UnknownUnionMember("")
    return out
