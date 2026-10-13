"""Generated from Smithy shape ``com.amazonaws.qconnect#MultiAgentConfigurationList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_qconnect.types.multi_agent_configuration

MultiAgentConfigurationList: TypeAlias = list[
    "capo_qconnect.types.multi_agent_configuration.MultiAgentConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: MultiAgentConfigurationList) -> list:
    import capo_qconnect.types.multi_agent_configuration

    out: list = []
    for item in value:
        out.append(capo_qconnect.types.multi_agent_configuration.serialize_json(item))
    return out


def deserialize_json(data: list) -> MultiAgentConfigurationList:
    import capo_qconnect.types.multi_agent_configuration

    out: MultiAgentConfigurationList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_qconnect.types.multi_agent_configuration.deserialize_json(item))
    return out


def redact_sensitive(value: MultiAgentConfigurationList) -> list[Any]:
    import capo_qconnect.types.multi_agent_configuration

    return [
        capo_qconnect.types.multi_agent_configuration.redact_sensitive(item)
        for item in value
    ]
