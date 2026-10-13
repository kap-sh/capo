"""Generated from Smithy shape ``com.amazonaws.connect#GetFederationTokenResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.agent_resource_id
    import capo_connect.types.arn
    import capo_connect.types.credentials
    import capo_connect.types.url


class GetFederationTokenResponse(TypedDict, closed=True):
    user_id: NotRequired["capo_connect.types.agent_resource_id.AgentResourceId"]
    """<p>The identifier for the user. This can be the ID or the ARN of the user.</p>"""
    user_arn: NotRequired["capo_connect.types.arn.ARN"]
    """<p>The Amazon Resource Name (ARN) of the user.</p>"""
    credentials: NotRequired["capo_connect.types.credentials.Credentials"]
    """<p>The credentials to use for federation.</p>"""
    sign_in_url: NotRequired["capo_connect.types.url.Url"]
    """<p>The URL to sign into the user's instance. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetFederationTokenResponse) -> dict:
    out: dict = {}
    if "user_id" in value:
        out["UserId"] = value["user_id"]
    if "user_arn" in value:
        out["UserArn"] = value["user_arn"]
    if "credentials" in value:
        import capo_connect.types.credentials

        out["Credentials"] = capo_connect.types.credentials.serialize_json(
            value["credentials"]
        )
    if "sign_in_url" in value:
        out["SignInUrl"] = value["sign_in_url"]
    return out


def deserialize_json(data: dict) -> GetFederationTokenResponse:
    out: GetFederationTokenResponse = {}  # type: ignore[typeddict-item]
    if data.get("UserId") is not None:
        out["user_id"] = data["UserId"]
    if data.get("UserArn") is not None:
        out["user_arn"] = data["UserArn"]
    if data.get("Credentials") is not None:
        import capo_connect.types.credentials

        out["credentials"] = capo_connect.types.credentials.deserialize_json(
            data["Credentials"]
        )
    if data.get("SignInUrl") is not None:
        out["sign_in_url"] = data["SignInUrl"]
    return out


def redact_sensitive(value: GetFederationTokenResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "credentials" in value:
        out["credentials"] = "*** Sensitive Data Redacted ***"
    return out
