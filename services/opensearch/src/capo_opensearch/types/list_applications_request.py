"""Generated from Smithy shape ``com.amazonaws.opensearch#ListApplicationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearch.types.application_statuses
    import capo_opensearch.types.max_results
    import capo_opensearch.types.next_token


class ListApplicationsRequest(TypedDict, closed=True):
    next_token: NotRequired["capo_opensearch.types.next_token.NextToken"]
    statuses: NotRequired[
        "capo_opensearch.types.application_statuses.ApplicationStatuses"
    ]
    """<p>Filters the list of OpenSearch applications by status. Possible values: <code>CREATING</code>, <code>UPDATING</code>, <code>DELETING</code>, <code>FAILED</code>, <code>ACTIVE</code>, and <code>DELETED</code>.</p>"""
    max_results: NotRequired["capo_opensearch.types.max_results.MaxResults"]


# --- restJson1 ser/de ---
def serialize_json(value: ListApplicationsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListApplicationsRequest:
    out: ListApplicationsRequest = {}  # type: ignore[typeddict-item]
    return out
