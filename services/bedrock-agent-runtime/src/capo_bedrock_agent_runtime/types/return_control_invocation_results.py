"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#ReturnControlInvocationResults``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.invocation_result_member

ReturnControlInvocationResults: TypeAlias = list[
    "capo_bedrock_agent_runtime.types.invocation_result_member.InvocationResultMember"
]


# --- restJson1 ser/de ---
def serialize_json(value: ReturnControlInvocationResults) -> list:
    import capo_bedrock_agent_runtime.types.invocation_result_member

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_agent_runtime.types.invocation_result_member.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ReturnControlInvocationResults:
    import capo_bedrock_agent_runtime.types.invocation_result_member

    out: ReturnControlInvocationResults = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock_agent_runtime.types.invocation_result_member.deserialize_json(
                item
            )
        )
    return out


def redact_sensitive(value: ReturnControlInvocationResults) -> list[Any]:
    import capo_bedrock_agent_runtime.types.invocation_result_member

    return [
        capo_bedrock_agent_runtime.types.invocation_result_member.redact_sensitive(item)
        for item in value
    ]
