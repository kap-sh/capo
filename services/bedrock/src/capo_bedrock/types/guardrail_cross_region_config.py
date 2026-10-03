"""Generated from Smithy shape ``com.amazonaws.bedrock#GuardrailCrossRegionConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock.types.guardrail_cross_region_guardrail_profile_identifier


class GuardrailCrossRegionConfig(TypedDict, closed=True):
    guardrail_profile_identifier: "capo_bedrock.types.guardrail_cross_region_guardrail_profile_identifier.GuardrailCrossRegionGuardrailProfileIdentifier"
    """<p>The ID or Amazon Resource Name (ARN) of the guardrail profile that your guardrail is using. Guardrail profile availability depends on your current Amazon Web Services Region. For more information, see the <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-cross-region-support.html">Amazon Bedrock User Guide</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailCrossRegionConfig) -> dict:
    out: dict = {}
    out["guardrailProfileIdentifier"] = value["guardrail_profile_identifier"]
    return out


def deserialize_json(data: dict) -> GuardrailCrossRegionConfig:
    out: GuardrailCrossRegionConfig = {}  # type: ignore[typeddict-item]
    if data.get("guardrailProfileIdentifier") is not None:
        out["guardrail_profile_identifier"] = data["guardrailProfileIdentifier"]
    else:
        raise DeserializationError(
            "GuardrailCrossRegionConfig.guardrail_profile_identifier required"
        )
    return out
