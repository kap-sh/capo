"""Generated from Smithy shape ``com.amazonaws.voiceid#KnownFraudsterRisk``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_voice_id.types.generated_fraudster_id
    import capo_voice_id.types.score


class KnownFraudsterRisk(TypedDict, closed=True):
    risk_score: "capo_voice_id.types.score.Score"
    """<p>The score indicating the likelihood the speaker is a known fraudster.</p>"""
    generated_fraudster_id: NotRequired[
        "capo_voice_id.types.generated_fraudster_id.GeneratedFraudsterId"
    ]
    """<p>The identifier of the fraudster that is the closest match to the speaker. If there are no fraudsters registered in a given domain, or if there are no fraudsters with a non-zero RiskScore, this value is <code>null</code>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: KnownFraudsterRisk) -> dict:
    out: dict = {}
    out["RiskScore"] = value["risk_score"]
    if "generated_fraudster_id" in value:
        out["GeneratedFraudsterId"] = value["generated_fraudster_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> KnownFraudsterRisk:
    out: KnownFraudsterRisk = {}  # type: ignore[typeddict-item]
    if data.get("RiskScore") is not None:
        out["risk_score"] = data["RiskScore"]
    else:
        out["risk_score"] = 0
    if data.get("GeneratedFraudsterId") is not None:
        out["generated_fraudster_id"] = data["GeneratedFraudsterId"]
    return out
