"""Generated from Smithy shape ``com.amazonaws.redshift#ModifyClusterMaintenanceResult``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.cluster


class ModifyClusterMaintenanceResult(TypedDict, closed=True):
    cluster: NotRequired["capo_redshift.types.cluster.Cluster"]


# --- awsQuery ser/de ---
def serialize_query(
    value: ModifyClusterMaintenanceResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "cluster" in value:
        import capo_redshift.types.cluster

        capo_redshift.types.cluster.serialize_query(
            value["cluster"], pairs, f"{key_prefix}Cluster"
        )


def deserialize_query(el: Element) -> ModifyClusterMaintenanceResult:
    out: ModifyClusterMaintenanceResult = {}  # type: ignore[typeddict-item]
    child_cluster = el.find("Cluster")
    if child_cluster is not None:
        import capo_redshift.types.cluster

        out["cluster"] = capo_redshift.types.cluster.deserialize_query(child_cluster)
    return out


def redact_sensitive(value: ModifyClusterMaintenanceResult) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "cluster" in value:
        import capo_redshift.types.cluster

        out["cluster"] = capo_redshift.types.cluster.redact_sensitive(value["cluster"])
    return out
