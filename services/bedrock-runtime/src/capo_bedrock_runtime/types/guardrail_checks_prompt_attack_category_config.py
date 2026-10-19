"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#GuardrailChecksPromptAttackCategoryConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_runtime.types.guardrail_checks_prompt_attack_category


class GuardrailChecksPromptAttackCategoryConfig(TypedDict, closed=True):
    category: "capo_bedrock_runtime.types.guardrail_checks_prompt_attack_category.GuardrailChecksPromptAttackCategory"
    """<p>The prompt attack category to evaluate.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailChecksPromptAttackCategoryConfig) -> dict:
    out: dict = {}
    import capo_bedrock_runtime.types.guardrail_checks_prompt_attack_category

    out["category"] = (
        capo_bedrock_runtime.types.guardrail_checks_prompt_attack_category.serialize_json(
            value["category"]
        )
    )
    return out


def deserialize_json(data: dict) -> GuardrailChecksPromptAttackCategoryConfig:
    out: GuardrailChecksPromptAttackCategoryConfig = {}  # type: ignore[typeddict-item]
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
    return out
