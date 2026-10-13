"""Generated from Smithy shape ``com.amazonaws.resourceexplorer2#ViewList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_resource_explorer_2.types.view

ViewList: TypeAlias = list["capo_resource_explorer_2.types.view.View"]


# --- restJson1 ser/de ---
def serialize_json(value: ViewList) -> list:
    import capo_resource_explorer_2.types.view

    out: list = []
    for item in value:
        out.append(capo_resource_explorer_2.types.view.serialize_json(item))
    return out


def deserialize_json(data: list) -> ViewList:
    import capo_resource_explorer_2.types.view

    out: ViewList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_resource_explorer_2.types.view.deserialize_json(item))
    return out


def redact_sensitive(value: ViewList) -> list[Any]:
    import capo_resource_explorer_2.types.view

    return [
        capo_resource_explorer_2.types.view.redact_sensitive(item) for item in value
    ]
