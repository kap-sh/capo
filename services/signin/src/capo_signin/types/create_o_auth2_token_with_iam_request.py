"""Generated from Smithy shape ``com.amazonaws.signin#CreateOAuth2TokenWithIAMRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_signin.errors import DeserializationError

if TYPE_CHECKING:
    import capo_signin.types.client_credentials_grant_type


class CreateOAuth2TokenWithIAMRequest(TypedDict, closed=True):
    grant_type: (
        "capo_signin.types.client_credentials_grant_type.ClientCredentialsGrantType"
    )
    """OAuth 2.0 grant type. Must be "client_credentials"."""
    resource: "str"
    """The OAuth resource for which the access token is requested. Example: "aws-mcp.amazonaws.com"."""


# --- restJson1 ser/de ---
def serialize_json(value: CreateOAuth2TokenWithIAMRequest) -> dict:
    out: dict = {}
    out["grant_type"] = value["grant_type"]
    out["resource"] = value["resource"]
    return out


def deserialize_json(data: dict) -> CreateOAuth2TokenWithIAMRequest:
    out: CreateOAuth2TokenWithIAMRequest = {}  # type: ignore[typeddict-item]
    if data.get("grant_type") is not None:
        out["grant_type"] = data["grant_type"]
    else:
        raise DeserializationError(
            "CreateOAuth2TokenWithIAMRequest.grant_type required"
        )
    if data.get("resource") is not None:
        out["resource"] = data["resource"]
    else:
        raise DeserializationError("CreateOAuth2TokenWithIAMRequest.resource required")
    return out
