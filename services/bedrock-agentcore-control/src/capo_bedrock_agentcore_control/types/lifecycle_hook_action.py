"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#LifecycleHookAction``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agentcore_control.errors import (
    DeserializationError,
    SerializationError,
)
from capo_bedrock_agentcore_control.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.http_post_lifecycle_hook_action


class LifecycleHookActionHttpPostMember(TypedDict, closed=True):
    httpPost: "capo_bedrock_agentcore_control.types.http_post_lifecycle_hook_action.HttpPostLifecycleHookAction"


LifecycleHookAction: TypeAlias = LifecycleHookActionHttpPostMember | UnknownUnionMember


# --- restJson1 ser/de ---
def serialize_json(value: LifecycleHookAction) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"LifecycleHookAction: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "httpPost" in value:
        import capo_bedrock_agentcore_control.types.http_post_lifecycle_hook_action

        return {
            "httpPost": capo_bedrock_agentcore_control.types.http_post_lifecycle_hook_action.serialize_json(
                value["httpPost"]
            )
        }
    else:
        raise SerializationError("LifecycleHookAction: no variant present")


def deserialize_json(data: dict) -> LifecycleHookAction:
    if data.get("httpPost") is not None:
        import capo_bedrock_agentcore_control.types.http_post_lifecycle_hook_action

        return {
            "httpPost": capo_bedrock_agentcore_control.types.http_post_lifecycle_hook_action.deserialize_json(
                data["httpPost"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("LifecycleHookAction: no recognized variant key")
