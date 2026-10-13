"""Generated from Smithy shape ``com.amazonaws.bedrock#GuardrailContentFiltersConfig``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock.types.guardrail_content_filter_config

GuardrailContentFiltersConfig: TypeAlias = list[
    "capo_bedrock.types.guardrail_content_filter_config.GuardrailContentFilterConfig"
]


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailContentFiltersConfig) -> list:
    import capo_bedrock.types.guardrail_content_filter_config

    out: list = []
    for item in value:
        out.append(
            capo_bedrock.types.guardrail_content_filter_config.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> GuardrailContentFiltersConfig:
    import capo_bedrock.types.guardrail_content_filter_config

    out: GuardrailContentFiltersConfig = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock.types.guardrail_content_filter_config.deserialize_json(item)
        )
    return out


def redact_sensitive(value: GuardrailContentFiltersConfig) -> list[Any]:
    import capo_bedrock.types.guardrail_content_filter_config

    return [
        capo_bedrock.types.guardrail_content_filter_config.redact_sensitive(item)
        for item in value
    ]
