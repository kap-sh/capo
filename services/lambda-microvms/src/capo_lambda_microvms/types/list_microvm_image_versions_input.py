"""Generated from Smithy shape ``com.amazonaws.lambdamicrovms#ListMicrovmImageVersionsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lambda_microvms.types.microvm_image_identifier
    import capo_lambda_microvms.types.string


class ListMicrovmImageVersionsInput(TypedDict, closed=True):
    max_results: NotRequired["int"]
    """<p>The maximum number of results to return in a single call.</p>"""
    next_token: NotRequired["capo_lambda_microvms.types.string.String"]
    """<p>The pagination token from a previous call. Use this token to retrieve the next page of results.</p>"""
    image_identifier: (
        "capo_lambda_microvms.types.microvm_image_identifier.MicrovmImageIdentifier"
    )
    """<p>The unique identifier (ARN or ID) of the MicroVM image to list versions for.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListMicrovmImageVersionsInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListMicrovmImageVersionsInput:
    out: ListMicrovmImageVersionsInput = {}  # type: ignore[typeddict-item]
    return out
