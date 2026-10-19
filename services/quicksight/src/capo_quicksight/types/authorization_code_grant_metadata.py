"""Generated from Smithy shape ``com.amazonaws.quicksight#AuthorizationCodeGrantMetadata``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.authorization_code_grant_credentials_details
    import capo_quicksight.types.authorization_code_grant_credentials_source
    import capo_quicksight.types.endpoint


class AuthorizationCodeGrantMetadata(TypedDict, closed=True):
    base_endpoint: "capo_quicksight.types.endpoint.Endpoint"
    """<p>The base URL endpoint for the external service.</p>"""
    redirect_url: "capo_quicksight.types.endpoint.Endpoint"
    """<p>The redirect URL for the OAuth authorization flow.</p>"""
    authorization_code_grant_credentials_source: NotRequired[
        "capo_quicksight.types.authorization_code_grant_credentials_source.AuthorizationCodeGrantCredentialsSource"
    ]
    """<p>The source of the authorization code grant credentials.</p>"""
    authorization_code_grant_credentials_details: NotRequired[
        "capo_quicksight.types.authorization_code_grant_credentials_details.AuthorizationCodeGrantCredentialsDetails"
    ]
    """<p>The detailed credentials configuration for authorization code grant.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AuthorizationCodeGrantMetadata) -> dict:
    out: dict = {}
    out["BaseEndpoint"] = value["base_endpoint"]
    out["RedirectUrl"] = value["redirect_url"]
    if "authorization_code_grant_credentials_source" in value:
        import capo_quicksight.types.authorization_code_grant_credentials_source

        out["AuthorizationCodeGrantCredentialsSource"] = (
            capo_quicksight.types.authorization_code_grant_credentials_source.serialize_json(
                value["authorization_code_grant_credentials_source"]
            )
        )
    if "authorization_code_grant_credentials_details" in value:
        import capo_quicksight.types.authorization_code_grant_credentials_details

        out["AuthorizationCodeGrantCredentialsDetails"] = (
            capo_quicksight.types.authorization_code_grant_credentials_details.serialize_json(
                value["authorization_code_grant_credentials_details"]
            )
        )
    return out


def deserialize_json(data: dict) -> AuthorizationCodeGrantMetadata:
    out: AuthorizationCodeGrantMetadata = {}  # type: ignore[typeddict-item]
    if data.get("BaseEndpoint") is not None:
        out["base_endpoint"] = data["BaseEndpoint"]
    else:
        out["base_endpoint"] = ""
    if data.get("RedirectUrl") is not None:
        out["redirect_url"] = data["RedirectUrl"]
    else:
        out["redirect_url"] = ""
    if data.get("AuthorizationCodeGrantCredentialsSource") is not None:
        import capo_quicksight.types.authorization_code_grant_credentials_source

        out["authorization_code_grant_credentials_source"] = (
            capo_quicksight.types.authorization_code_grant_credentials_source.deserialize_json(
                data["AuthorizationCodeGrantCredentialsSource"]
            )
        )
    if data.get("AuthorizationCodeGrantCredentialsDetails") is not None:
        import capo_quicksight.types.authorization_code_grant_credentials_details

        out["authorization_code_grant_credentials_details"] = (
            capo_quicksight.types.authorization_code_grant_credentials_details.deserialize_json(
                data["AuthorizationCodeGrantCredentialsDetails"]
            )
        )
    return out


def redact_sensitive(value: AuthorizationCodeGrantMetadata) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "authorization_code_grant_credentials_details" in value:
        import capo_quicksight.types.authorization_code_grant_credentials_details

        out["authorization_code_grant_credentials_details"] = (
            capo_quicksight.types.authorization_code_grant_credentials_details.redact_sensitive(
                value["authorization_code_grant_credentials_details"]
            )
        )
    return out
