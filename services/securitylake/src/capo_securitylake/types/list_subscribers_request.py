"""Generated from Smithy shape ``com.amazonaws.securitylake#ListSubscribersRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securitylake.types.max_results
    import capo_securitylake.types.next_token


class ListSubscribersRequest(TypedDict, closed=True):
    next_token: NotRequired["capo_securitylake.types.next_token.NextToken"]
    """<p>If nextToken is returned, there are more results available. You can repeat the call using the returned token to retrieve the next page.</p>"""
    max_results: NotRequired["capo_securitylake.types.max_results.MaxResults"]
    """<p>The maximum number of accounts for which the configuration is displayed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSubscribersRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListSubscribersRequest:
    out: ListSubscribersRequest = {}  # type: ignore[typeddict-item]
    return out
