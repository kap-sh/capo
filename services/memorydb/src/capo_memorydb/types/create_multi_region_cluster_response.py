"""Generated from Smithy shape ``com.amazonaws.memorydb#CreateMultiRegionClusterResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_memorydb.types.multi_region_cluster


class CreateMultiRegionClusterResponse(TypedDict, closed=True):
    multi_region_cluster: NotRequired[
        "capo_memorydb.types.multi_region_cluster.MultiRegionCluster"
    ]
    """<p>Details about the newly created multi-Region cluster.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateMultiRegionClusterResponse) -> dict:
    out: dict = {}
    if "multi_region_cluster" in value:
        import capo_memorydb.types.multi_region_cluster

        out["MultiRegionCluster"] = (
            capo_memorydb.types.multi_region_cluster.serialize_aws_json_1_1(
                value["multi_region_cluster"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateMultiRegionClusterResponse:
    out: CreateMultiRegionClusterResponse = {}  # type: ignore[typeddict-item]
    if data.get("MultiRegionCluster") is not None:
        import capo_memorydb.types.multi_region_cluster

        out["multi_region_cluster"] = (
            capo_memorydb.types.multi_region_cluster.deserialize_aws_json_1_1(
                data["MultiRegionCluster"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CreateMultiRegionClusterResponse) -> dict:
    out: dict = {}
    if "multi_region_cluster" in value:
        import capo_memorydb.types.multi_region_cluster

        out["MultiRegionCluster"] = (
            capo_memorydb.types.multi_region_cluster.serialize_cbor(
                value["multi_region_cluster"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> CreateMultiRegionClusterResponse:
    out: CreateMultiRegionClusterResponse = {}  # type: ignore[typeddict-item]
    if data.get("MultiRegionCluster") is not None:
        import capo_memorydb.types.multi_region_cluster

        out["multi_region_cluster"] = (
            capo_memorydb.types.multi_region_cluster.deserialize_cbor(
                data["MultiRegionCluster"]
            )
        )
    return out
