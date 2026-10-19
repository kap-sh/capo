"""Generated from Smithy shape ``com.amazonaws.neptunedata#GetRDFGraphSummaryInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_neptunedata.types.graph_summary_type


class GetRDFGraphSummaryInput(TypedDict, closed=True):
    mode: NotRequired["capo_neptunedata.types.graph_summary_type.GraphSummaryType"]
    """<p>Mode can take one of two values: <code>BASIC</code> (the default), and <code>DETAILED</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetRDFGraphSummaryInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetRDFGraphSummaryInput:
    out: GetRDFGraphSummaryInput = {}  # type: ignore[typeddict-item]
    return out
