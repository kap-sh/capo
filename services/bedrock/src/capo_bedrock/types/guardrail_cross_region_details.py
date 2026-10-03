"""Generated from Smithy shape ``com.amazonaws.bedrock#GuardrailCrossRegionDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock.types.guardrail_cross_region_guardrail_profile_arn
    import capo_bedrock.types.guardrail_cross_region_guardrail_profile_id


class GuardrailCrossRegionDetails(TypedDict, closed=True):
    guardrail_profile_id: NotRequired[
        "capo_bedrock.types.guardrail_cross_region_guardrail_profile_id.GuardrailCrossRegionGuardrailProfileId"
    ]
    """<p>The ID of the guardrail profile that your guardrail is using. Profile availability depends on your current Amazon Web Services Region. For more information, see the <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-cross-region-support.html">Amazon Bedrock User Guide</a>.</p>"""
    guardrail_profile_arn: NotRequired[
        "capo_bedrock.types.guardrail_cross_region_guardrail_profile_arn.GuardrailCrossRegionGuardrailProfileArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the guardrail profile that you're using with your guardrail.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailCrossRegionDetails) -> dict:
    out: dict = {}
    if "guardrail_profile_id" in value:
        out["guardrailProfileId"] = value["guardrail_profile_id"]
    if "guardrail_profile_arn" in value:
        out["guardrailProfileArn"] = value["guardrail_profile_arn"]
    return out


def deserialize_json(data: dict) -> GuardrailCrossRegionDetails:
    out: GuardrailCrossRegionDetails = {}  # type: ignore[typeddict-item]
    if data.get("guardrailProfileId") is not None:
        out["guardrail_profile_id"] = data["guardrailProfileId"]
    if data.get("guardrailProfileArn") is not None:
        out["guardrail_profile_arn"] = data["guardrailProfileArn"]
    return out
