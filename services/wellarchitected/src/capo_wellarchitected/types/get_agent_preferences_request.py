"""Generated from Smithy shape ``com.amazonaws.wellarchitected#GetAgentPreferencesRequest``."""

from typing_extensions import TypedDict


class GetAgentPreferencesRequest(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: GetAgentPreferencesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetAgentPreferencesRequest:
    out: GetAgentPreferencesRequest = {}  # type: ignore[typeddict-item]
    return out
