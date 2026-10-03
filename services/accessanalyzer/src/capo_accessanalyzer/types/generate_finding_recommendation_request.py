"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#GenerateFindingRecommendationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_accessanalyzer.types.analyzer_arn


class GenerateFindingRecommendationRequest(TypedDict, closed=True):
    analyzer_arn: "capo_accessanalyzer.types.analyzer_arn.AnalyzerArn"
    """<p>The <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-getting-started.html#permission-resources">ARN of the analyzer</a> used to generate the finding recommendation.</p>"""
    id: "str"
    """<p>The unique ID for the finding recommendation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GenerateFindingRecommendationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GenerateFindingRecommendationRequest:
    out: GenerateFindingRecommendationRequest = {}  # type: ignore[typeddict-item]
    return out
