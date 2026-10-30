"""Generated from Smithy shape ``com.amazonaws.continuum#OAuthCodeChallengeMethod``."""

from typing import Literal, TypeAlias, cast

"""The PKCE code challenge method (RFC 7636)."""
OAuthCodeChallengeMethod: TypeAlias = Literal["S256",]


# --- restJson1 ser/de ---
def serialize_json(value: OAuthCodeChallengeMethod) -> str:
    return value


def deserialize_json(data: str) -> OAuthCodeChallengeMethod:
    return cast(OAuthCodeChallengeMethod, data)
