"""Generated from Smithy shape ``com.amazonaws.wellarchitected#ListAgentOrganizationalReportsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wellarchitected.types.max_results
    import capo_wellarchitected.types.next_token
    import capo_wellarchitected.types.organizational_report_state


class ListAgentOrganizationalReportsRequest(TypedDict, closed=True):
    max_results: NotRequired["capo_wellarchitected.types.max_results.MaxResults"]
    """<p>Maximum number of items to return in a single page. Defaults to 100.</p>"""
    next_token: NotRequired["capo_wellarchitected.types.next_token.NextToken"]
    """<p>Pagination token from a previous ListAgentOrganizationalReports response. Absent on the first page.</p>"""
    state: NotRequired[
        "capo_wellarchitected.types.organizational_report_state.OrganizationalReportState"
    ]
    """<p>Optional filter restricting the response to reports in a single lifecycle state.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAgentOrganizationalReportsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListAgentOrganizationalReportsRequest:
    out: ListAgentOrganizationalReportsRequest = {}  # type: ignore[typeddict-item]
    return out
