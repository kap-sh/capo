"""Generated from Smithy shape ``com.amazonaws.rds#DBClusterMessage``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.db_cluster_list
    import capo_rds.types.string


class DBClusterMessage(TypedDict, closed=True):
    marker: NotRequired["capo_rds.types.string.String"]
    """<p>A pagination token that can be used in a later <code>DescribeDBClusters</code> request.</p>"""
    db_clusters: NotRequired["capo_rds.types.db_cluster_list.DBClusterList"]
    """<p>Contains a list of DB clusters for the user.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DBClusterMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "marker" in value:
        pairs.append((f"{key_prefix}Marker", str(value["marker"])))
    if "db_clusters" in value:
        import capo_rds.types.db_cluster_list

        capo_rds.types.db_cluster_list.serialize_query(
            value["db_clusters"], pairs, f"{key_prefix}DBClusters"
        )


def deserialize_query(el: Element) -> DBClusterMessage:
    out: DBClusterMessage = {}  # type: ignore[typeddict-item]
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    child_db_clusters = el.find("DBClusters")
    if child_db_clusters is not None:
        import capo_rds.types.db_cluster_list

        out["db_clusters"] = capo_rds.types.db_cluster_list.deserialize_query(
            child_db_clusters
        )
    return out


def redact_sensitive(value: DBClusterMessage) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "db_clusters" in value:
        import capo_rds.types.db_cluster_list

        out["db_clusters"] = capo_rds.types.db_cluster_list.redact_sensitive(
            value["db_clusters"]
        )
    return out
