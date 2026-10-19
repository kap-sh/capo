"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#ListFailureModeAssessmentsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_resiliencehubv2.types.arn
    import capo_resiliencehubv2.types.assessment_sort_field
    import capo_resiliencehubv2.types.assessment_status_list
    import capo_resiliencehubv2.types.max_results
    import capo_resiliencehubv2.types.next_token
    import capo_resiliencehubv2.types.sort_order


class ListFailureModeAssessmentsRequest(TypedDict, closed=True):
    service_arn: "capo_resiliencehubv2.types.arn.Arn"
    assessment_statuses: NotRequired[
        "capo_resiliencehubv2.types.assessment_status_list.AssessmentStatusList"
    ]
    """<p>Specifies the assessment statuses to include in the results.</p>"""
    started_after: NotRequired["datetime.datetime"]
    """<p>Specifies that only assessments that started at or after this timestamp appear in the results.</p>"""
    ended_before: NotRequired["datetime.datetime"]
    """<p>Specifies that only assessments that ended at or before this timestamp appear in the results.</p>"""
    sort_by: NotRequired[
        "capo_resiliencehubv2.types.assessment_sort_field.AssessmentSortField"
    ]
    """<p>The field to use for sorting failure mode assessments.</p>"""
    sort_order: NotRequired["capo_resiliencehubv2.types.sort_order.SortOrder"]
    """<p>The sort order for results.</p>"""
    max_results: NotRequired["capo_resiliencehubv2.types.max_results.MaxResults"]
    next_token: NotRequired["capo_resiliencehubv2.types.next_token.NextToken"]


# --- restJson1 ser/de ---
def serialize_json(value: ListFailureModeAssessmentsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListFailureModeAssessmentsRequest:
    out: ListFailureModeAssessmentsRequest = {}  # type: ignore[typeddict-item]
    return out
