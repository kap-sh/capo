"""Generated from Smithy shape ``com.amazonaws.datazone#OAuth2PropertiesPatch``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.o_auth2_client_application
    import capo_datazone.types.o_auth2_grant_type
    import capo_datazone.types.token_url_parameters_map


class OAuth2PropertiesPatch(TypedDict, closed=True):
    o_auth2_grant_type: NotRequired[
        "capo_datazone.types.o_auth2_grant_type.OAuth2GrantType"
    ]
    """<p>The OAuth2 grant type of the OAuth2 properties to update.</p>"""
    o_auth2_client_application: NotRequired[
        "capo_datazone.types.o_auth2_client_application.OAuth2ClientApplication"
    ]
    """<p>The OAuth2 client application of the OAuth2 properties to update.</p>"""
    token_url: NotRequired["str"]
    """<p>The OAuth2 token URL of the OAuth2 properties to update.</p>"""
    token_url_parameters_map: NotRequired[
        "capo_datazone.types.token_url_parameters_map.TokenUrlParametersMap"
    ]
    """<p>The OAuth2 token URL parameter map of the OAuth2 properties to update, for example the scope. If you specify an empty map, the existing parameters are kept.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OAuth2PropertiesPatch) -> dict:
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
    return out


def deserialize_json(data: dict) -> OAuth2PropertiesPatch:
    out: OAuth2PropertiesPatch = {}  # type: ignore[typeddict-item]
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
    return out
