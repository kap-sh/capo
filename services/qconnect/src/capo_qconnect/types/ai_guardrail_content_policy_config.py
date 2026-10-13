"""Generated from Smithy shape ``com.amazonaws.qconnect#AIGuardrailContentPolicyConfig``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_qconnect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_qconnect.types.guardrail_content_filters_config


class AIGuardrailContentPolicyConfig(TypedDict, closed=True):
    filters_config: "capo_qconnect.types.guardrail_content_filters_config.GuardrailContentFiltersConfig"
    """<p>Contains the type of the content filter and how strongly it should apply to prompts and model responses.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AIGuardrailContentPolicyConfig) -> dict:
    out: dict = {}
    import capo_qconnect.types.guardrail_content_filters_config

    out["filtersConfig"] = (
        capo_qconnect.types.guardrail_content_filters_config.serialize_json(
            value["filters_config"]
        )
    )
    return out


def deserialize_json(data: dict) -> AIGuardrailContentPolicyConfig:
    out: AIGuardrailContentPolicyConfig = {}  # type: ignore[typeddict-item]
    if data.get("filtersConfig") is not None:
        import capo_qconnect.types.guardrail_content_filters_config

        out["filters_config"] = (
            capo_qconnect.types.guardrail_content_filters_config.deserialize_json(
                data["filtersConfig"]
            )
        )
    else:
        raise DeserializationError(
            "AIGuardrailContentPolicyConfig.filters_config required"
        )
    return out


def redact_sensitive(value: AIGuardrailContentPolicyConfig) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "filters_config" in value:
        import capo_qconnect.types.guardrail_content_filters_config

        out["filters_config"] = (
            capo_qconnect.types.guardrail_content_filters_config.redact_sensitive(
                value["filters_config"]
            )
        )
    return out
