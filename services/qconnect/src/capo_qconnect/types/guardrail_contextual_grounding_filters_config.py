"""Generated from Smithy shape ``com.amazonaws.qconnect#GuardrailContextualGroundingFiltersConfig``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_qconnect.types.guardrail_contextual_grounding_filter_config

GuardrailContextualGroundingFiltersConfig: TypeAlias = list[
    "capo_qconnect.types.guardrail_contextual_grounding_filter_config.GuardrailContextualGroundingFilterConfig"
]


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailContextualGroundingFiltersConfig) -> list:
    import capo_qconnect.types.guardrail_contextual_grounding_filter_config

    out: list = []
    for item in value:
        out.append(
            capo_qconnect.types.guardrail_contextual_grounding_filter_config.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> GuardrailContextualGroundingFiltersConfig:
    import capo_qconnect.types.guardrail_contextual_grounding_filter_config

    out: GuardrailContextualGroundingFiltersConfig = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_qconnect.types.guardrail_contextual_grounding_filter_config.deserialize_json(
                item
            )
        )
    return out


def redact_sensitive(value: GuardrailContextualGroundingFiltersConfig) -> list[Any]:
    import capo_qconnect.types.guardrail_contextual_grounding_filter_config

    return [
        capo_qconnect.types.guardrail_contextual_grounding_filter_config.redact_sensitive(
            item
        )
        for item in value
    ]
