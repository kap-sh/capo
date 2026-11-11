"""Generated from Smithy shape ``com.amazonaws.sagemaker#ListClusterExtensionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.cluster_arn
    import capo_sagemaker.types.max_results
    import capo_sagemaker.types.next_token
    import capo_sagemaker.types.timestamp


class ListClusterExtensionsRequest(TypedDict, closed=True):
    cluster_arn: NotRequired["capo_sagemaker.types.cluster_arn.ClusterArn"]
    """<p>The Amazon Resource Name (ARN) of the SageMaker HyperPod cluster whose extensions you want to list.</p>"""
    max_results: NotRequired["capo_sagemaker.types.max_results.MaxResults"]
    """<p>The maximum number of extensions to return in the response. If you don't specify a value, SageMaker HyperPod returns up to 100 extensions.</p>"""
    next_token: NotRequired["capo_sagemaker.types.next_token.NextToken"]
    """<p>If the result of the previous <code>ListClusterExtensions</code> request was truncated, the response includes a <code>NextToken</code>. To retrieve the next set of extensions, use the token in the next request. When you use the <code>CreationTimeAfter</code> or <code>CreationTimeBefore</code> filters, a response can contain fewer extensions than <code>MaxResults</code>, or none, and still include a <code>NextToken</code>. Continue until the response doesn't include a <code>NextToken</code>.</p>"""
    creation_time_after: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>A filter that returns extensions created at or after the specified time. Timestamps are formatted according to the ISO 8601 standard.</p>"""
    creation_time_before: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>A filter that returns extensions created at or before the specified time. The acceptable formats are the same as the timestamp formats for <code>CreationTimeAfter</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListClusterExtensionsRequest) -> dict:
    out: dict = {}
    if "cluster_arn" in value:
        out["ClusterArn"] = value["cluster_arn"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "creation_time_after" in value:
        import capo_sagemaker.types.timestamp

        out["CreationTimeAfter"] = (
            capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
                value["creation_time_after"]
            )
        )
    if "creation_time_before" in value:
        import capo_sagemaker.types.timestamp

        out["CreationTimeBefore"] = (
            capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
                value["creation_time_before"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListClusterExtensionsRequest:
    out: ListClusterExtensionsRequest = {}  # type: ignore[typeddict-item]
    if data.get("ClusterArn") is not None:
        out["cluster_arn"] = data["ClusterArn"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("CreationTimeAfter") is not None:
        import capo_sagemaker.types.timestamp

        out["creation_time_after"] = (
            capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["CreationTimeAfter"]
            )
        )
    if data.get("CreationTimeBefore") is not None:
        import capo_sagemaker.types.timestamp

        out["creation_time_before"] = (
            capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["CreationTimeBefore"]
            )
        )
    return out
