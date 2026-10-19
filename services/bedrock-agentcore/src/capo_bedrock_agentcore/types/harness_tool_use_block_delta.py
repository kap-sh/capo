"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#HarnessToolUseBlockDelta``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.sensitive_text


class HarnessToolUseBlockDelta(TypedDict, closed=True):
    input: "capo_bedrock_agentcore.types.sensitive_text.SensitiveText"
    """<p>The partial JSON input for the tool call.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HarnessToolUseBlockDelta) -> dict:
    out: dict = {}
    out["input"] = value["input"]
    return out


def deserialize_json(data: dict) -> HarnessToolUseBlockDelta:
    out: HarnessToolUseBlockDelta = {}  # type: ignore[typeddict-item]
    if data.get("input") is not None:
        out["input"] = data["input"]
    else:
        out["input"] = ""
    return out


def redact_sensitive(value: HarnessToolUseBlockDelta) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "input" in value:
        out["input"] = "*** Sensitive Data Redacted ***"
    return out
