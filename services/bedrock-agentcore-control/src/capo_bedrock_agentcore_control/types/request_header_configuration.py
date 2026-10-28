"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#RequestHeaderConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agentcore_control.errors import (
    DeserializationError,
    SerializationError,
)
from capo_bedrock_agentcore_control.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.request_header_allowlist


class RequestHeaderConfigurationRequestHeaderAllowlistMember(TypedDict, closed=True):
    requestHeaderAllowlist: "capo_bedrock_agentcore_control.types.request_header_allowlist.RequestHeaderAllowlist"


RequestHeaderConfiguration: TypeAlias = (
    RequestHeaderConfigurationRequestHeaderAllowlistMember | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: RequestHeaderConfiguration) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"RequestHeaderConfiguration: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "requestHeaderAllowlist" in value:
        import capo_bedrock_agentcore_control.types.request_header_allowlist

        return {
            "requestHeaderAllowlist": capo_bedrock_agentcore_control.types.request_header_allowlist.serialize_json(
                value["requestHeaderAllowlist"]
            )
        }
    else:
        raise SerializationError("RequestHeaderConfiguration: no variant present")


def deserialize_json(data: dict) -> RequestHeaderConfiguration:
    if data.get("requestHeaderAllowlist") is not None:
        import capo_bedrock_agentcore_control.types.request_header_allowlist

        return {
            "requestHeaderAllowlist": capo_bedrock_agentcore_control.types.request_header_allowlist.deserialize_json(
                data["requestHeaderAllowlist"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError(
            "RequestHeaderConfiguration: no recognized variant key"
        )
