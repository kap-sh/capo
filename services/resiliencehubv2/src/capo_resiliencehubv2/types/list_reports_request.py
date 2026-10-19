"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#ListReportsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_resiliencehubv2.types.arn
    import capo_resiliencehubv2.types.max_results
    import capo_resiliencehubv2.types.next_token
    import capo_resiliencehubv2.types.report_type
    import capo_resiliencehubv2.types.test_run_id


class ListReportsRequest(TypedDict, closed=True):
    service_arn: NotRequired["capo_resiliencehubv2.types.arn.Arn"]
    """<p>Optional. If not provided, lists all reports owned by the account.</p>"""
    report_type: NotRequired["capo_resiliencehubv2.types.report_type.ReportType"]
    """<p>Filter reports by type.</p>"""
    test_run_id: NotRequired["capo_resiliencehubv2.types.test_run_id.TestRunId"]
    max_results: NotRequired["capo_resiliencehubv2.types.max_results.MaxResults"]
    next_token: NotRequired["capo_resiliencehubv2.types.next_token.NextToken"]


# --- restJson1 ser/de ---
def serialize_json(value: ListReportsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListReportsRequest:
    out: ListReportsRequest = {}  # type: ignore[typeddict-item]
    return out
