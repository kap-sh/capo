"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#BedrockGuardrailConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lex_models_v2.types.bedrock_guardrail_identifier
    import capo_lex_models_v2.types.bedrock_guardrail_version


class BedrockGuardrailConfiguration(TypedDict, closed=True):
    identifier: "capo_lex_models_v2.types.bedrock_guardrail_identifier.BedrockGuardrailIdentifier"
    """<p>The unique guardrail id for the Bedrock guardrail configuration.</p>"""
    version: (
        "capo_lex_models_v2.types.bedrock_guardrail_version.BedrockGuardrailVersion"
    )
    """<p>The guardrail version for the Bedrock guardrail configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BedrockGuardrailConfiguration) -> dict:
    out: dict = {}
    out["identifier"] = value["identifier"]
    out["version"] = value["version"]
    return out


def deserialize_json(data: dict) -> BedrockGuardrailConfiguration:
    out: BedrockGuardrailConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("identifier") is not None:
        out["identifier"] = data["identifier"]
    else:
        out["identifier"] = ""
    if data.get("version") is not None:
        out["version"] = data["version"]
    else:
        out["version"] = ""
    return out
