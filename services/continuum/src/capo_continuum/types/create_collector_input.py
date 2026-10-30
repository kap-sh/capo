"""Generated from Smithy shape ``com.amazonaws.continuum#CreateCollectorInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_continuum.types.collector_client_token
    import capo_continuum.types.collector_type
    import capo_continuum.types.kubernetes_cluster_role_configuration


class CreateCollectorInput(TypedDict, closed=True):
    type: NotRequired["capo_continuum.types.collector_type.CollectorType"]
    """Source to collect. Defaults to AWS_COLLECTOR when omitted."""
    kubernetes_cluster_role: NotRequired[
        "capo_continuum.types.kubernetes_cluster_role_configuration.KubernetesClusterRoleConfiguration"
    ]
    """IAM role configuration used to collect Kubernetes cluster metadata. The authenticated caller must be allowed to pass its exact roleArn to Continuum."""
    client_token: NotRequired[
        "capo_continuum.types.collector_client_token.CollectorClientToken"
    ]
    """Caller-provided token that makes retried create requests return the original Collector rather than creating a duplicate."""


# --- restJson1 ser/de ---
def serialize_json(value: CreateCollectorInput) -> dict:
    out: dict = {}
    if "type" in value:
        import capo_continuum.types.collector_type

        out["type"] = capo_continuum.types.collector_type.serialize_json(value["type"])
    if "kubernetes_cluster_role" in value:
        import capo_continuum.types.kubernetes_cluster_role_configuration

        out["k8ClusterRole"] = (
            capo_continuum.types.kubernetes_cluster_role_configuration.serialize_json(
                value["kubernetes_cluster_role"]
            )
        )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> CreateCollectorInput:
    out: CreateCollectorInput = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        import capo_continuum.types.collector_type

        out["type"] = capo_continuum.types.collector_type.deserialize_json(data["type"])
    if data.get("k8ClusterRole") is not None:
        import capo_continuum.types.kubernetes_cluster_role_configuration

        out["kubernetes_cluster_role"] = (
            capo_continuum.types.kubernetes_cluster_role_configuration.deserialize_json(
                data["k8ClusterRole"]
            )
        )
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out


def redact_sensitive(value: CreateCollectorInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "kubernetes_cluster_role" in value:
        import capo_continuum.types.kubernetes_cluster_role_configuration

        out["kubernetes_cluster_role"] = (
            capo_continuum.types.kubernetes_cluster_role_configuration.redact_sensitive(
                value["kubernetes_cluster_role"]
            )
        )
    return out
