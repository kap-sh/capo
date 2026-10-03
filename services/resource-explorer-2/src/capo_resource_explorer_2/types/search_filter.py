"""Generated from Smithy shape ``com.amazonaws.resourceexplorer2#SearchFilter``."""

from typing_extensions import TypedDict

from capo_resource_explorer_2.errors import DeserializationError


class SearchFilter(TypedDict, closed=True):
    filter_string: "str"
    """<p>The string that contains the search keywords, prefixes, and operators to control the results that can be returned by a <a>Search</a> operation. For more details, see <a href="https://docs.aws.amazon.com/resource-explorer/latest/APIReference/about-query-syntax.html">Search query syntax</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchFilter) -> dict:
    out: dict = {}
    out["FilterString"] = value["filter_string"]
    return out


def deserialize_json(data: dict) -> SearchFilter:
    out: SearchFilter = {}  # type: ignore[typeddict-item]
    if data.get("FilterString") is not None:
        out["filter_string"] = data["FilterString"]
    else:
        raise DeserializationError("SearchFilter.filter_string required")
    return out
