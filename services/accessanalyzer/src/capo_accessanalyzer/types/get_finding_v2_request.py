"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#GetFindingV2Request``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_accessanalyzer.types.analyzer_arn
    import capo_accessanalyzer.types.finding_id
    import capo_accessanalyzer.types.token


class GetFindingV2Request(TypedDict, closed=True):
    analyzer_arn: "capo_accessanalyzer.types.analyzer_arn.AnalyzerArn"
    """<p>The <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-getting-started.html#permission-resources">ARN of the analyzer</a> that generated the finding.</p>"""
    id: "capo_accessanalyzer.types.finding_id.FindingId"
    """<p>The ID of the finding to retrieve.</p>"""
    max_results: NotRequired["int"]
    """<p>The maximum number of results to return in the response.</p>"""
    next_token: NotRequired["capo_accessanalyzer.types.token.Token"]
    """<p>A token used for pagination of results returned.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetFindingV2Request) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetFindingV2Request:
    out: GetFindingV2Request = {}  # type: ignore[typeddict-item]
    return out
