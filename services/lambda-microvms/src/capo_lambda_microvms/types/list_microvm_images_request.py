"""Generated from Smithy shape ``com.amazonaws.lambdamicrovms#ListMicrovmImagesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lambda_microvms.types.non_blank_string
    import capo_lambda_microvms.types.string


class ListMicrovmImagesRequest(TypedDict, closed=True):
    max_results: NotRequired["int"]
    """<p>The maximum number of results to return in a single call.</p>"""
    next_token: NotRequired["capo_lambda_microvms.types.string.String"]
    """<p>The pagination token from a previous call. Use this token to retrieve the next page of results.</p>"""
    name_filter: NotRequired[
        "capo_lambda_microvms.types.non_blank_string.NonBlankString"
    ]
    """<p>Filters images whose name contains the specified string.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListMicrovmImagesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListMicrovmImagesRequest:
    out: ListMicrovmImagesRequest = {}  # type: ignore[typeddict-item]
    return out
