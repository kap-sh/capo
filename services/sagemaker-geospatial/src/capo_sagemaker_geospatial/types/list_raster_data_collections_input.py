"""Generated from Smithy shape ``com.amazonaws.sagemakergeospatial#ListRasterDataCollectionsInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker_geospatial.types.next_token


class ListRasterDataCollectionsInput(TypedDict, closed=True):
    next_token: NotRequired["capo_sagemaker_geospatial.types.next_token.NextToken"]
    """<p>If the previous response was truncated, you receive this token. Use it in your next request to receive the next set of results.</p>"""
    max_results: NotRequired["int"]
    """<p>The total number of items to return.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListRasterDataCollectionsInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListRasterDataCollectionsInput:
    out: ListRasterDataCollectionsInput = {}  # type: ignore[typeddict-item]
    return out


def redact_sensitive(value: ListRasterDataCollectionsInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "next_token" in value:
        out["next_token"] = "*** Sensitive Data Redacted ***"
    return out
