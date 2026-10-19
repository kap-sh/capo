"""Generated from Smithy shape ``com.amazonaws.quicksight#TwitterParameters``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.positive_integer
    import capo_quicksight.types.query


class TwitterParameters(TypedDict, closed=True):
    query: "capo_quicksight.types.query.Query"
    """<p>Twitter query string.</p>"""
    max_rows: "capo_quicksight.types.positive_integer.PositiveInteger"
    """<p>Maximum number of rows to query Twitter.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TwitterParameters) -> dict:
    out: dict = {}
    out["Query"] = value["query"]
    out["MaxRows"] = value["max_rows"]
    return out


def deserialize_json(data: dict) -> TwitterParameters:
    out: TwitterParameters = {}  # type: ignore[typeddict-item]
    if data.get("Query") is not None:
        out["query"] = data["Query"]
    else:
        out["query"] = ""
    if data.get("MaxRows") is not None:
        out["max_rows"] = data["MaxRows"]
    else:
        out["max_rows"] = 0
    return out
