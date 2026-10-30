"""Generated from Smithy shape ``com.amazonaws.continuum#GetEnvironmentInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_continuum.types.environment_id


class GetEnvironmentInput(TypedDict, closed=True):
    environment_id: "capo_continuum.types.environment_id.EnvironmentId"
    """The unique identifier of the environment to retrieve."""


# --- restJson1 ser/de ---
def serialize_json(value: GetEnvironmentInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetEnvironmentInput:
    out: GetEnvironmentInput = {}  # type: ignore[typeddict-item]
    return out
