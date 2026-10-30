"""Generated from Smithy shape ``com.amazonaws.continuum#GetCodeFindingInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_continuum.types.environment_id
    import capo_continuum.types.finding_id


class GetCodeFindingInput(TypedDict, closed=True):
    environment_id: "capo_continuum.types.environment_id.EnvironmentId"
    """The environment that owns the finding."""
    finding_id: "capo_continuum.types.finding_id.FindingId"
    """The unique identifier of the finding to retrieve."""


# --- restJson1 ser/de ---
def serialize_json(value: GetCodeFindingInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetCodeFindingInput:
    out: GetCodeFindingInput = {}  # type: ignore[typeddict-item]
    return out
