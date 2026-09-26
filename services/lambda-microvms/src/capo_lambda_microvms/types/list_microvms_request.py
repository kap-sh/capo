"""Generated from Smithy shape ``com.amazonaws.lambdamicrovms#ListMicrovmsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lambda_microvms.types.microvm_image_identifier
    import capo_lambda_microvms.types.string


class ListMicrovmsRequest(TypedDict, closed=True):
    max_results: NotRequired["int"]
    """<p>The maximum number of results to return in a single call.</p>"""
    next_token: NotRequired["capo_lambda_microvms.types.string.String"]
    """<p>The pagination token from a previous call. Use this token to retrieve the next page of results.</p>"""
    image_identifier: NotRequired[
        "capo_lambda_microvms.types.microvm_image_identifier.MicrovmImageIdentifier"
    ]
    """<p>Optional filter to list only MicroVMs running the specified image.</p>"""
    image_version: NotRequired["str"]
    """<p>Optional filter to list only MicroVMs running the specified image version.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListMicrovmsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListMicrovmsRequest:
    out: ListMicrovmsRequest = {}  # type: ignore[typeddict-item]
    return out
