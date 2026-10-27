"""Generated from Smithy shape ``com.amazonaws.ivsrealtime#RevokeConnectionTokenResponse``."""

from typing_extensions import TypedDict


class RevokeConnectionTokenResponse(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: RevokeConnectionTokenResponse) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> RevokeConnectionTokenResponse:
    out: RevokeConnectionTokenResponse = {}  # type: ignore[typeddict-item]
    return out
