"""Generated from Smithy shape ``com.amazonaws.continuum#GetCollectorInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_continuum.types.collector_id


class GetCollectorInput(TypedDict, closed=True):
    collector_id: "capo_continuum.types.collector_id.CollectorId"
    """The unique identifier of the Collector to retrieve."""


# --- restJson1 ser/de ---
def serialize_json(value: GetCollectorInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetCollectorInput:
    out: GetCollectorInput = {}  # type: ignore[typeddict-item]
    return out
