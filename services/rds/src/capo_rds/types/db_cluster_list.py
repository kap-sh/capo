"""Generated from Smithy shape ``com.amazonaws.rds#DBClusterList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.db_cluster

DBClusterList: TypeAlias = list["capo_rds.types.db_cluster.DBCluster"]


# --- awsQuery ser/de ---
def serialize_query(
    value: DBClusterList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_rds.types.db_cluster

    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        capo_rds.types.db_cluster.serialize_query(
            item, pairs, f"{prefix}.DBCluster.{n}"
        )


def deserialize_query(el: Element) -> DBClusterList:
    import capo_rds.types.db_cluster

    out: DBClusterList = []
    for child in el.findall("DBCluster"):
        out.append(capo_rds.types.db_cluster.deserialize_query(child))
    return out


def serialize_query_flat(
    value: DBClusterList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_rds.types.db_cluster

    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        capo_rds.types.db_cluster.serialize_query(item, pairs, f"{prefix}.{n}")


def deserialize_query_flat(parent: Element, tag: str) -> DBClusterList:
    import capo_rds.types.db_cluster

    out: DBClusterList = []
    for child in parent.findall(tag):
        out.append(capo_rds.types.db_cluster.deserialize_query(child))
    return out


def redact_sensitive(value: DBClusterList) -> list[Any]:
    import capo_rds.types.db_cluster

    return [capo_rds.types.db_cluster.redact_sensitive(item) for item in value]
