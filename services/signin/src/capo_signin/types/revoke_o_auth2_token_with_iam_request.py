"""Generated from Smithy shape ``com.amazonaws.signin#RevokeOAuth2TokenWithIAMRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_signin.errors import DeserializationError

if TYPE_CHECKING:
    import capo_signin.types.revocation_token


class RevokeOAuth2TokenWithIAMRequest(TypedDict, closed=True):
    token: "capo_signin.types.revocation_token.RevocationToken"
    """The refresh_token to revoke. Must be a refresh_token issued by AWS Sign-In (prefix "ASOR"); access_tokens are not accepted for revocation."""


# --- restJson1 ser/de ---
def serialize_json(value: RevokeOAuth2TokenWithIAMRequest) -> dict:
    out: dict = {}
    out["token"] = value["token"]
    return out


def deserialize_json(data: dict) -> RevokeOAuth2TokenWithIAMRequest:
    out: RevokeOAuth2TokenWithIAMRequest = {}  # type: ignore[typeddict-item]
    if data.get("token") is not None:
        out["token"] = data["token"]
    else:
        raise DeserializationError("RevokeOAuth2TokenWithIAMRequest.token required")
    return out
