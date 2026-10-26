"""Generated from Smithy shape ``com.amazonaws.ssoadmin#PutApplicationAuthenticationMethodRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_sso_admin.types.application_arn
    import capo_sso_admin.types.authentication_method
    import capo_sso_admin.types.authentication_method_type


class PutApplicationAuthenticationMethodRequest(TypedDict, closed=True):
    application_arn: "capo_sso_admin.types.application_arn.ApplicationArn"
    """<p>Specifies the ARN of the application with the authentication method to add or update.</p>"""
    authentication_method_type: (
        "capo_sso_admin.types.authentication_method_type.AuthenticationMethodType"
    )
    """<p>Specifies the type of the authentication method that you want to add or update.</p>"""
    authentication_method: (
        "capo_sso_admin.types.authentication_method.AuthenticationMethod"
    )
    """<p>Specifies a structure that describes the authentication method to add or update. The structure type you provide is determined by the <code>AuthenticationMethodType</code> parameter.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutApplicationAuthenticationMethodRequest) -> dict:
    out: dict = {}
    out["ApplicationArn"] = value["application_arn"]
    import capo_sso_admin.types.authentication_method_type

    out["AuthenticationMethodType"] = (
        capo_sso_admin.types.authentication_method_type.serialize_aws_json_1_1(
            value["authentication_method_type"]
        )
    )
    import capo_sso_admin.types.authentication_method

    out["AuthenticationMethod"] = (
        capo_sso_admin.types.authentication_method.serialize_aws_json_1_1(
            value["authentication_method"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> PutApplicationAuthenticationMethodRequest:
    out: PutApplicationAuthenticationMethodRequest = {}  # type: ignore[typeddict-item]
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
    if data.get("AuthenticationMethod") is not None:
        import capo_sso_admin.types.authentication_method

        out["authentication_method"] = (
            capo_sso_admin.types.authentication_method.deserialize_aws_json_1_1(
                data["AuthenticationMethod"]
            )
        )
    else:
        out["authentication_method"] = {"$unknown": {"name": ""}}
    return out
