"""Generated from Smithy shape ``com.amazonaws.devopsagent#RegisteredServicesList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_devops_agent.types.registered_service

RegisteredServicesList: TypeAlias = list[
    "capo_devops_agent.types.registered_service.RegisteredService"
]


# --- restJson1 ser/de ---
def serialize_json(value: RegisteredServicesList) -> list:
    import capo_devops_agent.types.registered_service

    out: list = []
    for item in value:
        out.append(capo_devops_agent.types.registered_service.serialize_json(item))
    return out


def deserialize_json(data: list) -> RegisteredServicesList:
    import capo_devops_agent.types.registered_service

    out: RegisteredServicesList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_devops_agent.types.registered_service.deserialize_json(item))
    return out


def redact_sensitive(value: RegisteredServicesList) -> list[Any]:
    import capo_devops_agent.types.registered_service

    return [
        capo_devops_agent.types.registered_service.redact_sensitive(item)
        for item in value
    ]
