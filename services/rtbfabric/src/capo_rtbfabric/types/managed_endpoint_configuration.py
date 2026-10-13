"""Generated from Smithy shape ``com.amazonaws.rtbfabric#ManagedEndpointConfiguration``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_rtbfabric.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_rtbfabric.types.auto_scaling_groups_configuration
    import capo_rtbfabric.types.eks_endpoints_configuration


class _ManagedEndpointConfiguration_autoScalingGroups(TypedDict, closed=True):
    autoScalingGroups: "capo_rtbfabric.types.auto_scaling_groups_configuration.AutoScalingGroupsConfiguration"


class _ManagedEndpointConfiguration_eksEndpoints(TypedDict, closed=True):
    eksEndpoints: (
        "capo_rtbfabric.types.eks_endpoints_configuration.EksEndpointsConfiguration"
    )


ManagedEndpointConfiguration: TypeAlias = (
    _ManagedEndpointConfiguration_autoScalingGroups
    | _ManagedEndpointConfiguration_eksEndpoints
)


# --- restJson1 ser/de ---
def serialize_json(value: ManagedEndpointConfiguration) -> dict:
    if "autoScalingGroups" in value:
        import capo_rtbfabric.types.auto_scaling_groups_configuration

        return {
            "autoScalingGroups": capo_rtbfabric.types.auto_scaling_groups_configuration.serialize_json(
                value["autoScalingGroups"]
            )
        }
    elif "eksEndpoints" in value:
        import capo_rtbfabric.types.eks_endpoints_configuration

        return {
            "eksEndpoints": capo_rtbfabric.types.eks_endpoints_configuration.serialize_json(
                value["eksEndpoints"]
            )
        }
    else:
        raise SerializationError("ManagedEndpointConfiguration: no variant present")


def deserialize_json(data: dict) -> ManagedEndpointConfiguration:
    if data.get("autoScalingGroups") is not None:
        import capo_rtbfabric.types.auto_scaling_groups_configuration

        return {
            "autoScalingGroups": capo_rtbfabric.types.auto_scaling_groups_configuration.deserialize_json(
                data["autoScalingGroups"]
            )
        }
    elif data.get("eksEndpoints") is not None:
        import capo_rtbfabric.types.eks_endpoints_configuration

        return {
            "eksEndpoints": capo_rtbfabric.types.eks_endpoints_configuration.deserialize_json(
                data["eksEndpoints"]
            )
        }
    else:
        raise DeserializationError(
            "ManagedEndpointConfiguration: no recognized variant key"
        )


def redact_sensitive(value: ManagedEndpointConfiguration) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "eksEndpoints" in value:
        import capo_rtbfabric.types.eks_endpoints_configuration

        out["eksEndpoints"] = (
            capo_rtbfabric.types.eks_endpoints_configuration.redact_sensitive(
                value["eksEndpoints"]
            )
        )
    return out
