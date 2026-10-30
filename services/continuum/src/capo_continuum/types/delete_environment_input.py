"""Generated from Smithy shape ``com.amazonaws.continuum#DeleteEnvironmentInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_continuum.types.environment_id


class DeleteEnvironmentInput(TypedDict, closed=True):
    environment_id: "capo_continuum.types.environment_id.EnvironmentId"
    """The unique identifier of the environment to delete."""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteEnvironmentInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteEnvironmentInput:
    out: DeleteEnvironmentInput = {}  # type: ignore[typeddict-item]
    return out
