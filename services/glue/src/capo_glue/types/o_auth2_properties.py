"""Generated from Smithy shape ``com.amazonaws.glue#OAuth2Properties``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.o_auth2_client_application
    import capo_glue.types.o_auth2_grant_type
    import capo_glue.types.token_url
    import capo_glue.types.token_url_parameters_map


class OAuth2Properties(TypedDict, closed=True):
    o_auth2_grant_type: NotRequired[
        "capo_glue.types.o_auth2_grant_type.OAuth2GrantType"
    ]
    """<p>The OAuth2 grant type. For example, <code>AUTHORIZATION_CODE</code>, <code>JWT_BEARER</code>, <code>REFRESH_TOKEN</code>, or <code>CLIENT_CREDENTIALS</code>.</p>"""
    o_auth2_client_application: NotRequired[
        "capo_glue.types.o_auth2_client_application.OAuth2ClientApplication"
    ]
    """<p>The client application type. For example, AWS_MANAGED or USER_MANAGED.</p>"""
    token_url: NotRequired["capo_glue.types.token_url.TokenUrl"]
    """<p>The URL of the provider's authentication server, to exchange an authorization code for an access token.</p>"""
    token_url_parameters_map: NotRequired[
        "capo_glue.types.token_url_parameters_map.TokenUrlParametersMap"
    ]
    """<p>A map of parameters that are added to the token <code>GET</code> request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OAuth2Properties) -> dict:
    out: dict = {}
    if "o_auth2_grant_type" in value:
        import capo_glue.types.o_auth2_grant_type

        out["OAuth2GrantType"] = (
            capo_glue.types.o_auth2_grant_type.serialize_aws_json_1_1(
                value["o_auth2_grant_type"]
            )
        )
    if "o_auth2_client_application" in value:
        import capo_glue.types.o_auth2_client_application

        out["OAuth2ClientApplication"] = (
            capo_glue.types.o_auth2_client_application.serialize_aws_json_1_1(
                value["o_auth2_client_application"]
            )
        )
    if "token_url" in value:
        out["TokenUrl"] = value["token_url"]
    if "token_url_parameters_map" in value:
        import capo_glue.types.token_url_parameters_map

        out["TokenUrlParametersMap"] = (
            capo_glue.types.token_url_parameters_map.serialize_aws_json_1_1(
                value["token_url_parameters_map"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> OAuth2Properties:
    out: OAuth2Properties = {}  # type: ignore[typeddict-item]
    if data.get("OAuth2GrantType") is not None:
        import capo_glue.types.o_auth2_grant_type

        out["o_auth2_grant_type"] = (
            capo_glue.types.o_auth2_grant_type.deserialize_aws_json_1_1(
                data["OAuth2GrantType"]
            )
        )
    if data.get("OAuth2ClientApplication") is not None:
        import capo_glue.types.o_auth2_client_application

        out["o_auth2_client_application"] = (
            capo_glue.types.o_auth2_client_application.deserialize_aws_json_1_1(
                data["OAuth2ClientApplication"]
            )
        )
    if data.get("TokenUrl") is not None:
        out["token_url"] = data["TokenUrl"]
    if data.get("TokenUrlParametersMap") is not None:
        import capo_glue.types.token_url_parameters_map

        out["token_url_parameters_map"] = (
            capo_glue.types.token_url_parameters_map.deserialize_aws_json_1_1(
                data["TokenUrlParametersMap"]
            )
        )
    return out
