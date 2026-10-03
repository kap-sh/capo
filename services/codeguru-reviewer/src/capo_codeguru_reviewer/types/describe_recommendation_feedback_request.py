"""Generated from Smithy shape ``com.amazonaws.codegurureviewer#DescribeRecommendationFeedbackRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codeguru_reviewer.types.arn
    import capo_codeguru_reviewer.types.recommendation_id
    import capo_codeguru_reviewer.types.user_id


class DescribeRecommendationFeedbackRequest(TypedDict, closed=True):
    code_review_arn: "capo_codeguru_reviewer.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the <a href="https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_CodeReview.html">CodeReview</a> object. </p>"""
    recommendation_id: "capo_codeguru_reviewer.types.recommendation_id.RecommendationId"
    """<p>The recommendation ID that can be used to track the provided recommendations and then to collect the feedback.</p>"""
    user_id: NotRequired["capo_codeguru_reviewer.types.user_id.UserId"]
    """<p>Optional parameter to describe the feedback for a given user. If this is not supplied, it defaults to the user making the request.</p> <p> The <code>UserId</code> is an IAM principal that can be specified as an Amazon Web Services account ID or an Amazon Resource Name (ARN). For more information, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_principal.html#Principal_specifying"> Specifying a Principal</a> in the <i>Amazon Web Services Identity and Access Management User Guide</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeRecommendationFeedbackRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeRecommendationFeedbackRequest:
    out: DescribeRecommendationFeedbackRequest = {}  # type: ignore[typeddict-item]
    return out
