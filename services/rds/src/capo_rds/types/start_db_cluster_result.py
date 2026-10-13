"""Generated from Smithy shape ``com.amazonaws.rds#StartDBClusterResult``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.db_cluster


class StartDBClusterResult(TypedDict, closed=True):
    db_cluster: NotRequired["capo_rds.types.db_cluster.DBCluster"]


# --- awsQuery ser/de ---
def serialize_query(
    value: StartDBClusterResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "db_cluster" in value:
        import capo_rds.types.db_cluster

        capo_rds.types.db_cluster.serialize_query(
            value["db_cluster"], pairs, f"{key_prefix}DBCluster"
        )


def deserialize_query(el: Element) -> StartDBClusterResult:
    out: StartDBClusterResult = {}  # type: ignore[typeddict-item]
    child_db_cluster = el.find("DBCluster")
    if child_db_cluster is not None:
        import capo_rds.types.db_cluster

        out["db_cluster"] = capo_rds.types.db_cluster.deserialize_query(
            child_db_cluster
        )
    return out


def redact_sensitive(value: StartDBClusterResult) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "db_cluster" in value:
        import capo_rds.types.db_cluster

        out["db_cluster"] = capo_rds.types.db_cluster.redact_sensitive(
            value["db_cluster"]
        )
    return out
