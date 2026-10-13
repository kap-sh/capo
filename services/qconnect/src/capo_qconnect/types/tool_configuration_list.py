"""Generated from Smithy shape ``com.amazonaws.qconnect#ToolConfigurationList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_qconnect.types.tool_configuration

ToolConfigurationList: TypeAlias = list[
    "capo_qconnect.types.tool_configuration.ToolConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: ToolConfigurationList) -> list:
    import capo_qconnect.types.tool_configuration

    out: list = []
    for item in value:
        out.append(capo_qconnect.types.tool_configuration.serialize_json(item))
    return out


def deserialize_json(data: list) -> ToolConfigurationList:
    import capo_qconnect.types.tool_configuration

    out: ToolConfigurationList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_qconnect.types.tool_configuration.deserialize_json(item))
    return out


def redact_sensitive(value: ToolConfigurationList) -> list[Any]:
    import capo_qconnect.types.tool_configuration

    return [
        capo_qconnect.types.tool_configuration.redact_sensitive(item) for item in value
    ]
