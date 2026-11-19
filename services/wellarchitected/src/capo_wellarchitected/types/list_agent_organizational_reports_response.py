"""Generated from Smithy shape ``com.amazonaws.wellarchitected#ListAgentOrganizationalReportsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wellarchitected.types.next_token
    import capo_wellarchitected.types.organizational_report_summary_list


class ListAgentOrganizationalReportsResponse(TypedDict, closed=True):
    items: "capo_wellarchitected.types.organizational_report_summary_list.OrganizationalReportSummaryList"
    """<p>Page of report summaries, most-recently-created first.</p>"""
    next_token: NotRequired["capo_wellarchitected.types.next_token.NextToken"]
    """<p>Pagination token to supply on the next request, or absent when there are no more pages.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAgentOrganizationalReportsResponse) -> dict:
    out: dict = {}
    import capo_wellarchitected.types.organizational_report_summary_list

    out["items"] = (
        capo_wellarchitected.types.organizational_report_summary_list.serialize_json(
            value["items"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListAgentOrganizationalReportsResponse:
    out: ListAgentOrganizationalReportsResponse = {}  # type: ignore[typeddict-item]
    if data.get("items") is not None:
        import capo_wellarchitected.types.organizational_report_summary_list

        out["items"] = (
            capo_wellarchitected.types.organizational_report_summary_list.deserialize_json(
                data["items"]
            )
        )
    else:
        out["items"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
