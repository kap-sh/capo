"""Generated from Smithy shape ``com.amazonaws.appflow#OAuth2Properties``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appflow.types.o_auth2_grant_type
    import capo_appflow.types.token_url
    import capo_appflow.types.token_url_custom_properties


class OAuth2Properties(TypedDict, closed=True):
    token_url: "capo_appflow.types.token_url.TokenUrl"
    """<p>The token URL required for OAuth 2.0 authentication.</p>"""
    o_auth2_grant_type: "capo_appflow.types.o_auth2_grant_type.OAuth2GrantType"
    """<p>The OAuth 2.0 grant type used by connector for OAuth 2.0 authentication.</p>"""
    token_url_custom_properties: NotRequired[
        "capo_appflow.types.token_url_custom_properties.TokenUrlCustomProperties"
    ]
    """<p>Associates your token URL with a map of properties that you define. Use this parameter to provide any additional details that the connector requires to authenticate your request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OAuth2Properties) -> dict:
    out: dict = {}
    out["tokenUrl"] = value["token_url"]
    import capo_appflow.types.o_auth2_grant_type

    out["oAuth2GrantType"] = capo_appflow.types.o_auth2_grant_type.serialize_json(
        value["o_auth2_grant_type"]
    )
    if "token_url_custom_properties" in value:
        import capo_appflow.types.token_url_custom_properties

        out["tokenUrlCustomProperties"] = (
            capo_appflow.types.token_url_custom_properties.serialize_json(
                value["token_url_custom_properties"]
            )
        )
    return out


def deserialize_json(data: dict) -> OAuth2Properties:
    out: OAuth2Properties = {}  # type: ignore[typeddict-item]
    if data.get("tokenUrl") is not None:
        out["token_url"] = data["tokenUrl"]
    else:
        out["token_url"] = ""
    if data.get("oAuth2GrantType") is not None:
        import capo_appflow.types.o_auth2_grant_type

        out["o_auth2_grant_type"] = (
            capo_appflow.types.o_auth2_grant_type.deserialize_json(
                data["oAuth2GrantType"]
            )
        )
    else:
        import typing

        out["o_auth2_grant_type"] = typing.cast(
            "capo_appflow.types.o_auth2_grant_type.OAuth2GrantType", ""
        )
    if data.get("tokenUrlCustomProperties") is not None:
        import capo_appflow.types.token_url_custom_properties

        out["token_url_custom_properties"] = (
            capo_appflow.types.token_url_custom_properties.deserialize_json(
                data["tokenUrlCustomProperties"]
            )
        )
    return out
