"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#ListAnalyzedResourcesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_accessanalyzer.errors import DeserializationError

if TYPE_CHECKING:
    import capo_accessanalyzer.types.analyzer_arn
    import capo_accessanalyzer.types.resource_type
    import capo_accessanalyzer.types.token


class ListAnalyzedResourcesRequest(TypedDict, closed=True):
    analyzer_arn: "capo_accessanalyzer.types.analyzer_arn.AnalyzerArn"
    """<p>The <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-getting-started.html#permission-resources">ARN of the analyzer</a> to retrieve a list of analyzed resources from.</p>"""
    resource_type: NotRequired["capo_accessanalyzer.types.resource_type.ResourceType"]
    """<p>The type of resource.</p>"""
    next_token: NotRequired["capo_accessanalyzer.types.token.Token"]
    """<p>A token used for pagination of results returned.</p>"""
    max_results: NotRequired["int"]
    """<p>The maximum number of results to return in the response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAnalyzedResourcesRequest) -> dict:
    out: dict = {}
    out["analyzerArn"] = value["analyzer_arn"]
    if "resource_type" in value:
        out["resourceType"] = value["resource_type"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    return out


def deserialize_json(data: dict) -> ListAnalyzedResourcesRequest:
    out: ListAnalyzedResourcesRequest = {}  # type: ignore[typeddict-item]
    if data.get("analyzerArn") is not None:
        out["analyzer_arn"] = data["analyzerArn"]
    else:
        raise DeserializationError("ListAnalyzedResourcesRequest.analyzer_arn required")
    if data.get("resourceType") is not None:
        out["resource_type"] = data["resourceType"]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    return out
