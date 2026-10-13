"""Generated from Smithy shape ``com.amazonaws.redshift#ClusterList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.cluster

ClusterList: TypeAlias = list["capo_redshift.types.cluster.Cluster"]


# --- awsQuery ser/de ---
def serialize_query(
    value: ClusterList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_redshift.types.cluster

    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        capo_redshift.types.cluster.serialize_query(
            item, pairs, f"{prefix}.Cluster.{n}"
        )


def deserialize_query(el: Element) -> ClusterList:
    import capo_redshift.types.cluster

    out: ClusterList = []
    for child in el.findall("Cluster"):
        out.append(capo_redshift.types.cluster.deserialize_query(child))
    return out


def serialize_query_flat(
    value: ClusterList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_redshift.types.cluster

    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        capo_redshift.types.cluster.serialize_query(item, pairs, f"{prefix}.{n}")


def deserialize_query_flat(parent: Element, tag: str) -> ClusterList:
    import capo_redshift.types.cluster

    out: ClusterList = []
    for child in parent.findall(tag):
        out.append(capo_redshift.types.cluster.deserialize_query(child))
    return out


def redact_sensitive(value: ClusterList) -> list[Any]:
    import capo_redshift.types.cluster

    return [capo_redshift.types.cluster.redact_sensitive(item) for item in value]
