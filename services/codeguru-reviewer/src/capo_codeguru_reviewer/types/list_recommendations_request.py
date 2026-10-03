"""Generated from Smithy shape ``com.amazonaws.codegurureviewer#ListRecommendationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codeguru_reviewer.types.arn
    import capo_codeguru_reviewer.types.list_recommendations_max_results
    import capo_codeguru_reviewer.types.next_token


class ListRecommendationsRequest(TypedDict, closed=True):
    next_token: NotRequired["capo_codeguru_reviewer.types.next_token.NextToken"]
    """<p>Pagination token.</p>"""
    max_results: NotRequired[
        "capo_codeguru_reviewer.types.list_recommendations_max_results.ListRecommendationsMaxResults"
    ]
    """<p>The maximum number of results that are returned per call. The default is 100.</p>"""
    code_review_arn: "capo_codeguru_reviewer.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the <a href="https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_CodeReview.html">CodeReview</a> object. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListRecommendationsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListRecommendationsRequest:
    out: ListRecommendationsRequest = {}  # type: ignore[typeddict-item]
    return out
