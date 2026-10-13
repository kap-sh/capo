"""Generated from Smithy shape ``com.amazonaws.novaact#ToolSpecs``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_nova_act.types.tool_spec

ToolSpecs: TypeAlias = list["capo_nova_act.types.tool_spec.ToolSpec"]


# --- restJson1 ser/de ---
def serialize_json(value: ToolSpecs) -> list:
    import capo_nova_act.types.tool_spec

    out: list = []
    for item in value:
        out.append(capo_nova_act.types.tool_spec.serialize_json(item))
    return out


def deserialize_json(data: list) -> ToolSpecs:
    import capo_nova_act.types.tool_spec

    out: ToolSpecs = []
    for item in data:
        if item is None:
            continue
        out.append(capo_nova_act.types.tool_spec.deserialize_json(item))
    return out


def redact_sensitive(value: ToolSpecs) -> list[Any]:
    import capo_nova_act.types.tool_spec

    return [capo_nova_act.types.tool_spec.redact_sensitive(item) for item in value]
