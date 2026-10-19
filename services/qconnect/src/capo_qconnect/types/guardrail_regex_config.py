"""Generated from Smithy shape ``com.amazonaws.qconnect#GuardrailRegexConfig``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qconnect.types.guardrail_regex_description
    import capo_qconnect.types.guardrail_regex_name
    import capo_qconnect.types.guardrail_regex_pattern
    import capo_qconnect.types.guardrail_sensitive_information_action


class GuardrailRegexConfig(TypedDict, closed=True):
    name: "capo_qconnect.types.guardrail_regex_name.GuardrailRegexName"
    """<p>The name of the regular expression to configure for the AI Guardrail.</p>"""
    description: NotRequired[
        "capo_qconnect.types.guardrail_regex_description.GuardrailRegexDescription"
    ]
    """<p>The description of the regular expression to configure for the AI Guardrail.</p>"""
    pattern: "capo_qconnect.types.guardrail_regex_pattern.GuardrailRegexPattern"
    """<p>The regular expression pattern to configure for the AI Guardrail.</p>"""
    action: "capo_qconnect.types.guardrail_sensitive_information_action.GuardrailSensitiveInformationAction"
    """<p>The AI Guardrail action to configure when matching regular expression is detected.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailRegexConfig) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    out["pattern"] = value["pattern"]
    out["action"] = value["action"]
    return out


def deserialize_json(data: dict) -> GuardrailRegexConfig:
    out: GuardrailRegexConfig = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("pattern") is not None:
        out["pattern"] = data["pattern"]
    else:
        out["pattern"] = ""
    if data.get("action") is not None:
        out["action"] = data["action"]
    else:
        out["action"] = ""
    return out


def redact_sensitive(value: GuardrailRegexConfig) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "name" in value:
        out["name"] = "*** Sensitive Data Redacted ***"
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    if "pattern" in value:
        out["pattern"] = "*** Sensitive Data Redacted ***"
    if "action" in value:
        out["action"] = "*** Sensitive Data Redacted ***"
    return out
