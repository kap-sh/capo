"""Generated from Smithy shape ``com.amazonaws.continuum#DeleteCollectorInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_continuum.types.collector_id


class DeleteCollectorInput(TypedDict, closed=True):
    collector_id: "capo_continuum.types.collector_id.CollectorId"
    """The unique identifier of the Collector to delete."""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteCollectorInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteCollectorInput:
    out: DeleteCollectorInput = {}  # type: ignore[typeddict-item]
    return out
