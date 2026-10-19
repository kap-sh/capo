"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#HarnessInlineFunctionConfig``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.harness_inline_function_description
    import capo_bedrock_agentcore.types.sensitive_json


class HarnessInlineFunctionConfig(TypedDict, closed=True):
    description: "capo_bedrock_agentcore.types.harness_inline_function_description.HarnessInlineFunctionDescription"
    """<p>Description of what the tool does, provided to the model.</p>"""
    input_schema: "capo_bedrock_agentcore.types.sensitive_json.SensitiveJson"
    """<p>JSON Schema describing the tool's input parameters.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HarnessInlineFunctionConfig) -> dict:
    out: dict = {}
    out["description"] = value["description"]
    out["inputSchema"] = value["input_schema"]
    return out


def deserialize_json(data: dict) -> HarnessInlineFunctionConfig:
    out: HarnessInlineFunctionConfig = {}  # type: ignore[typeddict-item]
    if data.get("description") is not None:
        out["description"] = data["description"]
    else:
        out["description"] = ""
    if data.get("inputSchema") is not None:
        out["input_schema"] = data["inputSchema"]
    else:
        out["input_schema"] = None
    return out


def redact_sensitive(value: HarnessInlineFunctionConfig) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    if "input_schema" in value:
        out["input_schema"] = "*** Sensitive Data Redacted ***"
    return out
