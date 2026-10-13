"""Generated from Smithy shape ``com.amazonaws.applicationdiscoveryservice#AgentsInfo``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_application_discovery_service.types.agent_info

AgentsInfo: TypeAlias = list[
    "capo_application_discovery_service.types.agent_info.AgentInfo"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AgentsInfo) -> list:
    import capo_application_discovery_service.types.agent_info

    out: list = []
    for item in value:
        out.append(
            capo_application_discovery_service.types.agent_info.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> AgentsInfo:
    import capo_application_discovery_service.types.agent_info

    out: AgentsInfo = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_application_discovery_service.types.agent_info.deserialize_aws_json_1_1(
                item
            )
        )
    return out


def redact_sensitive(value: AgentsInfo) -> list[Any]:
    import capo_application_discovery_service.types.agent_info

    return [
        capo_application_discovery_service.types.agent_info.redact_sensitive(item)
        for item in value
    ]
