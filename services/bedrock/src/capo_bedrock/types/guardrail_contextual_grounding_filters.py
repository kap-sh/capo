"""Generated from Smithy shape ``com.amazonaws.bedrock#GuardrailContextualGroundingFilters``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock.types.guardrail_contextual_grounding_filter

GuardrailContextualGroundingFilters: TypeAlias = list[
    "capo_bedrock.types.guardrail_contextual_grounding_filter.GuardrailContextualGroundingFilter"
]


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailContextualGroundingFilters) -> list:
    import capo_bedrock.types.guardrail_contextual_grounding_filter

    out: list = []
    for item in value:
        out.append(
            capo_bedrock.types.guardrail_contextual_grounding_filter.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> GuardrailContextualGroundingFilters:
    import capo_bedrock.types.guardrail_contextual_grounding_filter

    out: GuardrailContextualGroundingFilters = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock.types.guardrail_contextual_grounding_filter.deserialize_json(
                item
            )
        )
    return out


def redact_sensitive(value: GuardrailContextualGroundingFilters) -> list[Any]:
    import capo_bedrock.types.guardrail_contextual_grounding_filter

    return [
        capo_bedrock.types.guardrail_contextual_grounding_filter.redact_sensitive(item)
        for item in value
    ]
