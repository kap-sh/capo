"""Generated from Smithy shape ``com.amazonaws.memorydb#UpdateMultiRegionClusterResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_memorydb.types.multi_region_cluster


class UpdateMultiRegionClusterResponse(TypedDict, closed=True):
    multi_region_cluster: NotRequired[
        "capo_memorydb.types.multi_region_cluster.MultiRegionCluster"
    ]
    """<p>The status of updating the multi-Region cluster.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateMultiRegionClusterResponse) -> dict:
    out: dict = {}
    if "multi_region_cluster" in value:
        import capo_memorydb.types.multi_region_cluster

        out["MultiRegionCluster"] = (
            capo_memorydb.types.multi_region_cluster.serialize_aws_json_1_1(
                value["multi_region_cluster"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateMultiRegionClusterResponse:
    out: UpdateMultiRegionClusterResponse = {}  # type: ignore[typeddict-item]
    if data.get("MultiRegionCluster") is not None:
        import capo_memorydb.types.multi_region_cluster

        out["multi_region_cluster"] = (
            capo_memorydb.types.multi_region_cluster.deserialize_aws_json_1_1(
                data["MultiRegionCluster"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: UpdateMultiRegionClusterResponse) -> dict:
    out: dict = {}
    if "multi_region_cluster" in value:
        import capo_memorydb.types.multi_region_cluster

        out["MultiRegionCluster"] = (
            capo_memorydb.types.multi_region_cluster.serialize_cbor(
                value["multi_region_cluster"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> UpdateMultiRegionClusterResponse:
    out: UpdateMultiRegionClusterResponse = {}  # type: ignore[typeddict-item]
    if data.get("MultiRegionCluster") is not None:
        import capo_memorydb.types.multi_region_cluster

        out["multi_region_cluster"] = (
            capo_memorydb.types.multi_region_cluster.deserialize_cbor(
                data["MultiRegionCluster"]
            )
        )
    return out
