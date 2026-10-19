"""Generated from Smithy shape ``com.amazonaws.quicksight#PaginationConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.long
    import capo_quicksight.types.page_number


class PaginationConfiguration(TypedDict, closed=True):
    page_size: "capo_quicksight.types.long.Long"
    """<p>Indicates how many items render in one page.</p>"""
    page_number: "capo_quicksight.types.page_number.PageNumber"
    """<p>Indicates the page number.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PaginationConfiguration) -> dict:
    out: dict = {}
    out["PageSize"] = value["page_size"]
    out["PageNumber"] = value["page_number"]
    return out


def deserialize_json(data: dict) -> PaginationConfiguration:
    out: PaginationConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("PageSize") is not None:
        out["page_size"] = data["PageSize"]
    else:
        out["page_size"] = 0
    if data.get("PageNumber") is not None:
        out["page_number"] = data["PageNumber"]
    else:
        out["page_number"] = 0
    return out
