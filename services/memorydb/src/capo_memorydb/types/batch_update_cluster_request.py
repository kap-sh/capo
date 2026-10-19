"""Generated from Smithy shape ``com.amazonaws.memorydb#BatchUpdateClusterRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_memorydb.types.cluster_name_list
    import capo_memorydb.types.service_update_request


class BatchUpdateClusterRequest(TypedDict, closed=True):
    cluster_names: "capo_memorydb.types.cluster_name_list.ClusterNameList"
    """<p>The cluster names to apply the updates.</p>"""
    service_update: NotRequired[
        "capo_memorydb.types.service_update_request.ServiceUpdateRequest"
    ]
    """<p>The unique ID of the service update</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchUpdateClusterRequest) -> dict:
    out: dict = {}
    import capo_memorydb.types.cluster_name_list

    out["ClusterNames"] = capo_memorydb.types.cluster_name_list.serialize_aws_json_1_1(
        value["cluster_names"]
    )
    if "service_update" in value:
        import capo_memorydb.types.service_update_request

        out["ServiceUpdate"] = (
            capo_memorydb.types.service_update_request.serialize_aws_json_1_1(
                value["service_update"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchUpdateClusterRequest:
    out: BatchUpdateClusterRequest = {}  # type: ignore[typeddict-item]
    if data.get("ClusterNames") is not None:
        import capo_memorydb.types.cluster_name_list

        out["cluster_names"] = (
            capo_memorydb.types.cluster_name_list.deserialize_aws_json_1_1(
                data["ClusterNames"]
            )
        )
    else:
        out["cluster_names"] = []
    if data.get("ServiceUpdate") is not None:
        import capo_memorydb.types.service_update_request

        out["service_update"] = (
            capo_memorydb.types.service_update_request.deserialize_aws_json_1_1(
                data["ServiceUpdate"]
            )
        )
    return out
