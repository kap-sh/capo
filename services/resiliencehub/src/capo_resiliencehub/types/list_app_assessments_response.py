"""Generated from Smithy shape ``com.amazonaws.resiliencehub#ListAppAssessmentsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_resiliencehub.types.app_assessment_summary_list
    import capo_resiliencehub.types.next_token


class ListAppAssessmentsResponse(TypedDict, closed=True):
    next_token: NotRequired["capo_resiliencehub.types.next_token.NextToken"]
    """<p>Token for the next set of results, or null if there are no more results.</p>"""
    assessment_summaries: (
        "capo_resiliencehub.types.app_assessment_summary_list.AppAssessmentSummaryList"
    )
    """<p>The summaries for the specified assessments, returned as an object. This object includes application versions, associated Amazon Resource Numbers (ARNs), cost, messages, resiliency scores, and more.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAppAssessmentsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import capo_resiliencehub.types.app_assessment_summary_list

    out["assessmentSummaries"] = (
        capo_resiliencehub.types.app_assessment_summary_list.serialize_json(
            value["assessment_summaries"]
        )
    )
    return out


def deserialize_json(data: dict) -> ListAppAssessmentsResponse:
    out: ListAppAssessmentsResponse = {}  # type: ignore[typeddict-item]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("assessmentSummaries") is not None:
        import capo_resiliencehub.types.app_assessment_summary_list

        out["assessment_summaries"] = (
            capo_resiliencehub.types.app_assessment_summary_list.deserialize_json(
                data["assessmentSummaries"]
            )
        )
    else:
        out["assessment_summaries"] = []
    return out
