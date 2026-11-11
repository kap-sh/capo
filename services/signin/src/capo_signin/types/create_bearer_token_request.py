"""Generated from Smithy shape ``com.amazonaws.signin#CreateBearerTokenRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_signin.types.client_credentials_grant_type
    import capo_signin.types.resource
    import capo_signin.types.token_duration


class CreateBearerTokenRequest(TypedDict, closed=True):
    grant_type: (
        "capo_signin.types.client_credentials_grant_type.ClientCredentialsGrantType"
    )
    """The grant type. Must be "client_credentials"."""
    resource: "capo_signin.types.resource.Resource"
    """The AWS service the bearer token is for. Example: "ecr.amazonaws.com"."""
    duration_seconds: NotRequired["capo_signin.types.token_duration.TokenDuration"]
    """The requested token lifetime in seconds, from 300 (5 minutes) up to the maximum allowed for the service, currently 43200 (12 hours). If omitted, the token is valid for 12 hours."""


# --- restJson1 ser/de ---
def serialize_json(value: CreateBearerTokenRequest) -> dict:
    out: dict = {}
    out["grant_type"] = value["grant_type"]
    out["resource"] = value["resource"]
    if "duration_seconds" in value:
        out["duration"] = value["duration_seconds"]
    return out


def deserialize_json(data: dict) -> CreateBearerTokenRequest:
    out: CreateBearerTokenRequest = {}  # type: ignore[typeddict-item]
    if data.get("grant_type") is not None:
        out["grant_type"] = data["grant_type"]
    else:
        out["grant_type"] = ""
    if data.get("resource") is not None:
        out["resource"] = data["resource"]
    else:
        out["resource"] = ""
    if data.get("duration") is not None:
        out["duration_seconds"] = data["duration"]
    return out
