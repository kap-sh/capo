"""Generated from Smithy shape ``com.amazonaws.appflow#CustomConnectorProfileCredentials``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_appflow.errors import DeserializationError

if TYPE_CHECKING:
    import capo_appflow.types.api_key_credentials
    import capo_appflow.types.authentication_type
    import capo_appflow.types.basic_auth_credentials
    import capo_appflow.types.custom_auth_credentials
    import capo_appflow.types.o_auth2_credentials


class CustomConnectorProfileCredentials(TypedDict, closed=True):
    authentication_type: "capo_appflow.types.authentication_type.AuthenticationType"
    """<p>The authentication type that the custom connector uses for authenticating while creating a connector profile.</p>"""
    basic: NotRequired["capo_appflow.types.basic_auth_credentials.BasicAuthCredentials"]
    """<p>The basic credentials that are required for the authentication of the user.</p>"""
    oauth2: NotRequired["capo_appflow.types.o_auth2_credentials.OAuth2Credentials"]
    """<p>The OAuth 2.0 credentials required for the authentication of the user.</p>"""
    api_key: NotRequired["capo_appflow.types.api_key_credentials.ApiKeyCredentials"]
    """<p>The API keys required for the authentication of the user.</p>"""
    custom: NotRequired[
        "capo_appflow.types.custom_auth_credentials.CustomAuthCredentials"
    ]
    """<p>If the connector uses the custom authentication mechanism, this holds the required credentials.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CustomConnectorProfileCredentials) -> dict:
    out: dict = {}
    import capo_appflow.types.authentication_type

    out["authenticationType"] = capo_appflow.types.authentication_type.serialize_json(
        value["authentication_type"]
    )
    if "basic" in value:
        import capo_appflow.types.basic_auth_credentials

        out["basic"] = capo_appflow.types.basic_auth_credentials.serialize_json(
            value["basic"]
        )
    if "oauth2" in value:
        import capo_appflow.types.o_auth2_credentials

        out["oauth2"] = capo_appflow.types.o_auth2_credentials.serialize_json(
            value["oauth2"]
        )
    if "api_key" in value:
        import capo_appflow.types.api_key_credentials

        out["apiKey"] = capo_appflow.types.api_key_credentials.serialize_json(
            value["api_key"]
        )
    if "custom" in value:
        import capo_appflow.types.custom_auth_credentials

        out["custom"] = capo_appflow.types.custom_auth_credentials.serialize_json(
            value["custom"]
        )
    return out


def deserialize_json(data: dict) -> CustomConnectorProfileCredentials:
    out: CustomConnectorProfileCredentials = {}  # type: ignore[typeddict-item]
    if data.get("authenticationType") is not None:
        import capo_appflow.types.authentication_type

        out["authentication_type"] = (
            capo_appflow.types.authentication_type.deserialize_json(
                data["authenticationType"]
            )
        )
    else:
        raise DeserializationError(
            "CustomConnectorProfileCredentials.authentication_type required"
        )
    if data.get("basic") is not None:
        import capo_appflow.types.basic_auth_credentials

        out["basic"] = capo_appflow.types.basic_auth_credentials.deserialize_json(
            data["basic"]
        )
    if data.get("oauth2") is not None:
        import capo_appflow.types.o_auth2_credentials

        out["oauth2"] = capo_appflow.types.o_auth2_credentials.deserialize_json(
            data["oauth2"]
        )
    if data.get("apiKey") is not None:
        import capo_appflow.types.api_key_credentials

        out["api_key"] = capo_appflow.types.api_key_credentials.deserialize_json(
            data["apiKey"]
        )
    if data.get("custom") is not None:
        import capo_appflow.types.custom_auth_credentials

        out["custom"] = capo_appflow.types.custom_auth_credentials.deserialize_json(
            data["custom"]
        )
    return out


def redact_sensitive(value: CustomConnectorProfileCredentials) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "basic" in value:
        import capo_appflow.types.basic_auth_credentials

        out["basic"] = capo_appflow.types.basic_auth_credentials.redact_sensitive(
            value["basic"]
        )
    if "oauth2" in value:
        import capo_appflow.types.o_auth2_credentials

        out["oauth2"] = capo_appflow.types.o_auth2_credentials.redact_sensitive(
            value["oauth2"]
        )
    if "api_key" in value:
        import capo_appflow.types.api_key_credentials

        out["api_key"] = capo_appflow.types.api_key_credentials.redact_sensitive(
            value["api_key"]
        )
    if "custom" in value:
        import capo_appflow.types.custom_auth_credentials

        out["custom"] = capo_appflow.types.custom_auth_credentials.redact_sensitive(
            value["custom"]
        )
    return out
