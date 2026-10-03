"""Generated from Smithy shape ``com.amazonaws.codegurureviewer#DescribeCodeReviewRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_codeguru_reviewer.types.arn


class DescribeCodeReviewRequest(TypedDict, closed=True):
    code_review_arn: "capo_codeguru_reviewer.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the <a href="https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_CodeReview.html">CodeReview</a> object. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeCodeReviewRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeCodeReviewRequest:
    out: DescribeCodeReviewRequest = {}  # type: ignore[typeddict-item]
    return out
