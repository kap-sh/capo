"""Generated from Smithy shape ``com.amazonaws.abusesignal#ListAbuseReportStatusesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_abuse_signal.types.correlation_id
    import capo_abuse_signal.types.next_token


class ListAbuseReportStatusesRequest(TypedDict, closed=True):
    correlation_id: NotRequired["capo_abuse_signal.types.correlation_id.CorrelationId"]
    """<p>Filters results by the reporter-provided correlation ID.</p>"""
    next_token: NotRequired["capo_abuse_signal.types.next_token.NextToken"]
    """<p>The pagination token for retrieving the next page of results. Omit this parameter to return the first page of results.</p>"""
    max_results: NotRequired["int"]
    """<p>The maximum number of results to return in a single page. Valid range: 1–50. The default is 50.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAbuseReportStatusesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListAbuseReportStatusesRequest:
    out: ListAbuseReportStatusesRequest = {}  # type: ignore[typeddict-item]
    return out
