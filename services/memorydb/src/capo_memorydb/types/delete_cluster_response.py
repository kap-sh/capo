"""Generated from Smithy shape ``com.amazonaws.memorydb#DeleteClusterResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_memorydb.types.cluster


class DeleteClusterResponse(TypedDict, closed=True):
    cluster: NotRequired["capo_memorydb.types.cluster.Cluster"]
    """<p>The cluster object that has been deleted.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteClusterResponse) -> dict:
    out: dict = {}
    if "cluster" in value:
        import capo_memorydb.types.cluster

        out["Cluster"] = capo_memorydb.types.cluster.serialize_aws_json_1_1(
            value["cluster"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteClusterResponse:
    out: DeleteClusterResponse = {}  # type: ignore[typeddict-item]
    if data.get("Cluster") is not None:
        import capo_memorydb.types.cluster

        out["cluster"] = capo_memorydb.types.cluster.deserialize_aws_json_1_1(
            data["Cluster"]
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DeleteClusterResponse) -> dict:
    out: dict = {}
    if "cluster" in value:
        import capo_memorydb.types.cluster

        out["Cluster"] = capo_memorydb.types.cluster.serialize_cbor(value["cluster"])
    return out


def deserialize_cbor(data: dict) -> DeleteClusterResponse:
    out: DeleteClusterResponse = {}  # type: ignore[typeddict-item]
    if data.get("Cluster") is not None:
        import capo_memorydb.types.cluster

        out["cluster"] = capo_memorydb.types.cluster.deserialize_cbor(data["Cluster"])
    return out
