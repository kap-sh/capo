"""Generated from Smithy shape ``com.amazonaws.supportauthz#ListActionsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_supportauthz.types.max_results
    import capo_supportauthz.types.next_token
    import capo_supportauthz.types.service


class ListActionsInput(TypedDict, closed=True):
    next_token: NotRequired["capo_supportauthz.types.next_token.NextToken"]
    """<p>The token for the next page of results.</p>"""
    max_results: NotRequired["capo_supportauthz.types.max_results.MaxResults"]
    """<p>The maximum number of results to return in a single call. Valid range is 1 to 100.</p>"""
    service: "capo_supportauthz.types.service.Service"
    """<p>The name of the AWS service for which to list available support actions.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListActionsInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListActionsInput:
    out: ListActionsInput = {}  # type: ignore[typeddict-item]
    return out
