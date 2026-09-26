"""Generated from Smithy shape ``com.amazonaws.supportauthz#ListSupportPermitRequestsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_supportauthz.types.max_results
    import capo_supportauthz.types.next_token
    import capo_supportauthz.types.support_case_display_id


class ListSupportPermitRequestsInput(TypedDict, closed=True):
    next_token: NotRequired["capo_supportauthz.types.next_token.NextToken"]
    """<p>The token for the next page of results.</p>"""
    max_results: NotRequired["capo_supportauthz.types.max_results.MaxResults"]
    """<p>The maximum number of results to return in a single call. Valid range is 1 to 100.</p>"""
    support_case_display_id: NotRequired[
        "capo_supportauthz.types.support_case_display_id.SupportCaseDisplayId"
    ]
    """<p>Filters the results by support case display identifier.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSupportPermitRequestsInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListSupportPermitRequestsInput:
    out: ListSupportPermitRequestsInput = {}  # type: ignore[typeddict-item]
    return out
