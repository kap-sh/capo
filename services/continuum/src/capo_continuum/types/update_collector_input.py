"""Generated from Smithy shape ``com.amazonaws.continuum#UpdateCollectorInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_continuum.types.collector_id
    import capo_continuum.types.collector_name
    import capo_continuum.types.kubernetes_cluster_role_update


class UpdateCollectorInput(TypedDict, closed=True):
    collector_id: "capo_continuum.types.collector_id.CollectorId"
    """The unique identifier of the Collector to update."""
    name: NotRequired["capo_continuum.types.collector_name.CollectorName"]
    """The new customer-visible name."""
    kubernetes_cluster_role: NotRequired[
        "capo_continuum.types.kubernetes_cluster_role_update.KubernetesClusterRoleUpdate"
    ]
    """Atomic update to the IAM role configuration used to collect Kubernetes cluster metadata. The set variant requires a complete configuration; the authenticated caller must be allowed to pass its exact roleArn to Continuum. The remove variant clears both the role and external ID."""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateCollectorInput) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "kubernetes_cluster_role" in value:
        import capo_continuum.types.kubernetes_cluster_role_update

        out["k8ClusterRole"] = (
            capo_continuum.types.kubernetes_cluster_role_update.serialize_json(
                value["kubernetes_cluster_role"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateCollectorInput:
    out: UpdateCollectorInput = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("k8ClusterRole") is not None:
        import capo_continuum.types.kubernetes_cluster_role_update

        out["kubernetes_cluster_role"] = (
            capo_continuum.types.kubernetes_cluster_role_update.deserialize_json(
                data["k8ClusterRole"]
            )
        )
    return out


def redact_sensitive(value: UpdateCollectorInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "kubernetes_cluster_role" in value:
        import capo_continuum.types.kubernetes_cluster_role_update

        out["kubernetes_cluster_role"] = (
            capo_continuum.types.kubernetes_cluster_role_update.redact_sensitive(
                value["kubernetes_cluster_role"]
            )
        )
    return out
