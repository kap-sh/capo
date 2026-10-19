"""Generated from Smithy shape ``com.amazonaws.voiceid#VoiceSpoofingRisk``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_voice_id.types.score


class VoiceSpoofingRisk(TypedDict, closed=True):
    risk_score: "capo_voice_id.types.score.Score"
    """<p>The score indicating the likelihood of speaker’s voice being spoofed.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: VoiceSpoofingRisk) -> dict:
    out: dict = {}
    out["RiskScore"] = value["risk_score"]
    return out


def deserialize_aws_json_1_0(data: dict) -> VoiceSpoofingRisk:
    out: VoiceSpoofingRisk = {}  # type: ignore[typeddict-item]
    if data.get("RiskScore") is not None:
        out["risk_score"] = data["RiskScore"]
    else:
        out["risk_score"] = 0
    return out
