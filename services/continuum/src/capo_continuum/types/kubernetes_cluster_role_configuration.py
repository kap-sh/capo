"""Generated from Smithy shape ``com.amazonaws.continuum#KubernetesClusterRoleConfiguration``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_continuum.types.kubernetes_cluster_external_id
    import capo_continuum.types.kubernetes_cluster_role_arn


class KubernetesClusterRoleConfiguration(TypedDict, closed=True):
    role_arn: (
        "capo_continuum.types.kubernetes_cluster_role_arn.KubernetesClusterRoleArn"
    )
    """IAM role the authenticated caller passes to Continuum."""
    external_id: NotRequired[
        "capo_continuum.types.kubernetes_cluster_external_id.KubernetesClusterExternalId"
    ]
    """Optional external ID Continuum supplies when assuming roleArn. This must match the role trust policy when configured and does not replace the caller's iam:PassRole permission."""


# --- restJson1 ser/de ---
def serialize_json(value: KubernetesClusterRoleConfiguration) -> dict:
    out: dict = {}
    out["roleArn"] = value["role_arn"]
    if "external_id" in value:
        out["externalId"] = value["external_id"]
    return out


def deserialize_json(data: dict) -> KubernetesClusterRoleConfiguration:
    out: KubernetesClusterRoleConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("roleArn") is not None:
        out["role_arn"] = data["roleArn"]
    else:
        out["role_arn"] = ""
    if data.get("externalId") is not None:
        out["external_id"] = data["externalId"]
    return out


def redact_sensitive(value: KubernetesClusterRoleConfiguration) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "external_id" in value:
        out["external_id"] = "*** Sensitive Data Redacted ***"
    return out
