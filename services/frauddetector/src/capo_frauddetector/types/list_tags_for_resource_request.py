"""Generated from Smithy shape ``com.amazonaws.frauddetector#ListTagsForResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_frauddetector.types.fraud_detector_arn
    import capo_frauddetector.types.string
    import capo_frauddetector.types.tags_max_results


class ListTagsForResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_frauddetector.types.fraud_detector_arn.fraudDetectorArn"
    """<p>The ARN that specifies the resource whose tags you want to list.</p>"""
    next_token: NotRequired["capo_frauddetector.types.string.string"]
    """<p>The next token from the previous results.</p>"""
    max_results: NotRequired["capo_frauddetector.types.tags_max_results.TagsMaxResults"]
    """<p>The maximum number of objects to return for the request. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListTagsForResourceRequest) -> dict:
    out: dict = {}
    out["resourceARN"] = value["resource_arn"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListTagsForResourceRequest:
    out: ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("resourceARN") is not None:
        out["resource_arn"] = data["resourceARN"]
    else:
        out["resource_arn"] = ""
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    return out
