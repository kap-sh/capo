"""Generated from Smithy shape ``com.amazonaws.neptunedata#GetIndexRebuildStatusInput``."""

from typing_extensions import TypedDict


class GetIndexRebuildStatusInput(TypedDict, closed=True):
    rebuild_id: "str"
    """<p>The unique identifier of the index rebuild job returned by the StartIndexRebuild operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetIndexRebuildStatusInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetIndexRebuildStatusInput:
    out: GetIndexRebuildStatusInput = {}  # type: ignore[typeddict-item]
    return out
