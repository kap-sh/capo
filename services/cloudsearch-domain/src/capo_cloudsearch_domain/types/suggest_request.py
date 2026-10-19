"""Generated from Smithy shape ``com.amazonaws.cloudsearchdomain#SuggestRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudsearch_domain.types.query
    import capo_cloudsearch_domain.types.suggester
    import capo_cloudsearch_domain.types.suggestions_size


class SuggestRequest(TypedDict, closed=True):
    query: "capo_cloudsearch_domain.types.query.Query"
    """<p>Specifies the string for which you want to get suggestions.</p>"""
    suggester: "capo_cloudsearch_domain.types.suggester.Suggester"
    """<p>Specifies the name of the suggester to use to find suggested matches.</p>"""
    size: NotRequired["capo_cloudsearch_domain.types.suggestions_size.SuggestionsSize"]
    """<p>Specifies the maximum number of suggestions to return. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SuggestRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> SuggestRequest:
    out: SuggestRequest = {}  # type: ignore[typeddict-item]
    return out
