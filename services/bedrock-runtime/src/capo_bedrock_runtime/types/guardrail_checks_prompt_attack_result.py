"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#GuardrailChecksPromptAttackResult``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_runtime.types.guardrail_checks_prompt_attack_result_list


class GuardrailChecksPromptAttackResult(TypedDict, closed=True):
    results: "capo_bedrock_runtime.types.guardrail_checks_prompt_attack_result_list.GuardrailChecksPromptAttackResultList"
    """<p>The per-category prompt attack results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailChecksPromptAttackResult) -> dict:
    out: dict = {}
    import capo_bedrock_runtime.types.guardrail_checks_prompt_attack_result_list

    out["results"] = (
        capo_bedrock_runtime.types.guardrail_checks_prompt_attack_result_list.serialize_json(
            value["results"]
        )
    )
    return out


def deserialize_json(data: dict) -> GuardrailChecksPromptAttackResult:
    out: GuardrailChecksPromptAttackResult = {}  # type: ignore[typeddict-item]
    if data.get("results") is not None:
        import capo_bedrock_runtime.types.guardrail_checks_prompt_attack_result_list

        out["results"] = (
            capo_bedrock_runtime.types.guardrail_checks_prompt_attack_result_list.deserialize_json(
                data["results"]
            )
        )
    else:
        out["results"] = []
    return out
