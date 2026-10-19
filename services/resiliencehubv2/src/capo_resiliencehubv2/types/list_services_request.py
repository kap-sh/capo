"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#ListServicesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_resiliencehubv2.types.account_id
    import capo_resiliencehubv2.types.arn
    import capo_resiliencehubv2.types.assessment_status
    import capo_resiliencehubv2.types.max_results
    import capo_resiliencehubv2.types.next_token
    import capo_resiliencehubv2.types.ou_id
    import capo_resiliencehubv2.types.user_journey_id


class ListServicesRequest(TypedDict, closed=True):
    system_arn: NotRequired["capo_resiliencehubv2.types.arn.Arn"]
    user_journey_id: NotRequired[
        "capo_resiliencehubv2.types.user_journey_id.UserJourneyId"
    ]
    """<p>Filter services by user journey identifier.</p>"""
    ou_id: NotRequired["capo_resiliencehubv2.types.ou_id.OuId"]
    """<p>Filter services by organizational unit (OU) identifier.</p>"""
    account_id: NotRequired["capo_resiliencehubv2.types.account_id.AccountId"]
    """<p>Filter services by AWS account ID.</p>"""
    assessment_status: NotRequired[
        "capo_resiliencehubv2.types.assessment_status.AssessmentStatus"
    ]
    """<p>Filter services by assessment status.</p>"""
    policy_arn: NotRequired["capo_resiliencehubv2.types.arn.Arn"]
    max_results: NotRequired["capo_resiliencehubv2.types.max_results.MaxResults"]
    next_token: NotRequired["capo_resiliencehubv2.types.next_token.NextToken"]


# --- restJson1 ser/de ---
def serialize_json(value: ListServicesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListServicesRequest:
    out: ListServicesRequest = {}  # type: ignore[typeddict-item]
    return out
