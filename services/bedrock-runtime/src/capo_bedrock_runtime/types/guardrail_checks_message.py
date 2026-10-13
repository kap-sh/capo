"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#GuardrailChecksMessage``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_bedrock_runtime.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_runtime.types.guardrail_checks_content_block_list
    import capo_bedrock_runtime.types.guardrail_checks_role


class GuardrailChecksMessage(TypedDict, closed=True):
    role: "capo_bedrock_runtime.types.guardrail_checks_role.GuardrailChecksRole"
    """<p>The role of the message sender.</p>"""
    content: "capo_bedrock_runtime.types.guardrail_checks_content_block_list.GuardrailChecksContentBlockList"
    """<p>The content blocks for the message.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailChecksMessage) -> dict:
    out: dict = {}
    import capo_bedrock_runtime.types.guardrail_checks_role

    out["role"] = capo_bedrock_runtime.types.guardrail_checks_role.serialize_json(
        value["role"]
    )
    import capo_bedrock_runtime.types.guardrail_checks_content_block_list

    out["content"] = (
        capo_bedrock_runtime.types.guardrail_checks_content_block_list.serialize_json(
            value["content"]
        )
    )
    return out


def deserialize_json(data: dict) -> GuardrailChecksMessage:
    out: GuardrailChecksMessage = {}  # type: ignore[typeddict-item]
    if data.get("role") is not None:
        import capo_bedrock_runtime.types.guardrail_checks_role

        out["role"] = capo_bedrock_runtime.types.guardrail_checks_role.deserialize_json(
            data["role"]
        )
    else:
        raise DeserializationError("GuardrailChecksMessage.role required")
    if data.get("content") is not None:
        import capo_bedrock_runtime.types.guardrail_checks_content_block_list

        out["content"] = (
            capo_bedrock_runtime.types.guardrail_checks_content_block_list.deserialize_json(
                data["content"]
            )
        )
    else:
        raise DeserializationError("GuardrailChecksMessage.content required")
    return out


def redact_sensitive(value: GuardrailChecksMessage) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "content" in value:
        import capo_bedrock_runtime.types.guardrail_checks_content_block_list

        out["content"] = (
            capo_bedrock_runtime.types.guardrail_checks_content_block_list.redact_sensitive(
                value["content"]
            )
        )
    return out
