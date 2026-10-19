"""Generated from Smithy shape ``com.amazonaws.amplify#ListAppsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_amplify.types.max_results_for_list_apps
    import capo_amplify.types.next_token


class ListAppsRequest(TypedDict, closed=True):
    next_token: NotRequired["capo_amplify.types.next_token.NextToken"]
    """<p>A pagination token. If non-null, the pagination token is returned in a result. Pass its value in another request to retrieve more entries. </p>"""
    max_results: NotRequired[
        "capo_amplify.types.max_results_for_list_apps.MaxResultsForListApps"
    ]
    """<p>The maximum number of records to list in a single response. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAppsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListAppsRequest:
    out: ListAppsRequest = {}  # type: ignore[typeddict-item]
    return out
