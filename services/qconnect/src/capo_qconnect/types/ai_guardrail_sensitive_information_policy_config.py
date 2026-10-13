"""Generated from Smithy shape ``com.amazonaws.qconnect#AIGuardrailSensitiveInformationPolicyConfig``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qconnect.types.guardrail_pii_entities_config
    import capo_qconnect.types.guardrail_regexes_config


class AIGuardrailSensitiveInformationPolicyConfig(TypedDict, closed=True):
    pii_entities_config: NotRequired[
        "capo_qconnect.types.guardrail_pii_entities_config.GuardrailPiiEntitiesConfig"
    ]
    """<p>A list of PII entities to configure to the AI Guardrail.</p>"""
    regexes_config: NotRequired[
        "capo_qconnect.types.guardrail_regexes_config.GuardrailRegexesConfig"
    ]
    """<p>A list of regular expressions to configure to the AI Guardrail.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AIGuardrailSensitiveInformationPolicyConfig) -> dict:
    out: dict = {}
    if "pii_entities_config" in value:
        import capo_qconnect.types.guardrail_pii_entities_config

        out["piiEntitiesConfig"] = (
            capo_qconnect.types.guardrail_pii_entities_config.serialize_json(
                value["pii_entities_config"]
            )
        )
    if "regexes_config" in value:
        import capo_qconnect.types.guardrail_regexes_config

        out["regexesConfig"] = (
            capo_qconnect.types.guardrail_regexes_config.serialize_json(
                value["regexes_config"]
            )
        )
    return out


def deserialize_json(data: dict) -> AIGuardrailSensitiveInformationPolicyConfig:
    out: AIGuardrailSensitiveInformationPolicyConfig = {}  # type: ignore[typeddict-item]
    if data.get("piiEntitiesConfig") is not None:
        import capo_qconnect.types.guardrail_pii_entities_config

        out["pii_entities_config"] = (
            capo_qconnect.types.guardrail_pii_entities_config.deserialize_json(
                data["piiEntitiesConfig"]
            )
        )
    if data.get("regexesConfig") is not None:
        import capo_qconnect.types.guardrail_regexes_config

        out["regexes_config"] = (
            capo_qconnect.types.guardrail_regexes_config.deserialize_json(
                data["regexesConfig"]
            )
        )
    return out


def redact_sensitive(
    value: AIGuardrailSensitiveInformationPolicyConfig,
) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "pii_entities_config" in value:
        import capo_qconnect.types.guardrail_pii_entities_config

        out["pii_entities_config"] = (
            capo_qconnect.types.guardrail_pii_entities_config.redact_sensitive(
                value["pii_entities_config"]
            )
        )
    if "regexes_config" in value:
        import capo_qconnect.types.guardrail_regexes_config

        out["regexes_config"] = (
            capo_qconnect.types.guardrail_regexes_config.redact_sensitive(
                value["regexes_config"]
            )
        )
    return out
