"""Generated from Smithy shape ``com.amazonaws.ssoadmin#GetApplicationAuthenticationMethodRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_sso_admin.types.application_arn
    import capo_sso_admin.types.authentication_method_type


class GetApplicationAuthenticationMethodRequest(TypedDict, closed=True):
    application_arn: "capo_sso_admin.types.application_arn.ApplicationArn"
    """<p>Specifies the ARN of the application.</p>"""
    authentication_method_type: (
        "capo_sso_admin.types.authentication_method_type.AuthenticationMethodType"
    )
    """<p>Specifies the type of authentication method for which you want details.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetApplicationAuthenticationMethodRequest) -> dict:
    out: dict = {}
    out["ApplicationArn"] = value["application_arn"]
    import capo_sso_admin.types.authentication_method_type

    out["AuthenticationMethodType"] = (
        capo_sso_admin.types.authentication_method_type.serialize_aws_json_1_1(
            value["authentication_method_type"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetApplicationAuthenticationMethodRequest:
    out: GetApplicationAuthenticationMethodRequest = {}  # type: ignore[typeddict-item]
    if data.get("ApplicationArn") is not None:
        out["application_arn"] = data["ApplicationArn"]
    else:
        out["application_arn"] = ""
    if data.get("AuthenticationMethodType") is not None:
        import capo_sso_admin.types.authentication_method_type

        out["authentication_method_type"] = (
            capo_sso_admin.types.authentication_method_type.deserialize_aws_json_1_1(
                data["AuthenticationMethodType"]
            )
        )
    else:
        import typing

        out["authentication_method_type"] = typing.cast(
            "capo_sso_admin.types.authentication_method_type.AuthenticationMethodType",
            "",
        )
    return out
