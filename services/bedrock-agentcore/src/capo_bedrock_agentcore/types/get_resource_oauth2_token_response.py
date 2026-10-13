"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#GetResourceOauth2TokenResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.access_token_type
    import capo_bedrock_agentcore.types.authorization_url_type
    import capo_bedrock_agentcore.types.request_uri
    import capo_bedrock_agentcore.types.session_status


class GetResourceOauth2TokenResponse(TypedDict, closed=True):
    authorization_url: NotRequired[
        "capo_bedrock_agentcore.types.authorization_url_type.AuthorizationUrlType"
    ]
    """<p>The URL to initiate the authorization process, provided when the access token requires user authorization.</p>"""
    access_token: NotRequired[
        "capo_bedrock_agentcore.types.access_token_type.AccessTokenType"
    ]
    """<p>The OAuth 2.0 access token to use.</p>"""
    session_uri: NotRequired["capo_bedrock_agentcore.types.request_uri.RequestUri"]
    """<p>Unique identifier for the user's authorization session for retrieving OAuth2 tokens. This matches the sessionId from the request and can be used to track the session state.</p>"""
    session_status: NotRequired[
        "capo_bedrock_agentcore.types.session_status.SessionStatus"
    ]
    """<p>Status indicating whether the user's authorization session is in progress or has failed. This helps determine the next steps in the OAuth2 authentication flow.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetResourceOauth2TokenResponse) -> dict:
    out: dict = {}
    if "authorization_url" in value:
        out["authorizationUrl"] = value["authorization_url"]
    if "access_token" in value:
        out["accessToken"] = value["access_token"]
    if "session_uri" in value:
        out["sessionUri"] = value["session_uri"]
    if "session_status" in value:
        import capo_bedrock_agentcore.types.session_status

        out["sessionStatus"] = (
            capo_bedrock_agentcore.types.session_status.serialize_json(
                value["session_status"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetResourceOauth2TokenResponse:
    out: GetResourceOauth2TokenResponse = {}  # type: ignore[typeddict-item]
    if data.get("authorizationUrl") is not None:
        out["authorization_url"] = data["authorizationUrl"]
    if data.get("accessToken") is not None:
        out["access_token"] = data["accessToken"]
    if data.get("sessionUri") is not None:
        out["session_uri"] = data["sessionUri"]
    if data.get("sessionStatus") is not None:
        import capo_bedrock_agentcore.types.session_status

        out["session_status"] = (
            capo_bedrock_agentcore.types.session_status.deserialize_json(
                data["sessionStatus"]
            )
        )
    return out


def redact_sensitive(value: GetResourceOauth2TokenResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "authorization_url" in value:
        out["authorization_url"] = "*** Sensitive Data Redacted ***"
    if "access_token" in value:
        out["access_token"] = "*** Sensitive Data Redacted ***"
    return out
