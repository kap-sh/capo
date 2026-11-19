"""Generated from Smithy shape ``com.amazonaws.cloudhsmv2#ModifyClusterResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudhsm_v2.types.cluster


class ModifyClusterResponse(TypedDict, closed=True):
    cluster: NotRequired["capo_cloudhsm_v2.types.cluster.Cluster"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ModifyClusterResponse) -> dict:
    out: dict = {}
    if "cluster" in value:
        import capo_cloudhsm_v2.types.cluster

        out["Cluster"] = capo_cloudhsm_v2.types.cluster.serialize_aws_json_1_1(
            value["cluster"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ModifyClusterResponse:
    out: ModifyClusterResponse = {}  # type: ignore[typeddict-item]
    if data.get("Cluster") is not None:
        import capo_cloudhsm_v2.types.cluster

        out["cluster"] = capo_cloudhsm_v2.types.cluster.deserialize_aws_json_1_1(
            data["Cluster"]
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ModifyClusterResponse) -> dict:
    out: dict = {}
    if "cluster" in value:
        import capo_cloudhsm_v2.types.cluster

        out["Cluster"] = capo_cloudhsm_v2.types.cluster.serialize_cbor(value["cluster"])
    return out


def deserialize_cbor(data: dict) -> ModifyClusterResponse:
    out: ModifyClusterResponse = {}  # type: ignore[typeddict-item]
    if data.get("Cluster") is not None:
        import capo_cloudhsm_v2.types.cluster

        out["cluster"] = capo_cloudhsm_v2.types.cluster.deserialize_cbor(
            data["Cluster"]
        )
    return out
