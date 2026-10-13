"""Generated from Smithy shape ``com.amazonaws.redshift#ClustersMessage``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.cluster_list
    import capo_redshift.types.string


class ClustersMessage(TypedDict, closed=True):
    marker: NotRequired["capo_redshift.types.string.String"]
    """<p>A value that indicates the starting point for the next set of response records in a subsequent request. If a value is returned in a response, you can retrieve the next set of records by providing this returned marker value in the <code>Marker</code> parameter and retrying the command. If the <code>Marker</code> field is empty, all response records have been retrieved for the request. </p>"""
    clusters: NotRequired["capo_redshift.types.cluster_list.ClusterList"]
    """<p>A list of <code>Cluster</code> objects, where each object describes one cluster. </p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ClustersMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "marker" in value:
        pairs.append((f"{key_prefix}Marker", str(value["marker"])))
    if "clusters" in value:
        import capo_redshift.types.cluster_list

        capo_redshift.types.cluster_list.serialize_query(
            value["clusters"], pairs, f"{key_prefix}Clusters"
        )


def deserialize_query(el: Element) -> ClustersMessage:
    out: ClustersMessage = {}  # type: ignore[typeddict-item]
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    child_clusters = el.find("Clusters")
    if child_clusters is not None:
        import capo_redshift.types.cluster_list

        out["clusters"] = capo_redshift.types.cluster_list.deserialize_query(
            child_clusters
        )
    return out


def redact_sensitive(value: ClustersMessage) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "clusters" in value:
        import capo_redshift.types.cluster_list

        out["clusters"] = capo_redshift.types.cluster_list.redact_sensitive(
            value["clusters"]
        )
    return out
