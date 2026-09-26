"""Generated from Smithy shape ``com.amazonaws.lambdamicrovms#ListManagedMicrovmImagesInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lambda_microvms.types.string


class ListManagedMicrovmImagesInput(TypedDict, closed=True):
    max_results: NotRequired["int"]
    """<p>The maximum number of results to return in a single call.</p>"""
    next_token: NotRequired["capo_lambda_microvms.types.string.String"]
    """<p>The pagination token from a previous call. Use this token to retrieve the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListManagedMicrovmImagesInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListManagedMicrovmImagesInput:
    out: ListManagedMicrovmImagesInput = {}  # type: ignore[typeddict-item]
    return out
