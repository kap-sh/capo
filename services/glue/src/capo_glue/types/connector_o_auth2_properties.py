"""Generated from Smithy shape ``com.amazonaws.glue#ConnectorOAuth2Properties``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.client_credentials_properties
    import capo_glue.types.connector_authorization_code_properties
    import capo_glue.types.connector_o_auth2_grant_type
    import capo_glue.types.jwt_bearer_properties


class ConnectorOAuth2Properties(TypedDict, closed=True):
    o_auth2_grant_type: (
        "capo_glue.types.connector_o_auth2_grant_type.ConnectorOAuth2GrantType"
    )
    """<p>The OAuth2 grant type to use for authentication, such as CLIENT_CREDENTIALS, JWT_BEARER, or AUTHORIZATION_CODE.</p>"""
    client_credentials_properties: NotRequired[
        "capo_glue.types.client_credentials_properties.ClientCredentialsProperties"
    ]
    """<p>Configuration properties specific to the OAuth2 Client Credentials grant type flow.</p>"""
    jwt_bearer_properties: NotRequired[
        "capo_glue.types.jwt_bearer_properties.JWTBearerProperties"
    ]
    """<p>Configuration properties specific to the OAuth2 JWT Bearer grant type flow.</p>"""
    authorization_code_properties: NotRequired[
        "capo_glue.types.connector_authorization_code_properties.ConnectorAuthorizationCodeProperties"
    ]
    """<p>Configuration properties specific to the OAuth2 Authorization Code grant type flow.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConnectorOAuth2Properties) -> dict:
    out: dict = {}
    import capo_glue.types.connector_o_auth2_grant_type

    out["OAuth2GrantType"] = (
        capo_glue.types.connector_o_auth2_grant_type.serialize_aws_json_1_1(
            value["o_auth2_grant_type"]
        )
    )
    if "client_credentials_properties" in value:
        import capo_glue.types.client_credentials_properties

        out["ClientCredentialsProperties"] = (
            capo_glue.types.client_credentials_properties.serialize_aws_json_1_1(
                value["client_credentials_properties"]
            )
        )
    if "jwt_bearer_properties" in value:
        import capo_glue.types.jwt_bearer_properties

        out["JWTBearerProperties"] = (
            capo_glue.types.jwt_bearer_properties.serialize_aws_json_1_1(
                value["jwt_bearer_properties"]
            )
        )
    if "authorization_code_properties" in value:
        import capo_glue.types.connector_authorization_code_properties

        out["AuthorizationCodeProperties"] = (
            capo_glue.types.connector_authorization_code_properties.serialize_aws_json_1_1(
                value["authorization_code_properties"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ConnectorOAuth2Properties:
    out: ConnectorOAuth2Properties = {}  # type: ignore[typeddict-item]
    if data.get("OAuth2GrantType") is not None:
        import capo_glue.types.connector_o_auth2_grant_type

        out["o_auth2_grant_type"] = (
            capo_glue.types.connector_o_auth2_grant_type.deserialize_aws_json_1_1(
                data["OAuth2GrantType"]
            )
        )
    else:
        import typing

        out["o_auth2_grant_type"] = typing.cast(
            "capo_glue.types.connector_o_auth2_grant_type.ConnectorOAuth2GrantType", ""
        )
    if data.get("ClientCredentialsProperties") is not None:
        import capo_glue.types.client_credentials_properties

        out["client_credentials_properties"] = (
            capo_glue.types.client_credentials_properties.deserialize_aws_json_1_1(
                data["ClientCredentialsProperties"]
            )
        )
    if data.get("JWTBearerProperties") is not None:
        import capo_glue.types.jwt_bearer_properties

        out["jwt_bearer_properties"] = (
            capo_glue.types.jwt_bearer_properties.deserialize_aws_json_1_1(
                data["JWTBearerProperties"]
            )
        )
    if data.get("AuthorizationCodeProperties") is not None:
        import capo_glue.types.connector_authorization_code_properties

        out["authorization_code_properties"] = (
            capo_glue.types.connector_authorization_code_properties.deserialize_aws_json_1_1(
                data["AuthorizationCodeProperties"]
            )
        )
    return out
