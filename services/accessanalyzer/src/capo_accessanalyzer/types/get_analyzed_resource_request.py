"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#GetAnalyzedResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_accessanalyzer.types.analyzer_arn
    import capo_accessanalyzer.types.resource_arn


class GetAnalyzedResourceRequest(TypedDict, closed=True):
    analyzer_arn: "capo_accessanalyzer.types.analyzer_arn.AnalyzerArn"
    """<p>The <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-getting-started.html#permission-resources">ARN of the analyzer</a> to retrieve information from.</p>"""
    resource_arn: "capo_accessanalyzer.types.resource_arn.ResourceArn"
    """<p>The ARN of the resource to retrieve information about.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAnalyzedResourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetAnalyzedResourceRequest:
    out: GetAnalyzedResourceRequest = {}  # type: ignore[typeddict-item]
    return out
