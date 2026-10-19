"""Generated from Smithy shape ``com.amazonaws.inspector2#GetClustersForImageResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_inspector2.types.cluster_information_list
    import capo_inspector2.types.get_clusters_for_image_next_token


class GetClustersForImageResponse(TypedDict, closed=True):
    cluster: "capo_inspector2.types.cluster_information_list.ClusterInformationList"
    """<p>A unit of work inside of a cluster, which can include metadata about the cluster.</p>"""
    next_token: NotRequired[
        "capo_inspector2.types.get_clusters_for_image_next_token.GetClustersForImageNextToken"
    ]
    """<p>The pagination token from a previous request used to retrieve the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetClustersForImageResponse) -> dict:
    out: dict = {}
    import capo_inspector2.types.cluster_information_list

    out["cluster"] = capo_inspector2.types.cluster_information_list.serialize_json(
        value["cluster"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> GetClustersForImageResponse:
    out: GetClustersForImageResponse = {}  # type: ignore[typeddict-item]
    if data.get("cluster") is not None:
        import capo_inspector2.types.cluster_information_list

        out["cluster"] = (
            capo_inspector2.types.cluster_information_list.deserialize_json(
                data["cluster"]
            )
        )
    else:
        out["cluster"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
