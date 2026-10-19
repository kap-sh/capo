"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#ListFailureModeFindingsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_resiliencehubv2.types.arn
    import capo_resiliencehubv2.types.failure_category
    import capo_resiliencehubv2.types.finding_severity
    import capo_resiliencehubv2.types.finding_status
    import capo_resiliencehubv2.types.max_results
    import capo_resiliencehubv2.types.next_token


class ListFailureModeFindingsRequest(TypedDict, closed=True):
    service_arn: "capo_resiliencehubv2.types.arn.Arn"
    severity: NotRequired["capo_resiliencehubv2.types.finding_severity.FindingSeverity"]
    """<p>Filter findings by severity.</p>"""
    failure_category: NotRequired[
        "capo_resiliencehubv2.types.failure_category.FailureCategory"
    ]
    """<p>Filter findings by failure category.</p>"""
    status: NotRequired["capo_resiliencehubv2.types.finding_status.FindingStatus"]
    """<p>Filter findings by status.</p>"""
    max_results: NotRequired["capo_resiliencehubv2.types.max_results.MaxResults"]
    next_token: NotRequired["capo_resiliencehubv2.types.next_token.NextToken"]


# --- restJson1 ser/de ---
def serialize_json(value: ListFailureModeFindingsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListFailureModeFindingsRequest:
    out: ListFailureModeFindingsRequest = {}  # type: ignore[typeddict-item]
    return out
