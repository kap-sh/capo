"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#InvokeGuardrailChecksRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_bedrock_runtime.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_runtime.types.guardrail_checks_config
    import capo_bedrock_runtime.types.guardrail_checks_message_list


class InvokeGuardrailChecksRequest(TypedDict, closed=True):
    messages: "capo_bedrock_runtime.types.guardrail_checks_message_list.GuardrailChecksMessageList"
    """<p>The messages to evaluate against the specified guardrail checks. Each message includes a role and one or more content blocks.</p>"""
    checks: "capo_bedrock_runtime.types.guardrail_checks_config.GuardrailChecksConfig"
    """<p>The inline check configurations that specify which guardrail checks to run against the messages.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InvokeGuardrailChecksRequest) -> dict:
    out: dict = {}
    import capo_bedrock_runtime.types.guardrail_checks_message_list

    out["messages"] = (
        capo_bedrock_runtime.types.guardrail_checks_message_list.serialize_json(
            value["messages"]
        )
    )
    import capo_bedrock_runtime.types.guardrail_checks_config

    out["checks"] = capo_bedrock_runtime.types.guardrail_checks_config.serialize_json(
        value["checks"]
    )
    return out


def deserialize_json(data: dict) -> InvokeGuardrailChecksRequest:
    out: InvokeGuardrailChecksRequest = {}  # type: ignore[typeddict-item]
    if data.get("messages") is not None:
        import capo_bedrock_runtime.types.guardrail_checks_message_list

        out["messages"] = (
            capo_bedrock_runtime.types.guardrail_checks_message_list.deserialize_json(
                data["messages"]
            )
        )
    else:
        raise DeserializationError("InvokeGuardrailChecksRequest.messages required")
    if data.get("checks") is not None:
        import capo_bedrock_runtime.types.guardrail_checks_config

        out["checks"] = (
            capo_bedrock_runtime.types.guardrail_checks_config.deserialize_json(
                data["checks"]
            )
        )
    else:
        raise DeserializationError("InvokeGuardrailChecksRequest.checks required")
    return out


def redact_sensitive(value: InvokeGuardrailChecksRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "messages" in value:
        import capo_bedrock_runtime.types.guardrail_checks_message_list

        out["messages"] = (
            capo_bedrock_runtime.types.guardrail_checks_message_list.redact_sensitive(
                value["messages"]
            )
        )
    return out
