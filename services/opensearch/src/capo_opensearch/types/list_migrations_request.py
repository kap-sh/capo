"""Generated from Smithy shape ``com.amazonaws.opensearch#ListMigrationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearch.types.application_id
    import capo_opensearch.types.integer
    import capo_opensearch.types.string


class ListMigrationsRequest(TypedDict, closed=True):
    application_id: "capo_opensearch.types.application_id.ApplicationId"
    """<p>The unique identifier of the OpenSearch application to list migrations for.</p>"""
    status: NotRequired["capo_opensearch.types.string.String"]
    """<p>Filters the results by migration status. Valid values are <code>PENDING</code>, <code>IN_PROGRESS</code>, <code>SUCCEEDED</code>, and <code>FAILED</code>.</p>"""
    max_results: NotRequired["capo_opensearch.types.integer.Integer"]
    """<p>The maximum number of results to return in a single call.</p>"""
    next_token: NotRequired["capo_opensearch.types.string.String"]
    """<p>The pagination token from a previous call to retrieve the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListMigrationsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListMigrationsRequest:
    out: ListMigrationsRequest = {}  # type: ignore[typeddict-item]
    return out
