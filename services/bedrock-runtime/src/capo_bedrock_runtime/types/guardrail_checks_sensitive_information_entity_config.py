"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#GuardrailChecksSensitiveInformationEntityConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_runtime.types.guardrail_checks_sensitive_information_entity_type


class GuardrailChecksSensitiveInformationEntityConfig(TypedDict, closed=True):
    type: "capo_bedrock_runtime.types.guardrail_checks_sensitive_information_entity_type.GuardrailChecksSensitiveInformationEntityType"
    """<p>The PII entity type to detect.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailChecksSensitiveInformationEntityConfig) -> dict:
    out: dict = {}
    import capo_bedrock_runtime.types.guardrail_checks_sensitive_information_entity_type

    out["type"] = (
        capo_bedrock_runtime.types.guardrail_checks_sensitive_information_entity_type.serialize_json(
            value["type"]
        )
    )
    return out


def deserialize_json(data: dict) -> GuardrailChecksSensitiveInformationEntityConfig:
    out: GuardrailChecksSensitiveInformationEntityConfig = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        import capo_bedrock_runtime.types.guardrail_checks_sensitive_information_entity_type

        out["type"] = (
            capo_bedrock_runtime.types.guardrail_checks_sensitive_information_entity_type.deserialize_json(
                data["type"]
            )
        )
    else:
        import typing

        out["type"] = typing.cast(
            "capo_bedrock_runtime.types.guardrail_checks_sensitive_information_entity_type.GuardrailChecksSensitiveInformationEntityType",
            "",
        )
    return out
