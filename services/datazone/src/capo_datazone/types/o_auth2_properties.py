"""Generated from Smithy shape ``com.amazonaws.datazone#OAuth2Properties``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.authorization_code_properties
    import capo_datazone.types.glue_o_auth2_credentials
    import capo_datazone.types.o_auth2_client_application
    import capo_datazone.types.o_auth2_grant_type
    import capo_datazone.types.token_url_parameters_map


class OAuth2Properties(TypedDict, closed=True):
    o_auth2_grant_type: NotRequired[
        "capo_datazone.types.o_auth2_grant_type.OAuth2GrantType"
    ]
    """<p>The OAuth2 grant type of the OAuth2 properties.</p>"""
    o_auth2_client_application: NotRequired[
        "capo_datazone.types.o_auth2_client_application.OAuth2ClientApplication"
    ]
    """<p>The OAuth2 client application of the OAuth2 properties.</p>"""
    token_url: NotRequired["str"]
    """<p>The OAuth2 token URL of the OAuth2 properties.</p>"""
    token_url_parameters_map: NotRequired[
        "capo_datazone.types.token_url_parameters_map.TokenUrlParametersMap"
    ]
    """<p>The OAuth2 token URL parameter map of the OAuth2 properties.</p>"""
    authorization_code_properties: NotRequired[
        "capo_datazone.types.authorization_code_properties.AuthorizationCodeProperties"
    ]
    """<p>The authorization code properties of the OAuth2 properties.</p>"""
    o_auth2_credentials: NotRequired[
        "capo_datazone.types.glue_o_auth2_credentials.GlueOAuth2Credentials"
    ]
    """<p>The OAuth2 credentials of the OAuth2 properties.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OAuth2Properties) -> dict:
    out: dict = {}
    if "o_auth2_grant_type" in value:
        import capo_datazone.types.o_auth2_grant_type

        out["oAuth2GrantType"] = capo_datazone.types.o_auth2_grant_type.serialize_json(
            value["o_auth2_grant_type"]
        )
    if "o_auth2_client_application" in value:
        import capo_datazone.types.o_auth2_client_application

        out["oAuth2ClientApplication"] = (
            capo_datazone.types.o_auth2_client_application.serialize_json(
                value["o_auth2_client_application"]
            )
        )
    if "token_url" in value:
        out["tokenUrl"] = value["token_url"]
    if "token_url_parameters_map" in value:
        import capo_datazone.types.token_url_parameters_map

        out["tokenUrlParametersMap"] = (
            capo_datazone.types.token_url_parameters_map.serialize_json(
                value["token_url_parameters_map"]
            )
        )
    if "authorization_code_properties" in value:
        import capo_datazone.types.authorization_code_properties

        out["authorizationCodeProperties"] = (
            capo_datazone.types.authorization_code_properties.serialize_json(
                value["authorization_code_properties"]
            )
        )
    if "o_auth2_credentials" in value:
        import capo_datazone.types.glue_o_auth2_credentials

        out["oAuth2Credentials"] = (
            capo_datazone.types.glue_o_auth2_credentials.serialize_json(
                value["o_auth2_credentials"]
            )
        )
    return out


def deserialize_json(data: dict) -> OAuth2Properties:
    out: OAuth2Properties = {}  # type: ignore[typeddict-item]
    if data.get("oAuth2GrantType") is not None:
        import capo_datazone.types.o_auth2_grant_type

        out["o_auth2_grant_type"] = (
            capo_datazone.types.o_auth2_grant_type.deserialize_json(
                data["oAuth2GrantType"]
            )
        )
    if data.get("oAuth2ClientApplication") is not None:
        import capo_datazone.types.o_auth2_client_application

        out["o_auth2_client_application"] = (
            capo_datazone.types.o_auth2_client_application.deserialize_json(
                data["oAuth2ClientApplication"]
            )
        )
    if data.get("tokenUrl") is not None:
        out["token_url"] = data["tokenUrl"]
    if data.get("tokenUrlParametersMap") is not None:
        import capo_datazone.types.token_url_parameters_map

        out["token_url_parameters_map"] = (
            capo_datazone.types.token_url_parameters_map.deserialize_json(
                data["tokenUrlParametersMap"]
            )
        )
    if data.get("authorizationCodeProperties") is not None:
        import capo_datazone.types.authorization_code_properties

        out["authorization_code_properties"] = (
            capo_datazone.types.authorization_code_properties.deserialize_json(
                data["authorizationCodeProperties"]
            )
        )
    if data.get("oAuth2Credentials") is not None:
        import capo_datazone.types.glue_o_auth2_credentials

        out["o_auth2_credentials"] = (
            capo_datazone.types.glue_o_auth2_credentials.deserialize_json(
                data["oAuth2Credentials"]
            )
        )
    return out


def redact_sensitive(value: OAuth2Properties) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "o_auth2_credentials" in value:
        out["o_auth2_credentials"] = "*** Sensitive Data Redacted ***"
    return out
