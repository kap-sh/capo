"""Generated from Smithy shape ``com.amazonaws.repostspace#ListSpacesInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_repostspace.types.list_spaces_limit


class ListSpacesInput(TypedDict, closed=True):
    next_token: NotRequired["str"]
    """<p>The token for the next set of private re:Posts to return. You receive this token from a previous ListSpaces operation.</p>"""
    max_results: NotRequired["capo_repostspace.types.list_spaces_limit.ListSpacesLimit"]
    """<p>The maximum number of private re:Posts to include in the results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSpacesInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListSpacesInput:
    out: ListSpacesInput = {}  # type: ignore[typeddict-item]
    return out
