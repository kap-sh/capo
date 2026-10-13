"""Generated from Smithy shape ``com.amazonaws.qconnect#GuardrailPiiEntitiesConfig``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_qconnect.types.guardrail_pii_entity_config

GuardrailPiiEntitiesConfig: TypeAlias = list[
    "capo_qconnect.types.guardrail_pii_entity_config.GuardrailPiiEntityConfig"
]


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailPiiEntitiesConfig) -> list:
    import capo_qconnect.types.guardrail_pii_entity_config

    out: list = []
    for item in value:
        out.append(capo_qconnect.types.guardrail_pii_entity_config.serialize_json(item))
    return out


def deserialize_json(data: list) -> GuardrailPiiEntitiesConfig:
    import capo_qconnect.types.guardrail_pii_entity_config

    out: GuardrailPiiEntitiesConfig = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_qconnect.types.guardrail_pii_entity_config.deserialize_json(item)
        )
    return out


def redact_sensitive(value: GuardrailPiiEntitiesConfig) -> list[Any]:
    import capo_qconnect.types.guardrail_pii_entity_config

    return [
        capo_qconnect.types.guardrail_pii_entity_config.redact_sensitive(item)
        for item in value
    ]
