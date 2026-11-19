"""Generated from Smithy shape ``com.amazonaws.memorydb#BatchUpdateClusterResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_memorydb.types.cluster_list
    import capo_memorydb.types.unprocessed_cluster_list


class BatchUpdateClusterResponse(TypedDict, closed=True):
    processed_clusters: NotRequired["capo_memorydb.types.cluster_list.ClusterList"]
    """<p>The list of clusters that have been updated.</p>"""
    unprocessed_clusters: NotRequired[
        "capo_memorydb.types.unprocessed_cluster_list.UnprocessedClusterList"
    ]
    """<p>The list of clusters where updates have not been applied.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchUpdateClusterResponse) -> dict:
    out: dict = {}
    if "processed_clusters" in value:
        import capo_memorydb.types.cluster_list

        out["ProcessedClusters"] = (
            capo_memorydb.types.cluster_list.serialize_aws_json_1_1(
                value["processed_clusters"]
            )
        )
    if "unprocessed_clusters" in value:
        import capo_memorydb.types.unprocessed_cluster_list

        out["UnprocessedClusters"] = (
            capo_memorydb.types.unprocessed_cluster_list.serialize_aws_json_1_1(
                value["unprocessed_clusters"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchUpdateClusterResponse:
    out: BatchUpdateClusterResponse = {}  # type: ignore[typeddict-item]
    if data.get("ProcessedClusters") is not None:
        import capo_memorydb.types.cluster_list

        out["processed_clusters"] = (
            capo_memorydb.types.cluster_list.deserialize_aws_json_1_1(
                data["ProcessedClusters"]
            )
        )
    if data.get("UnprocessedClusters") is not None:
        import capo_memorydb.types.unprocessed_cluster_list

        out["unprocessed_clusters"] = (
            capo_memorydb.types.unprocessed_cluster_list.deserialize_aws_json_1_1(
                data["UnprocessedClusters"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: BatchUpdateClusterResponse) -> dict:
    out: dict = {}
    if "processed_clusters" in value:
        import capo_memorydb.types.cluster_list

        out["ProcessedClusters"] = capo_memorydb.types.cluster_list.serialize_cbor(
            value["processed_clusters"]
        )
    if "unprocessed_clusters" in value:
        import capo_memorydb.types.unprocessed_cluster_list

        out["UnprocessedClusters"] = (
            capo_memorydb.types.unprocessed_cluster_list.serialize_cbor(
                value["unprocessed_clusters"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> BatchUpdateClusterResponse:
    out: BatchUpdateClusterResponse = {}  # type: ignore[typeddict-item]
    if data.get("ProcessedClusters") is not None:
        import capo_memorydb.types.cluster_list

        out["processed_clusters"] = capo_memorydb.types.cluster_list.deserialize_cbor(
            data["ProcessedClusters"]
        )
    if data.get("UnprocessedClusters") is not None:
        import capo_memorydb.types.unprocessed_cluster_list

        out["unprocessed_clusters"] = (
            capo_memorydb.types.unprocessed_cluster_list.deserialize_cbor(
                data["UnprocessedClusters"]
            )
        )
    return out
