"""Generated from Smithy shape ``com.amazonaws.signin#OAuth2ErrorCode``."""

from typing import Literal, TypeAlias, cast

"""OAuth 2.0 error codes returned by the server Standard OAuth 2.0 error codes used in error responses to indicate the specific type of error that occurred during token operations."""
OAuth2ErrorCode: TypeAlias = Literal[
    "TOKEN_EXPIRED",
    "USER_CREDENTIALS_CHANGED",
    "INSUFFICIENT_PERMISSIONS",
    "AUTHCODE_EXPIRED",
    "server_error",
    "INVALID_REQUEST",
    "RESOURCE_NOT_FOUND",
    "CONFLICT",
    "SERVICE_QUOTA_EXCEEDED",
    "unsupported_grant_type",
    "invalid_request",
    "invalid_grant",
    "invalid_scope",
    "invalid_target",
    "rate_exceeded",
    "service_unavailable",
]


# --- restJson1 ser/de ---
def serialize_json(value: OAuth2ErrorCode) -> str:
    return value


def deserialize_json(data: str) -> OAuth2ErrorCode:
    return cast(OAuth2ErrorCode, data)
