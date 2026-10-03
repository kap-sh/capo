"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#GetFindingRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_accessanalyzer.types.analyzer_arn
    import capo_accessanalyzer.types.finding_id


class GetFindingRequest(TypedDict, closed=True):
    analyzer_arn: "capo_accessanalyzer.types.analyzer_arn.AnalyzerArn"
    """<p>The <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-getting-started.html#permission-resources">ARN of the analyzer</a> that generated the finding.</p>"""
    id: "capo_accessanalyzer.types.finding_id.FindingId"
    """<p>The ID of the finding to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetFindingRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetFindingRequest:
    out: GetFindingRequest = {}  # type: ignore[typeddict-item]
    return out
