"""Generated from Smithy shape ``com.amazonaws.bedrock#GuardrailConfiguration``."""

from typing_extensions import TypedDict


class GuardrailConfiguration(TypedDict, closed=True):
    guardrail_id: "str"
    """<p>The unique identifier for the guardrail.</p>"""
    guardrail_version: "str"
    """<p>The version of the guardrail.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailConfiguration) -> dict:
    out: dict = {}
    out["guardrailId"] = value["guardrail_id"]
    out["guardrailVersion"] = value["guardrail_version"]
    return out


def deserialize_json(data: dict) -> GuardrailConfiguration:
    out: GuardrailConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("guardrailId") is not None:
        out["guardrail_id"] = data["guardrailId"]
    else:
        out["guardrail_id"] = ""
    if data.get("guardrailVersion") is not None:
        out["guardrail_version"] = data["guardrailVersion"]
    else:
        out["guardrail_version"] = ""
    return out
