"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#GuardrailChecksPromptAttackConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_runtime.types.guardrail_checks_prompt_attack_category_config_list


class GuardrailChecksPromptAttackConfig(TypedDict, closed=True):
    categories: "capo_bedrock_runtime.types.guardrail_checks_prompt_attack_category_config_list.GuardrailChecksPromptAttackCategoryConfigList"
    """<p>The prompt attack categories to evaluate.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailChecksPromptAttackConfig) -> dict:
    out: dict = {}
    import capo_bedrock_runtime.types.guardrail_checks_prompt_attack_category_config_list

    out["categories"] = (
        capo_bedrock_runtime.types.guardrail_checks_prompt_attack_category_config_list.serialize_json(
            value["categories"]
        )
    )
    return out


def deserialize_json(data: dict) -> GuardrailChecksPromptAttackConfig:
    out: GuardrailChecksPromptAttackConfig = {}  # type: ignore[typeddict-item]
    if data.get("categories") is not None:
        import capo_bedrock_runtime.types.guardrail_checks_prompt_attack_category_config_list

        out["categories"] = (
            capo_bedrock_runtime.types.guardrail_checks_prompt_attack_category_config_list.deserialize_json(
                data["categories"]
            )
        )
    else:
        out["categories"] = []
    return out
