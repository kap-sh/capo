"""Generated from Smithy shape ``com.amazonaws.memorydb#UnprocessedCluster``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_memorydb.types.string


class UnprocessedCluster(TypedDict, closed=True):
    cluster_name: NotRequired["capo_memorydb.types.string.String"]
    """<p>The name of the cluster</p>"""
    error_type: NotRequired["capo_memorydb.types.string.String"]
    """<p>The error type associated with the update failure</p>"""
    error_message: NotRequired["capo_memorydb.types.string.String"]
    """<p>The error message associated with the update failure</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UnprocessedCluster) -> dict:
    out: dict = {}
    if "cluster_name" in value:
        out["ClusterName"] = value["cluster_name"]
    if "error_type" in value:
        out["ErrorType"] = value["error_type"]
    if "error_message" in value:
        out["ErrorMessage"] = value["error_message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UnprocessedCluster:
    out: UnprocessedCluster = {}  # type: ignore[typeddict-item]
    if data.get("ClusterName") is not None:
        out["cluster_name"] = data["ClusterName"]
    if data.get("ErrorType") is not None:
        out["error_type"] = data["ErrorType"]
    if data.get("ErrorMessage") is not None:
        out["error_message"] = data["ErrorMessage"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: UnprocessedCluster) -> dict:
    out: dict = {}
    if "cluster_name" in value:
        out["ClusterName"] = value["cluster_name"]
    if "error_type" in value:
        out["ErrorType"] = value["error_type"]
    if "error_message" in value:
        out["ErrorMessage"] = value["error_message"]
    return out


def deserialize_cbor(data: dict) -> UnprocessedCluster:
    out: UnprocessedCluster = {}  # type: ignore[typeddict-item]
    if data.get("ClusterName") is not None:
        out["cluster_name"] = data["ClusterName"]
    if data.get("ErrorType") is not None:
        out["error_type"] = data["ErrorType"]
    if data.get("ErrorMessage") is not None:
        out["error_message"] = data["ErrorMessage"]
    return out
