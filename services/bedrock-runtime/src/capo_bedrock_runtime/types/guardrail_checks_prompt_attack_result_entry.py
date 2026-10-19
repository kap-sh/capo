"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#GuardrailChecksPromptAttackResultEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_runtime.types.guardrail_checks_prompt_attack_category


class GuardrailChecksPromptAttackResultEntry(TypedDict, closed=True):
    category: "capo_bedrock_runtime.types.guardrail_checks_prompt_attack_category.GuardrailChecksPromptAttackCategory"
    """<p>The prompt attack category that was evaluated.</p>"""
    severity_score: "float"
    """<p>The severity score for the category, ranging from 0.0 to 1.0. Higher values indicate greater severity.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailChecksPromptAttackResultEntry) -> dict:
    out: dict = {}
    import capo_bedrock_runtime.types.guardrail_checks_prompt_attack_category

    out["category"] = (
        capo_bedrock_runtime.types.guardrail_checks_prompt_attack_category.serialize_json(
            value["category"]
        )
    )
    out["severityScore"] = (
        "NaN"
        if value["severity_score"] != value["severity_score"]
        else "Infinity"
        if value["severity_score"] == float("inf")
        else "-Infinity"
        if value["severity_score"] == float("-inf")
        else value["severity_score"]
    )
    return out


def deserialize_json(data: dict) -> GuardrailChecksPromptAttackResultEntry:
    out: GuardrailChecksPromptAttackResultEntry = {}  # type: ignore[typeddict-item]
    if data.get("category") is not None:
        import capo_bedrock_runtime.types.guardrail_checks_prompt_attack_category

        out["category"] = (
            capo_bedrock_runtime.types.guardrail_checks_prompt_attack_category.deserialize_json(
                data["category"]
            )
        )
    else:
        import typing

        out["category"] = typing.cast(
            "capo_bedrock_runtime.types.guardrail_checks_prompt_attack_category.GuardrailChecksPromptAttackCategory",
            "",
        )
    if data.get("severityScore") is not None:
        out["severity_score"] = float(data["severityScore"])
    else:
        out["severity_score"] = 0.0
    return out
