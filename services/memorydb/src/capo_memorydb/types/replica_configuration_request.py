"""Generated from Smithy shape ``com.amazonaws.memorydb#ReplicaConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_memorydb.types.integer


class ReplicaConfigurationRequest(TypedDict, closed=True):
    replica_count: "capo_memorydb.types.integer.Integer"
    """<p>The number of replicas to scale up or down to</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReplicaConfigurationRequest) -> dict:
    out: dict = {}
    out["ReplicaCount"] = value.get("replica_count", 0)
    return out


def deserialize_aws_json_1_1(data: dict) -> ReplicaConfigurationRequest:
    out: ReplicaConfigurationRequest = {}  # type: ignore[typeddict-item]
    if data.get("ReplicaCount") is not None:
        out["replica_count"] = data["ReplicaCount"]
    else:
        out["replica_count"] = 0
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ReplicaConfigurationRequest) -> dict:
    out: dict = {}
    out["ReplicaCount"] = value.get("replica_count", 0)
    return out


def deserialize_cbor(data: dict) -> ReplicaConfigurationRequest:
    out: ReplicaConfigurationRequest = {}  # type: ignore[typeddict-item]
    if data.get("ReplicaCount") is not None:
        out["replica_count"] = data["ReplicaCount"]
    else:
        out["replica_count"] = 0
    return out
