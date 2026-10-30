"""Generated from Smithy shape ``com.amazonaws.neptunedata#CancelIndexRebuildInput``."""

from typing_extensions import TypedDict


class CancelIndexRebuildInput(TypedDict, closed=True):
    rebuild_id: "str"
    """<p>The unique identifier of the index rebuild job to cancel.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CancelIndexRebuildInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> CancelIndexRebuildInput:
    out: CancelIndexRebuildInput = {}  # type: ignore[typeddict-item]
    return out
