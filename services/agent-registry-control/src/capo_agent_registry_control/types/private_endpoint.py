"""Generated from Smithy shape ``com.amazonaws.agentregistrycontrol#PrivateEndpoint``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_agent_registry_control.errors import DeserializationError, SerializationError
from capo_agent_registry_control.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_agent_registry_control.types.managed_vpc_resource
    import capo_agent_registry_control.types.self_managed_lattice_resource


class _PrivateEndpoint_selfManagedLatticeResource(TypedDict, closed=True):
    selfManagedLatticeResource: "capo_agent_registry_control.types.self_managed_lattice_resource.SelfManagedLatticeResource"


class _PrivateEndpoint_managedVpcResource(TypedDict, closed=True):
    managedVpcResource: (
        "capo_agent_registry_control.types.managed_vpc_resource.ManagedVpcResource"
    )


PrivateEndpoint: TypeAlias = (
    _PrivateEndpoint_selfManagedLatticeResource
    | _PrivateEndpoint_managedVpcResource
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: PrivateEndpoint) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"PrivateEndpoint: cannot serialize unknown variant {value.name!r}"
        )
    elif "selfManagedLatticeResource" in value:
        import capo_agent_registry_control.types.self_managed_lattice_resource

        return {
            "selfManagedLatticeResource": capo_agent_registry_control.types.self_managed_lattice_resource.serialize_json(
                value["selfManagedLatticeResource"]
            )
        }
    elif "managedVpcResource" in value:
        import capo_agent_registry_control.types.managed_vpc_resource

        return {
            "managedVpcResource": capo_agent_registry_control.types.managed_vpc_resource.serialize_json(
                value["managedVpcResource"]
            )
        }
    else:
        raise SerializationError("PrivateEndpoint: no variant present")


def deserialize_json(data: dict) -> PrivateEndpoint:
    if data.get("selfManagedLatticeResource") is not None:
        import capo_agent_registry_control.types.self_managed_lattice_resource

        return {
            "selfManagedLatticeResource": capo_agent_registry_control.types.self_managed_lattice_resource.deserialize_json(
                data["selfManagedLatticeResource"]
            )
        }
    elif data.get("managedVpcResource") is not None:
        import capo_agent_registry_control.types.managed_vpc_resource

        return {
            "managedVpcResource": capo_agent_registry_control.types.managed_vpc_resource.deserialize_json(
                data["managedVpcResource"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError("PrivateEndpoint: no recognized variant key")
