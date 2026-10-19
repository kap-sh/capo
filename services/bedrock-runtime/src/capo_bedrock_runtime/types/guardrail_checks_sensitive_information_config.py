"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#GuardrailChecksSensitiveInformationConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_runtime.types.guardrail_checks_sensitive_information_entity_config_list


class GuardrailChecksSensitiveInformationConfig(TypedDict, closed=True):
    entities: "capo_bedrock_runtime.types.guardrail_checks_sensitive_information_entity_config_list.GuardrailChecksSensitiveInformationEntityConfigList"
    """<p>The sensitive information entity types to detect.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailChecksSensitiveInformationConfig) -> dict:
    out: dict = {}
    import capo_bedrock_runtime.types.guardrail_checks_sensitive_information_entity_config_list

    out["entities"] = (
        capo_bedrock_runtime.types.guardrail_checks_sensitive_information_entity_config_list.serialize_json(
            value["entities"]
        )
    )
    return out


def deserialize_json(data: dict) -> GuardrailChecksSensitiveInformationConfig:
    out: GuardrailChecksSensitiveInformationConfig = {}  # type: ignore[typeddict-item]
    if data.get("entities") is not None:
        import capo_bedrock_runtime.types.guardrail_checks_sensitive_information_entity_config_list

        out["entities"] = (
            capo_bedrock_runtime.types.guardrail_checks_sensitive_information_entity_config_list.deserialize_json(
                data["entities"]
            )
        )
    else:
        out["entities"] = []
    return out
