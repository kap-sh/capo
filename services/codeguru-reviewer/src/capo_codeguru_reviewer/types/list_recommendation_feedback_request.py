"""Generated from Smithy shape ``com.amazonaws.codegurureviewer#ListRecommendationFeedbackRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codeguru_reviewer.types.arn
    import capo_codeguru_reviewer.types.max_results
    import capo_codeguru_reviewer.types.next_token
    import capo_codeguru_reviewer.types.recommendation_ids
    import capo_codeguru_reviewer.types.user_ids


class ListRecommendationFeedbackRequest(TypedDict, closed=True):
    next_token: NotRequired["capo_codeguru_reviewer.types.next_token.NextToken"]
    """<p>If <code>nextToken</code> is returned, there are more results available. The value of <code>nextToken</code> is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged.</p>"""
    max_results: NotRequired["capo_codeguru_reviewer.types.max_results.MaxResults"]
    """<p>The maximum number of results that are returned per call. The default is 100.</p>"""
    code_review_arn: "capo_codeguru_reviewer.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the <a href="https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_CodeReview.html">CodeReview</a> object. </p>"""
    user_ids: NotRequired["capo_codeguru_reviewer.types.user_ids.UserIds"]
    """<p>An Amazon Web Services user's account ID or Amazon Resource Name (ARN). Use this ID to query the recommendation feedback for a code review from that user.</p> <p> The <code>UserId</code> is an IAM principal that can be specified as an Amazon Web Services account ID or an Amazon Resource Name (ARN). For more information, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_principal.html#Principal_specifying"> Specifying a Principal</a> in the <i>Amazon Web Services Identity and Access Management User Guide</i>.</p>"""
    recommendation_ids: NotRequired[
        "capo_codeguru_reviewer.types.recommendation_ids.RecommendationIds"
    ]
    """<p>Used to query the recommendation feedback for a given recommendation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListRecommendationFeedbackRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListRecommendationFeedbackRequest:
    out: ListRecommendationFeedbackRequest = {}  # type: ignore[typeddict-item]
    return out
