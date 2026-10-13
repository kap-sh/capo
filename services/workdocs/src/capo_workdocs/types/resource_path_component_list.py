"""Generated from Smithy shape ``com.amazonaws.workdocs#ResourcePathComponentList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_workdocs.types.resource_path_component

ResourcePathComponentList: TypeAlias = list[
    "capo_workdocs.types.resource_path_component.ResourcePathComponent"
]


# --- restJson1 ser/de ---
def serialize_json(value: ResourcePathComponentList) -> list:
    import capo_workdocs.types.resource_path_component

    out: list = []
    for item in value:
        out.append(capo_workdocs.types.resource_path_component.serialize_json(item))
    return out


def deserialize_json(data: list) -> ResourcePathComponentList:
    import capo_workdocs.types.resource_path_component

    out: ResourcePathComponentList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_workdocs.types.resource_path_component.deserialize_json(item))
    return out


def redact_sensitive(value: ResourcePathComponentList) -> list[Any]:
    import capo_workdocs.types.resource_path_component

    return [
        capo_workdocs.types.resource_path_component.redact_sensitive(item)
        for item in value
    ]
