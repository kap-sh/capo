"""Generated from Smithy shape ``com.amazonaws.bedrock#GuardrailStatusReasons``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock.types.guardrail_status_reason

GuardrailStatusReasons: TypeAlias = list[
    "capo_bedrock.types.guardrail_status_reason.GuardrailStatusReason"
]


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailStatusReasons) -> list:
    return list(value)


def deserialize_json(data: list) -> GuardrailStatusReasons:
    return [item for item in data if item is not None]


def redact_sensitive(value: GuardrailStatusReasons) -> list[Any]:
    return ["*** Sensitive Data Redacted ***"] * len(value)
