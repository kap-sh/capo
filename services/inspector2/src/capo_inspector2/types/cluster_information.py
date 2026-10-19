"""Generated from Smithy shape ``com.amazonaws.inspector2#ClusterInformation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_inspector2.types.cluster_details_list


class ClusterInformation(TypedDict, closed=True):
    cluster_arn: "str"
    """<p>The cluster ARN.</p>"""
    cluster_details: NotRequired[
        "capo_inspector2.types.cluster_details_list.ClusterDetailsList"
    ]
    """<p>Details about the cluster.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ClusterInformation) -> dict:
    out: dict = {}
    out["clusterArn"] = value["cluster_arn"]
    if "cluster_details" in value:
        import capo_inspector2.types.cluster_details_list

        out["clusterDetails"] = (
            capo_inspector2.types.cluster_details_list.serialize_json(
                value["cluster_details"]
            )
        )
    return out


def deserialize_json(data: dict) -> ClusterInformation:
    out: ClusterInformation = {}  # type: ignore[typeddict-item]
    if data.get("clusterArn") is not None:
        out["cluster_arn"] = data["clusterArn"]
    else:
        out["cluster_arn"] = ""
    if data.get("clusterDetails") is not None:
        import capo_inspector2.types.cluster_details_list

        out["cluster_details"] = (
            capo_inspector2.types.cluster_details_list.deserialize_json(
                data["clusterDetails"]
            )
        )
    return out
