"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#AgenticRetrieveGuardrailWarning``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.guardrail_action


class AgenticRetrieveGuardrailWarning(TypedDict, closed=True):
    id: "str"
    """<p>The unique identifier of the guardrail.</p>"""
    version: "str"
    """<p>The version of the guardrail.</p>"""
    action: "capo_bedrock_agent_runtime.types.guardrail_action.GuardrailAction"
    """<p>The action taken by the guardrail.</p>"""
    message: NotRequired["str"]
    """<p>A message describing the guardrail evaluation result.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AgenticRetrieveGuardrailWarning) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["version"] = value["version"]
    import capo_bedrock_agent_runtime.types.guardrail_action

    out["action"] = capo_bedrock_agent_runtime.types.guardrail_action.serialize_json(
        value["action"]
    )
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> AgenticRetrieveGuardrailWarning:
    out: AgenticRetrieveGuardrailWarning = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    if data.get("version") is not None:
        out["version"] = data["version"]
    else:
        out["version"] = ""
    if data.get("action") is not None:
        import capo_bedrock_agent_runtime.types.guardrail_action

        out["action"] = (
            capo_bedrock_agent_runtime.types.guardrail_action.deserialize_json(
                data["action"]
            )
        )
    else:
        import typing

        out["action"] = typing.cast(
            "capo_bedrock_agent_runtime.types.guardrail_action.GuardrailAction", ""
        )
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out
