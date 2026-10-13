"""Generated from Smithy shape ``com.amazonaws.devopsagent#AssociationsList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_devops_agent.types.association

AssociationsList: TypeAlias = list["capo_devops_agent.types.association.Association"]


# --- restJson1 ser/de ---
def serialize_json(value: AssociationsList) -> list:
    import capo_devops_agent.types.association

    out: list = []
    for item in value:
        out.append(capo_devops_agent.types.association.serialize_json(item))
    return out


def deserialize_json(data: list) -> AssociationsList:
    import capo_devops_agent.types.association

    out: AssociationsList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_devops_agent.types.association.deserialize_json(item))
    return out


def redact_sensitive(value: AssociationsList) -> list[Any]:
    import capo_devops_agent.types.association

    return [
        capo_devops_agent.types.association.redact_sensitive(item) for item in value
    ]
