"""Generated from Smithy shape ``com.amazonaws.lambdaweb#GetWebAccountSettingsRequest``."""

from typing_extensions import TypedDict


class GetWebAccountSettingsRequest(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: GetWebAccountSettingsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetWebAccountSettingsRequest:
    out: GetWebAccountSettingsRequest = {}  # type: ignore[typeddict-item]
    return out
