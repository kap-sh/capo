"""Generated from Smithy shape ``com.amazonaws.devopsagent#PrivateConnectionMode``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_devops_agent.errors import DeserializationError, SerializationError
from capo_devops_agent.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_devops_agent.types.self_managed_input
    import capo_devops_agent.types.service_managed_input


class PrivateConnectionModeServiceManagedMember(TypedDict, closed=True):
    serviceManaged: "capo_devops_agent.types.service_managed_input.ServiceManagedInput"


class PrivateConnectionModeSelfManagedMember(TypedDict, closed=True):
    selfManaged: "capo_devops_agent.types.self_managed_input.SelfManagedInput"


PrivateConnectionMode: TypeAlias = (
    PrivateConnectionModeServiceManagedMember
    | PrivateConnectionModeSelfManagedMember
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: PrivateConnectionMode) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"PrivateConnectionMode: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "serviceManaged" in value:
        import capo_devops_agent.types.service_managed_input

        return {
            "serviceManaged": capo_devops_agent.types.service_managed_input.serialize_json(
                value["serviceManaged"]
            )
        }
    elif "selfManaged" in value:
        import capo_devops_agent.types.self_managed_input

        return {
            "selfManaged": capo_devops_agent.types.self_managed_input.serialize_json(
                value["selfManaged"]
            )
        }
    else:
        raise SerializationError("PrivateConnectionMode: no variant present")


def deserialize_json(data: dict) -> PrivateConnectionMode:
    if data.get("serviceManaged") is not None:
        import capo_devops_agent.types.service_managed_input

        return {
            "serviceManaged": capo_devops_agent.types.service_managed_input.deserialize_json(
                data["serviceManaged"]
            )
        }
    elif data.get("selfManaged") is not None:
        import capo_devops_agent.types.self_managed_input

        return {
            "selfManaged": capo_devops_agent.types.self_managed_input.deserialize_json(
                data["selfManaged"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("PrivateConnectionMode: no recognized variant key")
