"""Generated from Smithy shape ``com.amazonaws.sagemaker#ListClusterExtensionVersionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.extension_name
    import capo_sagemaker.types.max_results
    import capo_sagemaker.types.next_token


class ListClusterExtensionVersionsRequest(TypedDict, closed=True):
    extension_name: NotRequired["capo_sagemaker.types.extension_name.ExtensionName"]
    """<p>The name of the extension whose versions you want to list, for example <code>sagemaker-observability</code>.</p>"""
    max_results: NotRequired["capo_sagemaker.types.max_results.MaxResults"]
    """<p>The maximum number of versions to return in the response. If you don't specify a value, SageMaker HyperPod returns up to 100 versions.</p>"""
    next_token: NotRequired["capo_sagemaker.types.next_token.NextToken"]
    """<p>If the result of the previous <code>ListClusterExtensionVersions</code> request was truncated, the response includes a <code>NextToken</code>. To retrieve the next set of versions, use the token in the next request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListClusterExtensionVersionsRequest) -> dict:
    out: dict = {}
    if "extension_name" in value:
        out["ExtensionName"] = value["extension_name"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListClusterExtensionVersionsRequest:
    out: ListClusterExtensionVersionsRequest = {}  # type: ignore[typeddict-item]
    if data.get("ExtensionName") is not None:
        out["extension_name"] = data["ExtensionName"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
