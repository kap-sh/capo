"""Generated from Smithy shape ``com.amazonaws.sagemaker#ListClusterOperationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.cluster_operation_summaries
    import capo_sagemaker.types.next_token


class ListClusterOperationsResponse(TypedDict, closed=True):
    next_token: NotRequired["capo_sagemaker.types.next_token.NextToken"]
    """<p>A token to retrieve the next set of results. Include this token in subsequent <code>ListClusterOperations</code> calls to fetch more operations.</p>"""
    cluster_operation_summaries: NotRequired[
        "capo_sagemaker.types.cluster_operation_summaries.ClusterOperationSummaries"
    ]
    """<p>A list of operation summaries matching the specified criteria.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListClusterOperationsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "cluster_operation_summaries" in value:
        import capo_sagemaker.types.cluster_operation_summaries

        out["ClusterOperationSummaries"] = (
            capo_sagemaker.types.cluster_operation_summaries.serialize_aws_json_1_1(
                value["cluster_operation_summaries"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListClusterOperationsResponse:
    out: ListClusterOperationsResponse = {}  # type: ignore[typeddict-item]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("ClusterOperationSummaries") is not None:
        import capo_sagemaker.types.cluster_operation_summaries

        out["cluster_operation_summaries"] = (
            capo_sagemaker.types.cluster_operation_summaries.deserialize_aws_json_1_1(
                data["ClusterOperationSummaries"]
            )
        )
    return out
