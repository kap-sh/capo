"""Generated from Smithy shape ``com.amazonaws.continuum#KubernetesClusterRoleUpdate``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_continuum.errors import DeserializationError, SerializationError
from capo_continuum.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_continuum.types.kubernetes_cluster_role_configuration
    import capo_continuum.types.remove_kubernetes_cluster_role


class KubernetesClusterRoleUpdateSetMember(TypedDict, closed=True):
    set: "capo_continuum.types.kubernetes_cluster_role_configuration.KubernetesClusterRoleConfiguration"


class KubernetesClusterRoleUpdateRemoveMember(TypedDict, closed=True):
    remove: "capo_continuum.types.remove_kubernetes_cluster_role.RemoveKubernetesClusterRole"


KubernetesClusterRoleUpdate: TypeAlias = (
    KubernetesClusterRoleUpdateSetMember
    | KubernetesClusterRoleUpdateRemoveMember
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: KubernetesClusterRoleUpdate) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"KubernetesClusterRoleUpdate: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "set" in value:
        import capo_continuum.types.kubernetes_cluster_role_configuration

        return {
            "set": capo_continuum.types.kubernetes_cluster_role_configuration.serialize_json(
                value["set"]
            )
        }
    elif "remove" in value:
        import capo_continuum.types.remove_kubernetes_cluster_role

        return {
            "remove": capo_continuum.types.remove_kubernetes_cluster_role.serialize_json(
                value["remove"]
            )
        }
    else:
        raise SerializationError("KubernetesClusterRoleUpdate: no variant present")


def deserialize_json(data: dict) -> KubernetesClusterRoleUpdate:
    if data.get("set") is not None:
        import capo_continuum.types.kubernetes_cluster_role_configuration

        return {
            "set": capo_continuum.types.kubernetes_cluster_role_configuration.deserialize_json(
                data["set"]
            )
        }
    elif data.get("remove") is not None:
        import capo_continuum.types.remove_kubernetes_cluster_role

        return {
            "remove": capo_continuum.types.remove_kubernetes_cluster_role.deserialize_json(
                data["remove"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError(
            "KubernetesClusterRoleUpdate: no recognized variant key"
        )


def redact_sensitive(value: KubernetesClusterRoleUpdate) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "set" in value:
        import capo_continuum.types.kubernetes_cluster_role_configuration

        out["set"] = (
            capo_continuum.types.kubernetes_cluster_role_configuration.redact_sensitive(
                value["set"]
            )
        )
    return out
