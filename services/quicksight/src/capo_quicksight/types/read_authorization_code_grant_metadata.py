"""Generated from Smithy shape ``com.amazonaws.quicksight#ReadAuthorizationCodeGrantMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.authorization_code_grant_credentials_source
    import capo_quicksight.types.endpoint
    import capo_quicksight.types.read_authorization_code_grant_credentials_details


class ReadAuthorizationCodeGrantMetadata(TypedDict, closed=True):
    base_endpoint: "capo_quicksight.types.endpoint.Endpoint"
    """<p>The base endpoint URL for the OAuth2 authorization code grant flow.</p>"""
    redirect_url: "capo_quicksight.types.endpoint.Endpoint"
    """<p>The redirect URL where the authorization server will send the user after authorization.</p>"""
    read_authorization_code_grant_credentials_details: NotRequired[
        "capo_quicksight.types.read_authorization_code_grant_credentials_details.ReadAuthorizationCodeGrantCredentialsDetails"
    ]
    """<p>The read-only credentials details for the authorization code grant flow.</p>"""
    authorization_code_grant_credentials_source: NotRequired[
        "capo_quicksight.types.authorization_code_grant_credentials_source.AuthorizationCodeGrantCredentialsSource"
    ]
    """<p>The source of credentials for the authorization code grant flow.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ReadAuthorizationCodeGrantMetadata) -> dict:
    out: dict = {}
    out["BaseEndpoint"] = value["base_endpoint"]
    out["RedirectUrl"] = value["redirect_url"]
    if "read_authorization_code_grant_credentials_details" in value:
        import capo_quicksight.types.read_authorization_code_grant_credentials_details

        out["ReadAuthorizationCodeGrantCredentialsDetails"] = (
            capo_quicksight.types.read_authorization_code_grant_credentials_details.serialize_json(
                value["read_authorization_code_grant_credentials_details"]
            )
        )
    if "authorization_code_grant_credentials_source" in value:
        import capo_quicksight.types.authorization_code_grant_credentials_source

        out["AuthorizationCodeGrantCredentialsSource"] = (
            capo_quicksight.types.authorization_code_grant_credentials_source.serialize_json(
                value["authorization_code_grant_credentials_source"]
            )
        )
    return out


def deserialize_json(data: dict) -> ReadAuthorizationCodeGrantMetadata:
    out: ReadAuthorizationCodeGrantMetadata = {}  # type: ignore[typeddict-item]
    if data.get("BaseEndpoint") is not None:
        out["base_endpoint"] = data["BaseEndpoint"]
    else:
        out["base_endpoint"] = ""
    if data.get("RedirectUrl") is not None:
        out["redirect_url"] = data["RedirectUrl"]
    else:
        out["redirect_url"] = ""
    if data.get("ReadAuthorizationCodeGrantCredentialsDetails") is not None:
        import capo_quicksight.types.read_authorization_code_grant_credentials_details

        out["read_authorization_code_grant_credentials_details"] = (
            capo_quicksight.types.read_authorization_code_grant_credentials_details.deserialize_json(
                data["ReadAuthorizationCodeGrantCredentialsDetails"]
            )
        )
    if data.get("AuthorizationCodeGrantCredentialsSource") is not None:
        import capo_quicksight.types.authorization_code_grant_credentials_source

        out["authorization_code_grant_credentials_source"] = (
            capo_quicksight.types.authorization_code_grant_credentials_source.deserialize_json(
                data["AuthorizationCodeGrantCredentialsSource"]
            )
        )
    return out
